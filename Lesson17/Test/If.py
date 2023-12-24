num1 = int(input("Введите первое число:"))
while True:
    num2 = int(input("Введите второе число:"))
    spike = False
    while not spike:
        sintaxys = input("Какую операцию вы хотите провести?:")
        if sintaxys == ("*"):
            spike = True
            num1 = num1 * num2

        elif sintaxys == ("/"):
            spike = True
            num1 = num1 / num2

        elif sintaxys == ("+"):
            spike = True
            num1 = num1 + num2
        elif sintaxys == ("-"):
            spike = True
            num1 = num1 - num2
        if not spike:
            print("Ошибка повторите попытку")
        else:
            print(num1)
