def swap(a,b):
    print(f"Before Swap A = {a} and B = {b}")
    a = a+b
    b = a-b
    a = a-b

    print(f"After Swap A = {a} and B = {b}")

a = int(input("Enter first number  :"))
b = int(input("Enter second number  :"))

swap(a,b)