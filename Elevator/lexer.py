from lift import Elevator
import threading
import time

class Lexer:
    def __init__(self, total_floors, e1 : Elevator, e2: Elevator, calls: list[list[int]], finishes: list[int]) -> None:
        self.total_floors = total_floors
        self.calls = calls
        self.finishes = finishes
        
        self.getClosest = {
            (True, True) : lambda *args: self.getClosestElevator(*args),
            (True, False) : lambda *args: 0,
            (False, True) : lambda *args: 1,
            (False, False) : lambda *args: None
        }
        
        self.actions = {
            -1 : {
                "OPEN" : "CLOSE",
                "CLOSE" : "UP",
                "UP" : "UP",
                },
            1 : {
                "OPEN" : "CLOSE",
                "CLOSE": "DOWN",
                "DOWN" : "DOWN"
            },
            0 : {
                "UP": "OPEN",
                "DOWN": "OPEN",
                "OPEN": "CLOSE",
            }
        }

        self.elevators = {
            e1 : {
                "move": None,
                "start": None,
                "finish": None,
                "is_take": False,
                "ready": True
            },
            e2 : {
                "move": None,
                "start": None,
                "finish": None,
                "is_take": False,
                "ready": True
            }
        }
        
        self.lock = threading.Lock()
        self.isWork = False
        
        self.shouldStopOrNot = {
            True: "STOP",
            False: None
        }

    def handle_call(self, call, finish):
        start, direction = call
        elevators = list(self.elevators.keys())
        elevator_number = self.chooseElevator(elevators, start)
        elevator = elevators[elevator_number]

        with self.lock:
            self.setCallToElevator(call, finish, elevator)


    def do(self):
        self.isWork = True
        
        threads = []
        while self.isWork:
            try:
                next_call = self.getNextCall()
                call, finish = next_call  # Попытка распаковки
                print(f"New call: {call}")
                thread = threading.Thread(target=self.handle_call, args=(call, finish))
                threads.append(thread)
                thread.start()
            except TypeError:  # Если next_call - None, возникнет ошибка распаковки
                break

        for thread in threads:
            thread.join()  # Ждем завершения всех потоков

        return False

    def setCallToElevator(self, call, finish, elevator: Elevator):
        self.elevators[elevator]["start"] = call[0]
        self.elevators[elevator]["finish"] = finish
        self.elevators[elevator]["ready"] = False
        self.elevators[elevator]["move"] = call[0]
        self.elevators[elevator]["is_take"] = False
        elevator.state = "CLOSE"
        self.nextState(elevator)

    def getNextCall(self):
        try:
            call = self.calls.pop(0)
            finish = self.finishes.pop(0)
            return call, finish
        except IndexError:
            self.isWork = False
            return None

    def chooseElevator(self, elevators: list[Elevator], start: int):
        e1, e2 = elevators
        e1_ready = self.elevators[e1]["ready"]
        e2_ready = self.elevators[e2]["ready"]
        key = e1_ready, e2_ready
        
        return self.getClosest[key](e1.current_floor, e2.current_floor, start)

    def getClosestElevator(self, f1: int, f2: int, start: int):
        return int(abs(f1 - start) > abs(f2 - start))
    
    def f(self, floor, move):
        return (floor > move) - (floor < move)
        # 1 if floor > move; 0 if floor == move; -1 if floor < move
    
    def chooseNextState(self, elevator, state, floor):
        move = self.elevators[elevator]["move"]
        
        floor_move = self.f(floor, move)
        print("state: ", state)
        print("floor_move: ", floor_move)
        action = self.actions[floor_move][state]
        
        return action

    def nextState(self, elevator: Elevator):
        state = elevator.state
        floor = elevator.current_floor
        time.sleep(0.3)
        
        print("floor: ", floor)
        print(self.elevators[elevator])
        
        if state == "Exception":
            self.elevators[elevator]["ready"] = True
            return

        next_state = self.chooseNextState(elevator, state, floor)
        if state == "OPEN":
            if self.elevators[elevator]["is_take"]:
                self.elevators[elevator]["ready"] = True
                return
            self.elevators[elevator]["is_take"] = True
            self.elevators[elevator]["move"] = self.elevators[elevator]["finish"]

        elevator.makeAction(next_state)
