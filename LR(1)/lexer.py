class Lexer:
    def __init__(self):
        self.makeAction = {
            "S": lambda next_state: self.shift(next_state),
            "R": lambda num_rule: self.reduction(num_rule)
        }

        self.result = {
            (1, "S"): "Удовлетворяет грамматике"
        }

    def initAll(self, symbols_stack, states_stack, DKA, terminals, rule_symbol, rule_length):
        self.symbols_stack = symbols_stack
        self.states_stack = states_stack
        self.DKA = DKA
        self.terminals = terminals
        self.rule_symbol = rule_symbol
        self.rule_length = rule_length

    def initInput(self, input):
        self.input = iter(input)

    def run(self):
        self.state = 1
        self.current_symbol = next(self.input)
        self.error = False
        while not self.error and not (self.state == 1 and self.current_symbol == "S"):
            self.next()

        print(self.result.get((self.state, self.current_symbol), "Не удовлетворяет грамматике"))

    def next(self):
        try:
            print(f"state: {type(self.state), self.state}\nsymbol: {self.current_symbol}")
            print(f"symbols_stack: {self.symbols_stack.stack}\nstates_stack: {self.states_stack.stack}")
            self.action = self.DKA[self.state][self.current_symbol]
            print(self.action)
            print()
            self.shiftOrReduction()
        except KeyError:
            print(self.DKA)
            print(self.state)
            print(self.current_symbol)
            print("next ERROR")
            print(self.symbols_stack.stack)
            self.error = True

    def shiftOrReduction(self):
        shift_or_reduction = self.action[0]
        num = int(self.action[1])
        self.makeAction[shift_or_reduction](num)

    def shift(self, next_state):
        self.symbols_stack.push(self.current_symbol)
        self.states_stack.push(next_state)
        self.state = next_state
        # try:
        # self.terminals.index(self.current_symbol)
        print("new symbol: ", self.current_symbol)
        self.current_symbol = next(self.input)
        print("new symbol2: ", self.current_symbol) 
        # except ValueError:
        #     pass

    def reduction(self, num_rule):
        try:
            n = self.rule_length[num_rule]
            print(f"reduct {n}")
            print(self.symbols_stack.stack)

            self.symbols_stack.remove(n)
            self.states_stack.remove(n)
            self.state = self.states_stack.removeFirst()
            self.current_symbol = self.rule_symbol[num_rule]
            print("new", self.symbols_stack.stack)
            # self.symbols_stack.push(self.current_symbol)
        except IndexError:
            print("reduction ERROR")
            self.error = True
