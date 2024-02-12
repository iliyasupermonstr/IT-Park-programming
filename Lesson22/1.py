cost = int(input("Введите цену"))
rise = int(input("Введите на сколько процентов подорожал товар"))
wallet = int(input("Введите сколько у вас есть денег"))
fin = cost + cost / 100 * rise

final = wallet // fin
print(final)