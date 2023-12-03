login =  input("Введите логин:")
password = input("Введите почту")
log= True
passw = True
while True:
    for i in range(0, len(login)):
        if login[i] == "@":
            log = False
    for b in range(0,len(password)):
        if  password[b] == "@":
            passw = True
    if login and passw:
        print("Да")
        break
    elif not log:
        print("Некорректный логин, попробуйте еще раз!")
    elif not passw:
        print("Неккоректный адрес, попробуйте еще раз!")