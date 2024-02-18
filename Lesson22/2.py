numbers = [123, 456, 789, 1023, 5678, 9999]

max_num = None

for num in numbers:
    if num % 2 != 0:
        if max_num is None or num > max_num:
            max_num = num

print("Самое большое число, оканчивающееся на нечетную цифру:", max_num)