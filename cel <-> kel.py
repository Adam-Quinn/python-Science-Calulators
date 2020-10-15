from defnvar import add, subtract

num1 = 0
op = 273.15
ans = ""
ctk = int(input("1. Celsius to kelvin\n2. Kelvin to celsius\n"
                "Enter the number of the action you want to preform here: "))

if ctk == 1:
    num1 = int(input("Enter temperature in celsius: "))
    ans = add(num1, op)
    print(num1, "+", op, "=", ans)
    exit()
elif ctk == 2:
    num1 = int(input("Enter temperature in kelvins: "))
    ans = subtract(op, num1)
    print(num1, "-", op, "=", ans)
    exit()
else:
    print("Enter the number next to the action you want to preform")
    exit()
