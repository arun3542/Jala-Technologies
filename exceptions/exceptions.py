# 1. Write a program to generate Arithmetic Exception without exception handling
def arithmetic_exception():
    x = 1
    y = 0
    x/y

print('--2')
# 2. Handle the Arithmetic exception using try-catch block
x = 1
y = 0
try:
    a = x/y
except:
    print('can\'t divide by zero')

print('--3')

# 3. Write a program with multiple catch blocks

try:
    x/y
except ZeroDivisionError:
    print('can\'t divide by zero')
except ArithmeticError:
    print('error')
except TypeError:
    print('TypeError')

print('--4')

# 4.Write a program to throw exception with your own message

try:
    a = x/y
except:
    print('can\'t divide by zero')

print('--5')

# 5.Write a program to create your own exception

class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


def check_value(a):
    try:
        if a<10:
            raise ValueTooSmallError
    except ValueTooSmallError:
        print('value is too small')


print('--6')

# 6.Write a program with finally block

try:
    a = x/y
except:
    print('can\'t divide by zero')
finally:
    print('executed successfully')

print('--7')

# 7.Write a program to generate Arithmetic Exception

try:
    a = x/y
except:
    print('can\'t divide by zero')

print('--8')

# 8.Write a program to generate NameError

try:
    print(a)
except NameError:
    print('name not found')

print('--9')

# 9.Write a program to generate IOError

try:
    f = open("foo.txt", 'r')
except IOError as e:
    print(e)

print('--10')

# 10.Write a program to generate EOFError

try:
    while True:
        data = input('prompt ')
        print('data')
except EOFError as e:
    print('end of file error')







