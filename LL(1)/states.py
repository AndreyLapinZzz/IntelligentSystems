from abc import ABC, abstractmethod
from lexer import Lexer
from stack import Stack

class State(ABC):
    @abstractmethod
    def next(self, state):
        pass

class StateNSE(State):
    def next(self, state):
        lexer.must_error()
        stack.push(state)
        return next_state

class StateNE(State):
    def next(self, state):
        lexer.must_error()
        return next_state

class StateNS(State):
    def next(self, state):
        stack.push(state)
        return lexer.next_state()

class StateANE(State):
    def next(self):
        lexer.must_error()
        lexer.accept()
        return lexer.next_state()

class StateNSER(State):
    def next(self):
        lexer.must_error()
        stack.push(state)
        lexer.return_()  # return может быть зарезервированным словом, поэтому лучше использовать return_() или другое имя
        return next_state
