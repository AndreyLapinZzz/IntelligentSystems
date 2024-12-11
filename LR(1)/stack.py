class Stack:
    def __init__(self, init_value):
        self.stack = []
        self.push(init_value)

    def push(self, value):
        self.stack.append(value)

    def removeFirst(self):
        try:
            return self.stack.pop()
        except IndexError:
            raise
    
    def remove(self, n):
        try:
            self.stack = self.stack[:len(self.stack)-n+1]
            self.stack.pop()
        except IndexError:
            raise

    def getLength(self):
        return len(self.stack)
