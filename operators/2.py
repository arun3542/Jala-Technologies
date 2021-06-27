
# Write a method for increment and decrement operators(++, --)

x = 0


def increment_or_decrement(a):
    global x
    if a == '+':
        x += 1
    elif a == '-':
        x -= 1
