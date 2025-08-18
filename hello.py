num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("choose operation +,-,*,/ :")
op = input ("Enter Operator:")
if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1-num2)
elif op == '*':
    print(num1*num2)
elif op == '/':
    if num2!=0:
        print(num1/num2)
    else : print ("Cannot divide by zero")
else :
    print ("Invalid Operator")