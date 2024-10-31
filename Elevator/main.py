from lift import Elevator
from lexer import Lexer
from generate_calls import generate_calls

total_floors = 11
n_calls = 10

calls, finishes = generate_calls(total_floors=total_floors, n_calls=n_calls)
elevator1 = Elevator(1, total_floors)
elevator2 = Elevator(1, total_floors)

print(f"all calls: \n{calls}\n {finishes}")

lexer = Lexer(total_floors, elevator1, elevator2, calls, finishes)

elevator1.initLexer(lexer)
elevator2.initLexer(lexer)

flag = True
while flag:
    flag = lexer.do()
