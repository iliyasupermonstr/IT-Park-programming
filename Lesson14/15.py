words = input("Введите все что угодно:")
words_fin = ""
for i in range(0,len(words)):
    words_fin += words[i]*2
print(words_fin)