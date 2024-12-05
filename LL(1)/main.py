from lexer import Lexer
from stack import Stack
from states import StateN, StateNE, StateER, StateNSE, StateNAE, StateAER
import pickle

stack = Stack()
lexer = Lexer()

stateN = StateN(lexer)
stateNE = StateNE(lexer)
stateER = StateER(lexer)
stateNSE = StateNSE(lexer, stack)
stateNAE = StateNAE(lexer)
stateAER = StateAER(lexer)

object_dict = {
            (False, False, False, False) : stateN,
            (False, False, True, False) : stateNE,
            (False, False, True, True) : stateER,
            (False, True, True, False) : stateNSE,
            (True, False, True, False) : stateNAE,
            (True, False, True, True) : stateAER,
}

file_path = input('Путь к файлу с таблицей DKA: ')
with open(file_path, 'rb') as file:
    transitions = pickle.load(file)
    
inputs = [
    ['int', 'id', '(', 'int', 'id', ',', 'int', 'id', ')', '{', 'return', 'id', '+', 'id', '}', 'empty'],
    ['id', '(', ')', 'empty'],
    ['if', '(', 'true', ')', '{', '}', 'empty'],
    ['int', 'id', '=', 'NUM', '*', 'empty'],
    ['int', 'id', '(', 'int', 'id', ',', 'int', 'id', ')', '{', 'return', 'id', '+', 'id', 'int', 'id', '}', 'empty'],
    ['число', '+', 'число', '+', '(', 'число', ')', 'empty'],
    ['число', '+', 'число', 'empty']
]

lexer.initInput(inputs[0])
lexer.initStack(stack)
lexer.initDKA(transitions, object_dict)

lexer.run()
