print("hello")

a = float(input("Введіть перше число: "))
op = input("Операція (+ - * /): ")
b = float(input("Введіть друге число: "))

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Невідома операція")
