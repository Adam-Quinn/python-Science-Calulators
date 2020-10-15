from defnvar import divide

num1 = 0
ans = ""
ftc = int(input("1. Celsius to Fahrenheit\n2. Fahrenheit to celsius\n"
                "Enter the number of the action you want to preform here: "))

if ftc == 1:
    num1 = float(input("Enter the temperature in Celsius: "))
    ans = float(1.8 * num1 + 32)
    print("1.8 *", num1, "+ 32 =", ans)
elif ftc == 2:
    num1 = float(input("Enter the temperature in Fahrenheit: "))
    num2 = num1 - 32
    ans = divide(num2, 1.8)
    print("(" + str(num1), "- 32) / 1.8 =", ans)
else:
    exit()
