cost_fin = 0
count = 0

while True:
    cost = int(input("Введите стоимость товара:"))
    if cost == 0:
        print(cost_fin,cost_fin//count)
        break
    else:
         cost_fin += cost
         count += 1