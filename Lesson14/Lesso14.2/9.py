def task9(word):
    word_fin = ""
    for i in range(0,len(word)-1):
        if word[i+1] != "@":
            word_fin += word[i]
        elif word[i] == "@":
            word_fin += ""
        elif word[i+1] == "@":
            word_fin += ""

    print(word_fin)
w = "qwer@ty"
task9(w)