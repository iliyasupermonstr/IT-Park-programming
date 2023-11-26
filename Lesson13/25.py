login =  input("Введите логин:")
password = input("Введите почту")
log= True
passw = True
for i in range(0, len(login)):
    if login[i] == "@":
        log = False
for b in range(0,len(password)):
    if  password[b] == "@":
        passw = True
if login and passw == True:
    print("Да")
elif passw or login == False:
    print("Нет")