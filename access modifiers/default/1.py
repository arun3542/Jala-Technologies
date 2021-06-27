# Create a class with DEFAULT fields and methods. Access these fields and methods
# from any other class in the same package
import default


class Normal(default.Person):
    def __init__(self,name,last_name):
        super(Normal, self).__init__(name,last_name)


aru = Normal('arun','poloju')

aru.fun()
