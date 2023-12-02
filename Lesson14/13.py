my_list = [8,12,7,4,6,7,3,5,90,123456,7678]
list = list(set(my_list))
num = 98
for i in range(0,len(my_list)):
    for n in range(len(my_list)-1,0,-1):
        if list[i] + list[n] == num:
            print(list[i],"+ ",list[n]," =",list[i]+list[n])