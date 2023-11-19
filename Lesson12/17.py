word = input("Введите слово")
l = len(word)
g = ""
for i in range(l-1,-1,-1):
    g += str(word[i])
print(g)