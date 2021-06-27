# Create a class with DEFAULT fields and methods. Access these fields and methods
# from any other class in the same package


class Person:

    def __init__(self, name, last_name):
        self.name = name       # public
        self.last_name = last_name

    def who(self):
        print('name  : ', self.name)
        print('last_name : ', self.last_name)

    def fun(self):            # public method
        print('This is public method')



a = Person('aru ','fadf')

