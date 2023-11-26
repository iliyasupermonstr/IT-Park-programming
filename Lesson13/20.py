pon = 1
count = 1
n = int(input("Введите число:"))
while pon!= n:
    pon = pon* 2 
    count += 1
    if pon > n+1:
        print("Нет")
        break
if pon == n:
    print("2 в(-о) ",count," степени")

