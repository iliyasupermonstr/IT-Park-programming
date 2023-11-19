
word = input("Введите слово:")
l = len(word)
g = True
for i in range(0,int(l/2),1):
    if word[i]==word[l-i-1]:
        g == True
    else:
        g == False
if g == True:
    print("Слово является полиндромом")
elif g ==False:
    print("Слово не является палиндромом ")
