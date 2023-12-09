def task7(num):
    factorial = 1
    for i in range(2,num+1,1):
        factorial *= i 
    print(factorial)
n = int(input("Введите число:"))
task7(n)