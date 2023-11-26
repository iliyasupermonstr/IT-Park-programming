count = 0
while True:
    str = input("Введите строку:")
    if str != "стоп":
        count += 1
    elif str == "стоп":
        print("Было введено ",count," Строк(-и)")
        break