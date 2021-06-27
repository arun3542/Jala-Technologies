# Create a HashSet with at least 10 elements of type String
# Write program covering all the operations of HashSet

numbers = {1,2,3,4,5,6,7,8,9,10}

def length():
    return len(numbers)

def check(a):
    return a in numbers

def add(a):
    numbers.add(a)

def update(a):
    numbers.update(a)

def remove(a):
    numbers.remove(a)

def pop():
    numbers.pop()

def intersection(a):
    return numbers.intersection(a)