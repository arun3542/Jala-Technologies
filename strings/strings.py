
import re

# 1.Different ways creating a string

name = 'Arun'
name = "Arun"


print('--2')
# 2.Concatenating two strings using + operator


def concat(a,b):
    return a+b


print('--3')
# 3.Finding the length of the string


def length(a):
    return len(a)


print('--4')
# 4. Extract a string using Substring


def substring(a,start,end):
    return a[start:end]


print('--5')
# 5. Searching in strings using indexOf()


def search(a,char):
    return a.index(char)


print('--6')
# 6. Matching a String Against a Regular Expression With matches()


def match(a,pattern):
    return re.match(pattern,a)


print('--7')
# 7. Comparing strings using the methods equals()


def compare(a,b):
    return a == b


print('--8')
# 8.equalsIgnoreCase(), startsWith(), endsWith() and compareTo()
# --don't have equalsIgnoreCase(),compareTo() in python


def startswith(a,start):
    return a.startswith(start)


def endswith(a,end):
    return a.endswith(end)


print('--9')

# 9.Trimming strings with trim()
# --trim() not in python


def strip(a):
    return a.strip()


print('--10')

# 10. Replacing characters in strings with replace()


def replace(str,a,b):
    str = str.replace(a,b)
    return str


print('--11')
# 11. Splitting strings with split()


def split(str,delimeter = ' '):
    return str.split(delimeter)


print('--12')

# 12.Converting Numbers to Strings with valueOf()
# -- valueOf() not in python


def convert_str(a):
    return str(a)


print('--13')

# 13.Converting integer objects to Strings


def convert(a):
    return str(a)


print('--14')

# 14.Converting to uppercase and lowercase


def upper(a):
    return a.upper()


def lower(a):
    return a.lower()







