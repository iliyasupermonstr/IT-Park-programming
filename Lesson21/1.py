group = {"Iliya":13,
        'Timoha':12,
        "DJ Watermelon":11,
        "Bulat":12,
        "Zarina":13,
        "Kamil":54,
        "Daniil":13,
        "Kayum":12,
        "Iskandor":13,
        "Almaz":99
         }
name = "Milana"
age = 11
group[name] = age
age = group[name]
age = 0
count = 0
print(group)
for i in group:
    age += group[i]
    count += 1
print(age // count)