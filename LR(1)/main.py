import pickle

from lexer import Lexer
from stack import Stack

file_path_DKA = input('Путь к файлу с таблицей DKA: ')
with open(file_path_DKA, "rb") as f:
    state_table = pickle.load(f)

file_terminals = input('Путь к файлу с терминальными символами: ')
with open(file_terminals, "rb") as f:
    terminals = pickle.load(f)

file_rule_symbols = input('Путь к файлу для символовов в левой части правила: ')
with open(file_rule_symbols, "rb") as f:
    rule_symbol = pickle.load(f)

file_rule_length = input('Путь к файлу с длиной правых частей: ')
with open(file_rule_length, "rb") as f:
    rule_length = pickle.load(f)

symbols_stack = Stack("S")
states_stack = Stack(1)

lexer = Lexer()

inputs = [
    ['int', 'id', '(', 'int', 'id', ',', 'int', 'id', ')', '{', 'return', 'id', '+', 'id', '}', 'empty'],
    ['id', '(', ')', 'empty'],
    ['if', '(', 'true', ')', '{', '}', 'empty'],
    ['int', 'id', '=', 'NUM', '*', 'empty'],
    ['int', 'id', '(', 'int', 'id', ',', 'int', 'id', ')', '{', 'return', 'id', '+', 'id', 'int', 'id', '}', 'empty'],
    ['число', '+', 'число', '+', '(', 'число', ')', 'empty'],
    ['число', '+', 'число', 'empty']
]

lexer.initAll(
    symbols_stack,
    states_stack,
    state_table,
    terminals,
    rule_symbol,
    rule_length,
    inputs[0]
)

lexer.run()
