# 1. Write a class with 2 static variables, 2 Instance variables, 2 static methods, 2 instance methods
# and a main method.

class Person():
    country = 'India'                       # class variable
    state = 'Telangana'                     # class variable

    def __init__(self,first_name,last_name,age):
        self.firstName = first_name
        self.lastName = last_name           # instance variable
        self.age = age                      # instance variable

    def greet(self):
        Person.location(self)

    def fullname(self):
        return self.firstName + self.lastName

    @classmethod
    def location(cls,self):             # can't call instance methods in class method without giving object as parameter
        print('Hi ',self.firstName,'.your age is',self.age)
        print('your fullname is : ',cls.fullname(self))
        print('country :',self.country,'state : ',cls.state)


arun = Person('Arun','poloju',22)

arun.greet()
Person.location(arun)

