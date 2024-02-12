text = input("Введите текст:")
words = text.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
most_common_word = max(word_count,key=word_count.get)
longest_word  = max(words,key = len)
print("Наиболее встречающее слово ",most_common_word)
print("Самое длинное слово ", longest_word)