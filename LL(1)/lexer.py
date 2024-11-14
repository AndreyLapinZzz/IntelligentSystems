from stack import Stack

class Lexer:
    def __init__(self):
        # self.symbols = {
        #     "a": "accept",
        #     "s": "stack",
        #     "e": "error",
        #     "r": "return"
        # }
        self.input = []
        self.current_symbol = ""

        self.naser_transition = {}
        self.state_transition_table = {}

    def accept(self):
        if self.input:
            self.current_symbol = self.input.pop(0)
            return True
        return False

    def must_error(self):
        # Варианты:
        # 1) Если текущий символ совпадает
        #    Вернуть следующий статус
        # 2) Если не совпадает
        #    2.1) Если ошибка истина, увеличить состояние на 1
        #    2.2) Если ошибка ложь, вернуть ошибку, которая не является LL(1) грамматикой
        pass

    def return_(self):
        return Stack.pop()

    def next_state(self, state):
        if self.current_symbol in self.symbols:
            return self.state_transition_table[state]
        if self.state_transition_table.get("error", False):
            return state + 1
        return "Error"  # Или вы можете вернуть код ошибки