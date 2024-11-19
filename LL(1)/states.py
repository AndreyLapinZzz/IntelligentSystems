from abc import ABC, abstractmethod

# state_transition_table[state][?]

from main import lexer
from main import stack

class State(ABC):
    @abstractmethod
    def next(self):
        pass

class StateN(State):
    def next(self):
        lexer.must_error_false()
        lexer.nextState()
        # return lexer.state_transition_table[lexer.state]['next_state']
    
class StateNR(State):
    def next(self):
        lexer.must_error_false()
        lexer.return_()
        # return lexer.state_transition_table[lexer.state]['next_state']

class StateNER(State):
    def next(self):
        lexer.must_error_true()
        lexer.return_()

class StateNSR(State):
    def next(self):
        lexer.must_error_false()
        stack.push(lexer.state + 1)
        lexer.return_()

class StateNA(State):
    def next(self):
        lexer.must_error_false()
        lexer.accept()
        return lexer.state_transition_table[lexer.state]['next_state']

class StateNAR(State):
    def next(self):
        lexer.must_error_false()
        lexer.accept()
        lexer.return_()

class StateNAER(State):
    def next(self):
        lexer.must_error_true()
        lexer.accept()
        lexer.return_()

class StateNSE(State):
    def next(self):
        lexer.must_error_true()
        stack.push(lexer.state + 1)
        return lexer.state_transition_table[lexer.state]['next_state']

class StateNE(State):
    def next(self):
        lexer.must_error_true()
        return lexer.state_transition_table[lexer.state]['next_state']

class StateNS(State):
    def next(self):
        lexer.must_error_false()
        stack.push(lexer.state + 1)
        return lexer.state_transition_table[lexer.state]['next_state']

class StateNAE(State):
    def next(self):
        lexer.must_error_true()
        lexer.accept()
        return lexer.state_transition_table[lexer.state]['next_state']

class StateNSER(State):
    def next(self):
        lexer.must_error_true()
        lexer.return_()
        stack.push(lexer.state + 1)
