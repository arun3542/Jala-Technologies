from calculator.Calculate import Calculate


class Calculator(Calculate):

    def __init__(self):
        super().calculate(int(input('enter first number: ')),input('enter operation: '),int(input('enter second number: ')))



