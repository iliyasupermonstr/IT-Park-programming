
word = input("Введите число:")
l = len(word)
g = True
for i in range(0,int(l/2),1):
    if word[i]==word[l-i-1]:
        g = True
    else:
        g = False
if g :
    print("Число является полиндромом")
elif not g:
    print("Число не является палиндромом ")