def task6():
    str = input("Введите строку:")
    str_fin = ""
    for i in range(int(len(str)-1),-1,-1):
        str_fin += str[i]
    print(str_fin)
task6()
