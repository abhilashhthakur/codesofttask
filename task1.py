print("Welcome to Basic Calculator ")
a = int(input("Enter First No.="))
b = int(input("Enter Second No.="))
case = str(input("Enter Arithmetic Operation(+,-,*,/) ="))
if case == "+":
    print(a + b)
elif case == "-":
    print(a - b)
elif case == "*":
    print(a * b)
elif case == "/":
    print(a / b)
else:
    print("Enter Correct Operation !")
