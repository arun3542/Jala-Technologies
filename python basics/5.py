#  Define the local and Global variables with the same name and print both variables and
#  understand the scope of the variables


a = 20


def variables():
    a = 10
    print('I am local variable ', a)

variables()
print('I am Global variable',a)
