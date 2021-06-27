# Create a class with PRIVATE fields, private method and a main method. Print the fields
# in main method. Call the private method in main method.
# Create a sub class and try to access the private fields and methods from sub class.


class Person:

    def __init__(self, name, last_name):
        self.name = name  # public
        self.__last_name = last_name  # private

    def who(self):
        print('name  : ', self.name)
        print('alias : ', self.__last_name)

    def __private(self):  # private method
        print('This is private method')

    def fun(self):  # public method
        print('This is public method')
        self.__private()


class Female(Person):
    def __init__(self, name, last_name):
        super().__init__(name, last_name)


a = Person('arun', 'poloju')

print(a._Person__last_name)

a._Person__private()

b = Female('anu', 'revoju')
print(b._Person__last_name)
b._Person__private()
