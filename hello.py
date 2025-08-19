num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
print("Choose operation:'+', '-', '*', '/'")
op = input ("Enter Operator:")
if op == '+':
    print("Result:", num1 + num2)
elif op == '-':
    print("Result:", num1 - num2)
elif op == '*':
    print("Result:", num1 * num2)
elif op == '/':
    if num2!=0:
        print("Result:",num1 / num2)
    else:
        print("Division by zero not allowed")
else:
    print("Invalid operator.")     