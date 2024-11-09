class Elevator:
    def __init__(self, floor, total_floors):
        self.total_floors = total_floors
        self.floor = floor
        self.state = "CLOSE"
        self.commands = {
            "UP": self.goUp,
            "DOWN": self.goDown,
            "CLOSE": self.close,
            "OPEN": self.open,
        }
    
    def initMoveCounter(self):
        self.moveCounter = 0
    
    def getMoveCounter(self):
        return self.moveCounter
    
    def initLexer(self, lexer):
        self.lexer = lexer

    def whatToDo(self):
        self.lexer.nextState(self)
    
    def makeAction(self, action):
        self.state = action
        self.moveCounter += 1
        self.commands[action]()
        self.whatToDo()
    
    def goUp(self):
        print("up")
        self.floor += 1
    
    def goDown(self):
        print("down")
        self.floor -= 1
    
    def open(self):
        print("open")
    
    def close(self):
        print("close")
