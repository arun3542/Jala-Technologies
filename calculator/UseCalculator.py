from calculator.Calculator import Calculator
from calculator.ScientificCalculator import ScientificCalculator
print('---Welcome to Calculator---')
print('1 -- Basic Calculator')
print('2 -- Scientific Calculator')
print('3 -- exit')
print('Enter 1 or 2 or 3')

while True:
    calc = input('Type of calculator : ')
    if int(calc) == 1:
        c = Calculator()
        c.doCalculation()
        c.getResult()
    elif int(calc) == 2:
        s = ScientificCalculator()
        s.doCalculation()
        s.getResult()
    elif int(calc) == 3:
        break
    else:
        print('invalid input.please try again')








