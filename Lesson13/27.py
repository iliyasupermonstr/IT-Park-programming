count = int(input("Введите количество элементов:"))
list = []
for i in range(0,count):
    word = input("Введите элемент:")
    list.append(word)
print(" ".join(list))