from lift import Elevator
from lexer import Lexer

total_floors = 4

elevator1 = Elevator(1, total_floors)
elevator2 = Elevator(1, total_floors)

calls = [
    [-1, 1], [1, -1], [2, 1], [2, -1], [5, -1]
]
n_calls = len(calls)

finishes = [
    2, 0, 6, 1, 3
]

lexer = Lexer(total_floors, [elevator1, elevator2], calls, finishes)

elevator1.initLexer(lexer)
elevator2.initLexer(lexer)

lexer.run()
print("Количество общих перемещений: ", lexer.total_moves)
