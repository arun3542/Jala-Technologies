# Write a function for arithmetic operators(+,-,*,/)


def arithmetic_operators(a,b,operator):

    c = 0

    def add(a,b):
        nonlocal c
        c = a+b

    def sub(a,b):
        nonlocal c

        c = a-b

    def mul(a,b):
        nonlocal c
        c = a*b

    def div(a,b):
        nonlocal c
        c = a/b

    if operator == '+':
        add(a,b)
    elif operator == '-':
        sub(a, b)
    elif operator == '*':
        mul(a, b)
    elif operator == '/':
        div(a, b)

    return c



