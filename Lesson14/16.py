list = [8,12,7,4,6,7,3,5,90,123456,7678]
num = 24
for i in range(0,len(list)):
    for n in range(len(list)-1,0,-1):
        if list[i] * list[n] == num:
            print(list[i],"X ",list[n]," =",list[i]*list[n])