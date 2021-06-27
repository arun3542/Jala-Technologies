from calculator.Calc import Calc
import math


class Calculate(Calc):

    def __init__(self):
        pass

    def doCalculation(self):
        if self.char == '+':
            result = self.a+self.b
            self.result = result
        elif self.char == '-':
            result = self.a - self.b
            self.result = result
        elif self.char == '*':
            result = self.a * self.b
            self.result = result
        elif self.char == '/':
            result = self.a / self.b
            self.result = result
        elif self.char == 'sine':
            result = math.sin(self.a)
            self.result = result
        elif self.char == 'cosine':
            result = math.cos(self.a)
            self.result = result
        elif self.char == 'tangent':
            result = math.tan(self.a)
            self.result = result
        elif self.char == 'log':
            result = math.log(self.a)
            self.result = result

        else:
            print('invalid input.please try again')

    def getResult(self):
        print(self.result)

    def calculate(self,a,char,b):
        self.a = a
        self.char = char
        self.b = b

    def calculate_s(self,a,operator):
        self.a = a
        self.char = operator

