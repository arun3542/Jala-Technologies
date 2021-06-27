'''     A, B and C are classes
        A is a super class. B is a sub class of A. C is a sub class of B.
        Create three methods in each class, 2 methods are specific to each class and third
        method (override method) should be in all three Classes A, B and C
        Create a class with main method. Create an object for each class A, B and C in main
        method and call every method of each class using its own object/instance.
        Call an overridden method with super class reference to B and C class’s objects
        Runtime Polymorphism with Data Members/Instance variables, Repeat the above
        process only for data members
'''


class GrandParent():

    def __init__(self):
        self.value = "Inside GrandParent"

    def show(self):
        print(self.value)

    def money(self):
        print('Iam Grand parent and I have 10 lakhs')


class Parent(GrandParent):

    def __init__(self):
        self.value = "Inside Parent"

    def show(self):
        print(self.value)


class Child(Parent):
    def __init__(self):
        self.value = 'Inside Child'

    def show(self):
        print(self.value)


gp = GrandParent()
p = Parent()
c = Child()

c.money()

for i in (gp,p,c):
    i.show()
