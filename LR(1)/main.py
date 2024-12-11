import pickle

from lexer import Lexer
from stack import Stack

with open("DKA2.pkl", "rb") as f:
    state_table = pickle.load(f)

with open("terminals2.pkl", "rb") as f:
    terminals = pickle.load(f)

with open("rule_symbol2.pkl", "rb") as f:
    rule_symbol = pickle.load(f)

with open("rule_lengths", "rb") as f:
    rule_length = pickle.load(f)


symbols_stack = Stack("S")
states_stack = Stack(1)

lexer = Lexer()

# inputs = [
#     ['int', 'id', '(', 'int', 'id', ',', 'int', 'id', ')', '{', 'return', 'id', '+', 'id', '}', 'empty'],
#     ['id', '(', ')', 'empty'],
#     ['if', '(', 'true', ')', '{', '}', 'empty'],
#     ['int', 'id', '=', 'NUM', '*', 'empty'],
#     ['int', 'id', '(', 'int', 'id', ',', 'int', 'id', ')', '{', 'return', 'id', '+', 'id', 'int', 'id', '}', 'empty'],
#     ['число', '+', 'число', '+', '(', 'число', ')', 'empty'],
#     ['число', '+', 'число', 'empty']
# ]

inputs = [
    ['int', 'id', ',', 'id', ',', 'id', 'empty'],
    # ['int', 'id', ',', 'id', 'empty']
]

for input in inputs:
    lexer.initAll(
        symbols_stack,
        states_stack,
        state_table,
        terminals,
        rule_symbol,
        rule_length,
    )
    lexer.initInput(input)
    lexer.run()
