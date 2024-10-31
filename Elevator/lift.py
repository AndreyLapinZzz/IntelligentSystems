# from lexer import Lexer
# from main import lexer

class Elevator:
    def __init__(self, start_floor: int, total_floors: int) -> None:
        self.total_floors = total_floors
        self.state = "CLOSE"
        self.current_floor = start_floor
        self.commands = {
            "UP": self.goUp,
            "DOWN": self.goDown,
            "CLOSE": self.close,
            "OPEN": self.open,
            "STOP": self.stop
        }
        
    def initLexer(self, lexer):
        self.lexer = lexer
        
    def askWhatToDo(self, state):
        self.lexer.nextState(self, state)
    
    def makeAction(self, state: str):
        self.state = state
        self.commands[state]()
        self.askWhatToDo(self.state)
        # self.lexer.nextState(self, state)
    
    def close(self):
        print("close")
    
    def open(self):
        print("open")
    
    def goUp(self):
        print("up")
        if self.current_floor == self.total_floors:
            print("Нельзя проехать выше")
            self.state = "Exception"
            return

        self.current_floor += 1
    
    def goDown(self):
        print("down")
        if self.current_floor == 1:
            print("Нельзя проехать ниже")
            self.state = "Exception"
            return

        self.current_floor -= 1

    def stop(self):
        print("DoNothing")
