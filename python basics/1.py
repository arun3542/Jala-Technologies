# How to create a class, object, method and its signature


class Person():
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return self.name

    def person_name(self):
        print(self.name)


arun = Person('Arun')
arun.person_name()


