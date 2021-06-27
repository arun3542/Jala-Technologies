# 1. Create an ArrayList of type String with 10 string elements. Add 10 string elements to
# ArrayList and perform the below operations
# Add an element to the ArrayList
# Iterate through the ArrayList by using Iterator object
# Add an element at a specific index
# Remove an element from the ArrayList, Remove at an index
# Update the element at a specific index
# Check the element is present at a particular index
# Get an element at a particular index
# Find out the size of the ArrayList
# Check the given element is present in the ArrayList
# Remove all elements of the ArrayList


list = ['a','b','c','d','e','f','g','h','i','j']

def add(a):
    list.append(a)

def iterate(a):
    for i in a:
        print(i)

def insert(a,pos):
    list.insert(a,pos)

def remove(a):
    list.remove(a)

def update(a,pos):
    list[pos] = a


def check(a):
    return a in list

def getElement(a):
    return list[a]

def length(a):
    return len(a)

def clear():
    list.clear()

