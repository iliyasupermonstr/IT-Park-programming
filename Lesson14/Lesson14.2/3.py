def task3():
    num1 = int(input("Введите число с которого вы хотите начать диапазон:"))
    num2 = int(input("Введите число с которого вы хотите закончить диапазон:"))
    if num1 < num2:
        for i in range(num1,num2):
            print(i)
    elif num1 > num2:
        for i in range(num2,num1,-1):
            print(i)
    else:
        print("Ошибка,повторите попытку!")
