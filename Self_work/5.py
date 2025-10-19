year = int(input("Введите год: "))

if (year % 400 == 0):
    print(f"{year} является високосным годом.")
elif (year % 100 == 0):
    print(f"{year} не является високосным годом.")
elif (year % 4 == 0):
    print(f"{year} является високосным годом.")
else:
    print(f"{year} не является високосным годом.")
