list = [5,8,2,93,2,2,5,33]
count_ev = 0
count_odd = 0
for i in list:
    if i % 2 == 0:
        count_ev += 1
    elif i % 2 != 0:
        count_odd += 1
print(count_ev,"-четных чисел",count_odd,"-нечетных чисел")