password = "1234"
def ask_password(atempt1,atempt2,atempt3):
    if atempt1 == password:
        print("Пароль принят!")
    if atempt2 == password:
        print("Пароль принят!")
    if atempt3 == password:
        print("Пароль принят!")
    else:
        print("Пароль не принят!")
ask_password(atempt1=input("Введите пароль"),atempt2=input("Введите пароль"),atempt3=input("Введите пароль"))