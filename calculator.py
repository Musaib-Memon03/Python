#CALCULATOR IN PYTHON

num1=float(input("Please enter the first number :"))
op=input("Please enter the operator :")
num2=float(input("Please enter the second number :"))

if op =="+":
    print(num1 + num2)
elif op =="-":
    print(num1 - num2)
elif op =="*":
    print(num1 * num2)
elif op =="/":
    print(num1 / num2)
else:
    print("Invalid operator")
