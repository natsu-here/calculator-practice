import math

def input_number(num):
    while True:
        try:
            return float(input(num).replace(",", "."))
        except ValueError:
            print("Помилка! Можна ввести тільки число")

def division_zero_error(num_1, num_2):
    while True:
        try:
            return num_1/num_2
        except ZeroDivisionError:
            print("Ділити на 0 не можна!")
            num_2 = input_number("Введіть число: ")

def root_to_power(num, power):
    if num < 0:
        if power % 2 == 0:
            return "Корінь парного степеня з від'ємного числа неможливий"
        else:
            return -math.pow(abs(num), 1 / power)
    elif num == 0:
        if power < 0:
            return "Корінь від'ємного ступеня з нуля — це ділення на 0!"
        else:
            return 0
    return math.pow(num, 1/power)

def choise_radians_degrees(num):
    while True:
        radians_degrees = input("Це число в радіанах чи в градусах? Введіть r(радіани) або g(градуси):\n")
        radians_degrees = radians_degrees.strip().lower()
        if radians_degrees == "r":
            return num
        elif radians_degrees == "g":
            return math.radians(num)
        else:
            print("Невірний ввод!")

def negative_number_function(num, funk):
    while True:
        try:
            return funk(num)
        except ValueError:
            print("Помилка! Число від'ємне!")
            num = input_number("Введіть додатне число: ")

def check_num_for_int(num):
    while num % 1 != 0.0:
        print("Число має бути цілим")
        num = input_number("Введіть число:\n")
    return num

def engineering_calculator(action):
    result = None
    x = input_number("Введіть число:\n")
    match action:
        case 1:
            y = input_number("Введіть друге число:\n")
            result = x + y
        case 2:
            y = input_number("Введіть друге число:\n")
            result = x - y
        case 3:
            y = input_number("Введіть друге число:\n")
            result = x * y
        case 4:
            y = input_number("Введіть друге число:\n")
            result = division_zero_error(x, y)
        case 5:

            y = input_number("Введіть друге число:\n")
            result = math.pow(x, y)
        case 6:
            result = negative_number_function(x, math.sqrt)
        case 7:
            result = math.cbrt(x)
        case 8:
            n = input_number("Введіть n (ступінь):\n")
            while n == 0:
                print("Ступень кореня не може бути 0!")
                n = input_number("Введіть n (ступінь):\n")
            result = root_to_power(x, n)
        case 9:
            result = math.sin(choise_radians_degrees(x))
        case 10:
            result = math.cos(choise_radians_degrees(x))
        case 11:
            result = math.tan(choise_radians_degrees(x))
        case 12:
            result = negative_number_function(x, math.log)
        case 13:
            result = negative_number_function(x, math.log10)
        case 14:
            while x <= 0:
                print("Число логарифма має бути > 0")
                x = input_number("Введіть число > 0:\n")
            base = input_number("Введіть base: ")
            while base <= 0 or base == 1:
                print("База має бути > 0 і не дорівнювати 1")
                base = input_number("Введіть base: ")
            result = math.log(x, base)
        case 15:
            factorial_num = check_num_for_int(x)
            result = negative_number_function(factorial_num, math.factorial)
        case 16:
            result = math.fabs(x)
        case 17:
            result = division_zero_error(1, x)
        case _:
            result = "Такої дії не існує"
    return f"Результат: {result}\n"

while True:
    print("Виберіть дію:")
    print("1 - додавання\n2 - віднімання\n3 - множення\n4 - ділення\n5 - зведення у ступінь\n6 - квадратний корінь")
    print("7 - кубічний корінь\n8 - корінь в n ступені\n9 - sin(x)\n10 - cos(x)\n11 - tan(x)\n12 - ln(x) натуральний")
    print("13 - log10(x) десятичний\n14 - log(a, base)\n15 - факторіал(x) \n16 - |x|\n17 - 1/x\n18 - вийти")
    try:
        user_action = int(input("\nВведіть бажану дію:\n"))
    except ValueError:
        print("Введіть НОМЕР дії (цифрою)")
        continue
    if user_action == 18:
        break
    result_action = engineering_calculator(user_action)
    print(result_action)
