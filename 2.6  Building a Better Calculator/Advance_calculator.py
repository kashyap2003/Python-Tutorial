num1 = float(input("Enter a number: "))
op = input("Enter Operator: ")
num2 = float(input("Enter 2nd number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num2*num1)
elif op == "/":
    print(num1/num2)
elif op == "%":
    print(num1%num2)
else:
    print("Invalid Operator")
