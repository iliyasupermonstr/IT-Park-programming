list = ["Молоко","Вода","Соль","Сахар"]

while True:
    add = input("Введите,что вы хотите добавить в список: или введите / чтобы показать весь список")
    if add == "/":
        print(list)
        break
    else:
        list.append(add)