# 1. Create an abstract class with abstract and non-abstract methods.
# 2. Create a sub class for an abstract class. Create an object in the child class for the
# abstract class and access the non-abstract methods
# 3. Create an instance for the child class in child class and call abstract methods
# 4. Create an instance for the child class in child class and call non-abstract methods


from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self):
        print('animals can walk and run and crawl')


class Human(Animal):

    def move(self):
        super().move()
        print("I can walk and run")


class Snake(Animal):

    def move(self):
        print("I can crawl")


class Dog(Animal):

    def move(self):
        print("I can bark")


class Lion(Animal):

    def move(self):
        print("I can roar")


R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()