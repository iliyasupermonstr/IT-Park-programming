num_1 = int(input('Введите первое число:'))
num_2 = int(input('Введите второе число:'))
oper = input('Какую операцию вы хотите сделать(+/-/*//):')



if oper == '+':
    print('Получилось число:',num_1 + num_2)

if oper == '-':
    print('Получилось число:', num_1 - num_2)

if oper == '/':
    if num_2 == 0:
        print('На 0 делить нельзя!')
    else:
        print('Получилось число:', num_1 / num_2)

if oper == '*':
    print('Получилось число:', num_1 * num_2)
else:
    print('Ошибка,перезапустите программу')