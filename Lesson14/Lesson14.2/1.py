
def task1():
    num_1 = 20
    num_2 = int(input("Введите число:"))
    if num_2 > num_1:
        print(num_2,">",num_1)
    elif num_2 < num_1:
        print(num_2,"<",num_1)
    elif num_2 == num_1:
        print(num_2,"=",num_1)
    else:
        print("Ошибка,повторите попытку!")
task1()