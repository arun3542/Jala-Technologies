# 1.Write a program to print “Bright IT Career” ten times using for loop


def loop():
    for i in range(11):
        print('Bright IT Career')


print('--2')

# 2.Write a java program to print 1 to 20 numbers using the while loop.

i = 1
def print_numbers(a):
    while a <= 20:
        print(a)
        a += 1

print('--3')

# 3.Program to equal operator and not equal operators

print(1 == 2)
print(2 != 3)


print('--4')
# 4.Write a program to print the odd and even numbers.


def odd_even(a,number):

    for i in range(a):
        if number == 'odd':
            if i%2 != 0:
                print(i)
        elif number =='even':
            if i%2 == 0:
                print(i)

print('--5')

# 5.Write a program to print largest number among three numbers.


def largest(a,b,c):
    if a>b:
        if a>c:
            return a
        elif c>b:
            return c
    elif b>c:
        return b
    else:
        return c


print('--6')


# 6.Write a program to print even number between 10 and 100 using while

def even_num():
    i = 10
    while i <= 100:
        if i % 2 == 0:
            print(i)
        i += 1


print('--7')

# 7.Write a program to print 1 to 10 using the do-while loop statement.

# ------python don't have do while loop


print('--8')
# 8.Write a program to find Armstrong number or not


def armstrong_number(a):

    sum = 0
    temp = a
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if a == sum:
        print(a, "is an Armstrong number")
    else:
        print(a, "is not an Armstrong number")


print('--9')

# 9.Write a program to find the prime or not.


def prime(a):
    for i in range(2, a):
        if (a % i) == 0:
            print(a, "is not a prime number")
            break
    else:
        print(a, "is a prime number")


print('--10')

# 10. Write a program to palindrome or not.

def palindrome(a):
    temp = a
    rev = 0
    while(temp > 0):
        dig = temp % 10
        rev  = rev * 10 + dig
        temp = temp // 10
    if a == rev:
        print("This value is a palindrome number!")
    else:
        print("This value is not a palindrome number!")


print('--11')

# 11.Program to check whether a number is EVEN or ODD using switch


def even_odd(a):
    if a%2 == 0:
        print('even')
    else:
        print('odd')


print('--12')

# 12. Print gender (Male/Female) program according to given M/F using switch


def male_female(a):
    if a == 'M':
        print('Male')
    elif a == 'F':
        print('Female')


print('--13')

# 13. Program for multiple if else statement(Largest number in 10,20 and 30)


def check_largernumber(a):
    if a>10:
        if a>20:
            if a>30:
                print(a, 'is greater than 30')
            else:
                print(a, 'is greater than 20')
        else:
            print(a, 'is greater than 10')


check_largernumber(12)
