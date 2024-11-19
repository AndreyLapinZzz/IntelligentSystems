class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        
    def pop(self):
        try:
            return lambda: self.stack.pop()
        except IndexError:
            print("Входная последовательность не удовлетворяет заданной LL(1) грамматике")
            return lambda: IndexError

    def getLength(self):
        return len(self.stack)