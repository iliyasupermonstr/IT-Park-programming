
nums = input("Введите числа через пробел")
list = nums.split(" ")
fin = 0
for i in range(0,len(list)):
    fin += int(list[i])
print(fin)