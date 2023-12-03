def task7(num):
    factorial = 1
    for i in range(2,num+1,1):
        factorial *= i 
    print(factorial)
task7(5)