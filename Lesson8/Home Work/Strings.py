def check_string_brackets(input_string):
    count = 0
    for char in  input_string:
        if char == "(":
           count += 1
        elif char == ")":
            count -= 1
    if count == 0:
        print("YES")
    else:
        print("NO") 
input_string = input("Введите скобки :")
check_string_brackets(input_string)