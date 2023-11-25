def nums(n):
    for i in range(0,n+1):
        print(i)
    print("_________________________")
    for b in range(n,-1,-1):
        print(b)
num = int(input("Введите число"))
nums(num)