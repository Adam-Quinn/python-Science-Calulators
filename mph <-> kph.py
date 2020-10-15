# all code writen by Adam-Quinn on github

def multiply(a, b):
    return a * b


num1 = 0
ans = ""
op = int(input("1. Kph to Mph\n2. Mph to Kph\n"
               "Enter the number of the action you want to preform here: "))

if op == 1:
    num1 = float(input("Enter speed here in Kph: "))
    ans = float(multiply(num1, 0.621371192))
    print(num1, "* 0.621371192 =", ans, "Mph")
elif op == 2:
    num1 = float(input("Enter speed here in Mph: "))
    ans = float(multiply(num1, 1.6093440006146922))
    print(num1, "* 1.6093440006146922 =", ans, "Kph")
else:
    exit()
