count = int(input("Введите количество элементов:"))
symb = input("Введите символ поиска:")
elem_list = []
for i in range(0,count):
    word = input("Введите элемент:")
    elem_list.append(word)

result = list(filter(lambda x: symb in x, elem_list))




print("\n".join(result))