from defnvar import add, subtract, divide, multiply

num1 = 0
op = 0
ans = ""
fck = float(input("1. Celsius to kelvin\n2. Kelvin to celsius\n3. Celsius to Fahrenheit\n4. Fahrenheit to celsius\n5. "
                  "Fahrenheit to Kelvin\n6. Kelvin to Fahrenheit\n"
                  "Enter the number of the action you want to preform here: "))
if fck == 1:
    op = 273.15
    num1 = float(input("Enter temperature in celsius: "))
    ans = add(num1, op)
    print(ans)
    exit()
elif fck == 2:
    op = 273.15
    num1 = float(input("Enter temperature in kelvins: "))
    ans = subtract(op, num1)
    print(ans)
    exit()
if fck == 3:
    num1 = float(input("Enter the temperature in Celsius: "))
    ans = float(1.8 * num1 + 32)
    print(ans)
elif fck == 4:
    num1 = float(input("Enter the temperature in Fahrenheit: "))
    num2 = num1 - 32
    ans = divide(num2, 1.8)
    print(ans)
elif fck == 5:
    num1 = float(input("Enter the temperature in Fahrenheit: "))
    num2 = subtract(num1, 32)
    num3 = divide(5, 9)
    num4 = multiply(num2, num3)
    ans = add(num4, 273.15)
    print(ans)
elif fck == 6:
    num1 = float(input("Enter temperature in kelvins: "))
    num2 = subtract(num1, 273.15)
    num3 = divide(9, 5)
    num4 = multiply(num2, num3)
    ans = add(num4, 32)
    print(ans)
else:
    exit()
