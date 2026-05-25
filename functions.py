def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
def power(a,b):
    return a ** b
def modulus(a,b):
    if b == 0:
        return "Error: Modulus by zero is not allowed."
    return a % b

a=5
b=10

print(f"Addition: {add(a,b)}")
print(f"Subtraction: {subtract(a,b)}")
print(f"Multiplication: {multiply(a,b)}")
print(f"Division: {divide(a,b)}")
print(f"Power: {power(a,b)}")
print(f"Modulus: {modulus(a,b)}")

