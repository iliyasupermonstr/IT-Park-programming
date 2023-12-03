def unique():
    words = input("Введите числа через пробел")
    my_list = words.split(" ")
    my_list = set(my_list)
    print(" ".join(list(my_list)))
unique()