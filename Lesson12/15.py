numbers = input("Введите числа через пробел:")
numbers = numbers.split(" ")
l = len(numbers)

g = 0
for i in range(0,l):
    g += int(numbers[i]) 
print(g/l)