from calculator.Calculate import Calculate


class ScientificCalculator(Calculate):

    def __init__(self):
        super().calculate_s(int(input('enter value: ')),input('scientific operation: '))
