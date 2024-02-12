TEXT = "пhhтрп"
seen = {}

for i in TEXT:
    if i in seen:
        seen[i] += 1
    else:
        seen[i] = 1

max_value = max(seen, key=seen.get)
print('Наиболее встречаемый символ:', max_value)