class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        
    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            print("Не LL(1) грамматика")
            return False
