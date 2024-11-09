from lift import Elevator
from lexer import Lexer
from generate_calls import generate_calls

total_floors = 4
n_calls = 3

calls, finishes = generate_calls(total_floors=total_floors, n_calls=n_calls)
elevator1 = Elevator(1, total_floors)
elevator2 = Elevator(1, total_floors)

print(f"Вызовы: {calls}\n Финиши: {finishes}\n\n")

lexer = Lexer(total_floors, [elevator1, elevator2], calls, finishes)

elevator1.initLexer(lexer)
elevator2.initLexer(lexer)

lexer.run()
print("Количество общих перемещений: ", lexer.total_moves)
