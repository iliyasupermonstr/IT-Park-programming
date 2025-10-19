s = input("Введите строку")
letters = 0
numbers = 0

for char in s:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        numbers += 1

# Объединяем списки в строки


print("Буквы:", letters)  # Вывод: Буквы: HelloWorld
print("Цифры:", numbers)  # Вывод: Цифры: 123456
