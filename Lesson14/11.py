n = int(input("Введите число:"))
for i in range(1,n+1):
    if i % 7 == 0 or i % 11 == 0:
        print(i)