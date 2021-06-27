# Create a class with PROTECTED fields and methods. Access these fields and methods
# from any other class in the same package.
# Also, Access the PROTECTED fields and methods from child class located in a different
# package
# Access the PROTECTED fields and methods from any class in different package.

if __name__ == '__main__':
    from protected import Person


class Normal(Person):
    def __init__(self,name,last_name):
        super(Normal, self).__init__(name,last_name)


aru = Normal('arun','poloju')

aru._private()
