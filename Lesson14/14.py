num1 = 22
num2 = 99
for i in range(22,1,-1):
    if num1 % i == 0 and num2 % i == 0:
        print(i)
        break