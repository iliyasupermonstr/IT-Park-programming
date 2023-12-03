
def fact(n):
    fin = 1
    for i in range(1,n):
        fin += (fin * i)
    print(fin)
num = int(input("Введите число:"))
fact(num)