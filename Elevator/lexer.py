from lift import Elevator
# import concurrent.futures
import threading
import time

class Lexer:
    def __init__(self, total_floors, e1 : Elevator, e2: Elevator, calls: list[list[int]], finishes: list[int]) -> None:
        self.total_floors = total_floors
        self.calls = calls
        self.finishes = finishes

        self.elevators = {
            e1 : {
                "state": "CLOSE",
                # "elevator": e1,
                "start": None,
                "finish": None,
                "target": None,
                "direction": None,
                "ready": True
            },
            e2 : {
                "state": "CLOSE",
                # "elevator": e2,
                "start": None,
                "finish": None,
                "target": None,
                "direction": None,
                "ready": True
            }
        }
        
        self.lock = threading.Lock()
        self.isWork = False

    def handle_call(self, call, finish):
        start, direction = call
        elevator = self.chooseElevator(list(self.elevators.keys()), start)

        with self.lock:
            self.setCallToElevator(call, finish, elevator)


    def do(self):
        self.isWork = True
        
        threads = []
        while self.isWork:
            next_call = self.getNextCall()
            if next_call is None:
                break
            
            call, finish = next_call
            print(f"New call: {call}")
            thread = threading.Thread(target=self.handle_call, args=(call, finish))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()  # Ждем завершения всех потоков

        return False

    def setCallToElevator(self, call, finish, elevator):
        self.elevators[elevator]["start"] = call[0]
        self.elevators[elevator]["target"] = call[0]
        self.elevators[elevator]["finish"] = finish
        self.elevators[elevator]["direction"] = call[1]
        self.elevators[elevator]["ready"] = False
        self.nextState(elevator, self.elevators[elevator]["state"])

    def getNextCall(self):
        if len(self.calls) == 0:
            self.isWork = False
            return None
        call = self.calls.pop(0)
        finish = self.finishes.pop(0)
        return call, finish
    
    def chooseElevator(self, elevators: list[Elevator], start: int):
        e1, e2 = elevators
        if not self.elevators[e1]["ready"]:
            return e2
        
        if not self.elevators[e2]["ready"]:
            return e1
        
        closest = self.getClosesElevator(e1.current_floor, e2.current_floor, start)
        if closest == 0:
            return e1
        
        return e2
        
    def getClosesElevator(self, f1: int, f2: int, start: int):
        if abs(f1 - start) <= abs(f2 - start):
            return 0
        return 1
    
    def chooseNextState(self, elevator, state, floor):
        if state == "OPEN" and floor == self.elevators[elevator]["start"]:
            next_state = "CLOSE"
            self.elevators[elevator]["direction"] *= -1

        elif floor == self.elevators[elevator]["target"]:
            self.elevators[elevator]["target"] = self.elevators[elevator]["finish"]
            next_state = "OPEN"

        elif floor == self.elevators[elevator]["finish"]:
            next_state = "OPEN"

        elif floor < self.elevators[elevator]["target"]:
            next_state = "UP"
        
        elif floor > self.elevators[elevator]["target"]:
            next_state = "DOWN"
        
        elevator.makeAction(next_state)
        return next_state
    
    def nextState(self, elevator: Elevator, state: str):
        floor = elevator.current_floor
        time.sleep(0.3)
        
        if state == "Exception":
            
            if self.elevators[elevator]["finish"] == self.elevators[elevator]["target"]:
                self.elevators[elevator]["finish"] = floor
            else:
                self.elevators[elevator]["start"] = floor
    
            self.elevators[elevator]["target"] = floor
            elevator.makeAction("OPEN")
            return
        
        if state == "OPEN" and floor == self.elevators[elevator]["finish"]:
            self.elevators[elevator]["ready"] = True
            return
        
        print(floor)
        print(self.elevators[elevator])
        # print(elevator)
        next_state = self.chooseNextState(elevator, state, floor)
        self.elevators[elevator]["state"] = next_state
        # elevator.makeAction(next_state)
            