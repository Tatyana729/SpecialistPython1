# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
names_long = ['Z']
max_len = 1

for name in names:
    if len(name)>=max_len:
        names_long [0] = name
    if len(name)>=max_len:
        max_len=len(name)
print(names_long)
