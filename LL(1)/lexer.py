from main import stack
from states import *

# import pickle 

# with open('saved_dictionary.pkl', 'wb') as f:
#     pickle.dump(dictionary, f)
        
# with open('saved_dictionary.pkl', 'rb') as f:
#     loaded_dict = pickle.load(f)


class Lexer:
    def __init__(self):
        self.state = 1
        self.current_symbol = "S"

        self.error = False

        self.state_transition_table = {} # state: next_state, error, accept, return, stack, guid_symbols
        self.objects = {}

        # accept stack error return
        self.object_dict = {
            [False, False, False, False] : StateN,
            [False, False, False, True] : StateNR,
            [False, False, True, False] : StateNE,
            [False, False, True, True] : StateNER,
            [False, True, False, False] : StateNS,
            [False, True, False, True] : StateNSR,
            [False, True, True, False] : StateNSE,
            [False, True, True, True] : StateNSER,
            [True, False, False, False] : StateNA,
            [True, False, False, True] : StateNAR,
            [True, False, True, False] : StateNAE,
            [True, False, True, True] : StateNAER,
            [True, True, False, False] : StateNAS,
            [True, True, False, True] : StateNASR,
            [True, True, True, False] : StateNASE,
            [True, True, True, True] : StateNASER,
        }
    
    def initObjects(self, transition_table):
        for current_state, row in transition_table.items():
            error, stack, return_, accept, guid_symbols, next_state = list(row.values())
            self.objects[current_state] = self.object_dict[[accept, stack, error, return_]]
    
    def run(self):
        while self.error == False and not (self.current_symbol == '/eps' and stack.getLength() == 0):
            obj = self.objects[self.state]
            obj.next()
            # self.state = next_state

    def accept(self):
        try:
            # Получаем следующий элемент
            self.current_symbol = next(self.input)
            return self.current_symbol
        except StopIteration:
            # Возвращаем None, если итератор достиг конца списка
            # return None
            self.error = True

    def return_(self):
        try:
            self.state = stack.pop()
        except IndexError:
            self.error = True

    def initInput(self, input):
        self.input = iter(input)

    def incrementState(self):
        self.state += 1

    def f(self):
        self.incrementState()
        return True

    def f2(self):
        self.error = True
        return True

# типо мне генерить не trans[state][symbols] : doSomething, а trans[state] = {s1 : v1, s2: v2 ...}

    def must_error_false(self):
        for symbol in all_symbols:
            if symbol in guid_symbols:
                transitions[self.state][symbol] = lambda: self.nextState()
            else:
                transitions[self.state][symbol] = lambda: self.f()
        transitions[self.state][self.current_symbol]

    def must_error_true(self):
        for symbol in all_symbols:
            if symbol in guid_symbols:
                transitions[self.state][symbol] = lambda: self.nextState()
            else:
                transitions[self.state][symbol] = lambda: self.f2()
            
        transitions[self.state][self.current_symbol]
        # Фактически я знаю заранее, для каких состоя

    def nextState(self):
        self.state = self.state_transition_table[self.state]['next_state']
        # Варианты:
        # 1) Если текущий символ совпадает
        #    Вернуть следующее состояние
        # 2) Если не совпадает
        #    2.1) Если ошибка истина, увеличить состояние на 1
        #    2.2) Если ошибка ложь, вернуть ошибку, которая не является LL(1) грамматикой