import operator

from numpy import intp, place


def calculator(a,b,ch):
    if ch =="+":
        print(f"Addition  = {a+b}")
    elif ch == "-":
        print(f"Subtraction  = {a-b}")
    elif ch == "*":
        print(f"Multiplication  = {a*b}")
    elif ch == "/":
        print(f"Division  = {a/b}")
    else:
        print("!please enter a valid number or operator")

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
op = input("Enter Operator [+,-,*,/] :")

calculator(num1,num2,op)