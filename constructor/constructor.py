# Write a class with a default constructor, one argument constructor and two argument
# constructors. Instantiate the class to call all the constructors of that class from a main
# class
class Addition:
    first = 0
    second = 0
    answer = 0

    # parameterized constructor
    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))

    def calculate(self):
        self.answer = self.first + self.second

a = Addition(100, 200)

a.calculate()
a.display()