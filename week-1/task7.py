a = float(input("First number:"))
n = input("Operation:")
b = float(input("Second number:"))
c = 0
if n == "+":
    c = a + b
if n == "-":
    c = a - b
if n == "*":
    c = a * b
if n == "/":
    if b != 0:
        c = a / b
    else:
        print("Error: division by zero!")
print(c)