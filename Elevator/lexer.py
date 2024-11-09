class Lexer:
    def __init__(self, total_floors, elevators, calls, finishes):
        self.total_floors = total_floors
        self.calls = calls
        self.finishes = finishes
        
        self.total_moves = 0
        
        self.elevator_by_number = {i: elevators[i] for i in range(len(elevators))}
        self.number_by_elevator = dict((v,k) for k, v in self.elevator_by_number.items())
        self.elevators = {
            elevator: {"calls": [], "finishes": [], "target": None} for elevator in elevators
        }
        
        self.initStates()
        self.initClosest()
        
    def run(self):
        while len(self.calls) != 0:
            first_call = self.calls[0]
            elevator_keys = list(self.elevators.keys())
            elevator_number = self.chooseElevator(elevator_keys, first_call[0])
            elevator = self.elevator_by_number[elevator_number]
            self.setNextCallToElevator(elevator)

    def setNextState(self, elevator, next_state):
        elevator.makeAction(next_state)

    def nextState(self, elevator):
        target = self.elevators[elevator]["target"]
        try:
            self.states[elevator.floor, elevator.state][target](elevator)
        except KeyError:
            print(f"Некорректный финальный этаж\nВызов не выполнен. Количество перемещений: {elevator.getMoveCounter()}\n")
            self.total_moves += elevator.getMoveCounter()
            return

    def check(self, elevator, next_state):
        try:
            target = self.elevators[elevator]["finishes"].pop(0)
            self.elevators[elevator]["target"] = target
            self.setNextState(elevator, next_state)
        except IndexError:
            print(f"Вызов выполнен\nКоличество перемещений: {elevator.getMoveCounter()}\n")
            self.total_moves += elevator.getMoveCounter()
            return

    def setNextCallToElevator(self, elevator):
        try:
            call, direction = self.calls.pop(0)
            finishes = self.finishes.pop(0)
            self.elevators[elevator]["calls"].append([call, direction])
            self.elevators[elevator]["target"] = call
            self.elevators[elevator]["finishes"].append(finishes)
            key = (elevator.floor, elevator.state)

            try:
                print(f"call {[call, direction]} задан лифту {self.number_by_elevator[elevator]}")
                elevator.initMoveCounter()
                self.states[key][call](elevator)
            except KeyError:
                print("Не удалось задать вызов лифту\n")
                return

        except IndexError:
            print("\n\nВызовов больше нет\n")
            return
    
    def initClosest(self):
        self.closest = {}
        for floor1 in range(1, self.total_floors + 1):
            for floor2 in range(1, self.total_floors + 1):
                self.closest[floor1, floor2] = {}
        
        for floor1 in range(1, self.total_floors + 1):
            for floor2 in range(1, self.total_floors + 1):
                for start_floor in range(1, self.total_floors + 1):
                    self.closest[floor1, floor2].update({start_floor: self.getClosest(floor1, floor2, start_floor)})
    
    def chooseElevator(self, elevators, start_floor):
        elevator_number = self.getClosest(elevators[0].floor, elevators[1].floor, start_floor)
        return elevator_number
    
    def getClosest(self, floor1, floor2, start_floor):
        return int(abs(floor1 - start_floor) > abs(floor2 - start_floor))
    
    def initStates(self):
        self.states = {}
        for floor in range(1, self.total_floors + 1):
            self.states[floor, "CLOSE"] = {}
            self.states[floor, "OPEN"] = {}
            self.states[floor, "DOWN"] = {}
            self.states[floor, "UP"] = {}
        
        for floor in range(1, self.total_floors + 1):
            for target in range(1, self.total_floors + 1):
                if floor > target:
                    self.states[floor, "CLOSE"].update({target: lambda elevator: self.setNextState(elevator, "DOWN")})
                    self.states[floor, "OPEN"].update({target: lambda elevator: self.setNextState(elevator, "CLOSE")})
                    self.states[floor, "DOWN"].update({target: lambda elevator: self.setNextState(elevator, "DOWN")})
                    self.states[floor, "UP"].update({target: lambda elevator: self.setNextState(elevator, "DOWN")})
                elif floor < target:
                    self.states[floor, "CLOSE"].update({target: lambda elevator: self.setNextState(elevator, "UP")})
                    self.states[floor, "OPEN"].update({target: lambda elevator: self.setNextState(elevator, "CLOSE")})
                    self.states[floor, "DOWN"].update({target: lambda elevator: self.setNextState(elevator, "UP")})
                    self.states[floor, "UP"].update({target: lambda elevator: self.setNextState(elevator, "UP")})
                else:
                    self.states[floor, "CLOSE"].update({target: lambda elevator: self.setNextState(elevator, "OPEN")})
                    self.states[floor, "OPEN"].update({target: lambda elevator: self.check(elevator, "CLOSE")})
                    self.states[floor, "DOWN"].update({target: lambda elevator: self.setNextState(elevator, "OPEN")})
                    self.states[floor, "UP"].update({target: lambda elevator: self.setNextState(elevator, "OPEN")})
