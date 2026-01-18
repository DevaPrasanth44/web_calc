def add(a, b):
    return float(a) + float(b)

def subtract(a, b):
    return float(a) - float(b)

def multiply(a, b):
    return float(a) * float(b)

def divide(a, b):
    if float(b) == 0:
        return "Cannot divide by zero"
    return float(a) / float(b)

def calculate(a, b, operation):
    if operation == "add":
        return add(a, b)
    elif operation == "subtract":
        return subtract(a, b)
    elif operation == "multiply":
        return multiply(a, b)
    elif operation == "divide":
        return divide(a, b)
    else:
        return "Invalid operation"
