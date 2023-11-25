cost_fin = 0
while True:
    cost = int(input("Введите стоимость товара:"))
    if cost <= 0:
        break
    if cost >= 1000:
        pon = cost * 0.95
        cost_fin += pon
    else:
         cost_fin += cost
print(int(cost_fin))