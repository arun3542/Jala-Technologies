# Create a class with PROTECTED fields and methods. Access these fields and methods
# from any other class in the same package.
# Also, Access the PROTECTED fields and methods from child class located in a different
# package
# Access the PROTECTED fields and methods from any class in different package


class Person:

    def __init__(self, name, last_name):
        self.name = name       # public
        self._last_name = last_name   # protected

    def who(self):
        print('name  : ', self.name)
        print('alias : ', self._last_name)

    def _private(self):          # protected method
        print('This is private method')

    def fun(self):            # public method
        print('This is public method')
        self._private()


a = Person('aru ','fadf')

