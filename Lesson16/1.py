class Kids_It_park:
    def __init__(self,group,children,teacher):
        print("Ваша группа",group,"Кол-во детей",children,"Название группы ",teacher)
Iliya = Kids_It_park(input("Введите название группы:"),int(input("Введите количество людей в группе:")),input("Введите имя учителя:"))