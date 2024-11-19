from lexer import Lexer
from stack import Stack

lexer = Lexer()
stack = Stack()

# закончим работу, если текущий символ - пусто и вытащили из стэка END

# если есть в направляющих - переходим в состояние. Если s == True, кладём в стэк state + 1
# если accept есть, берём следующий символ
# если return есть, берём из стэка state и тек.сост = state

