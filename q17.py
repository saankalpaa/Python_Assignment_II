a = int(input('Enter firt number: '))
b = int(input('Enter second number: '))

op = input('Enter the operator: ')

def calc(a,b,operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        try:
            return a / b    
        except ZeroDivisionError:
            return None
print(calc(a,b,op))

