word1 = input("Введите слово:")
word2 = input("Введите второе слово:")
pon1 = False
pon2 = False
if word1 == "да"or "нет":
    pon1 = True
else:
    pon1 = False
if word2 == 'да'or "нет":
    pon2 =  True
else:
    pon2 = False
if pon1 and pon2 == True:
    print("Да")
else:
    print("Нет")