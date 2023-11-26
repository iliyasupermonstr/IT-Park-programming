def flip(n):
    word = ""
    for i in range(len(n),0,-1):
        word += str(i)
    print(word)
number = input("Введите число:")
flip(number)