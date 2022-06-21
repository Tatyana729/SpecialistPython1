# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа

# TODO: your code here

tup = (2, 4, 6, -4, 12, 0, 5)
max = 0

for number in tup:
    if number>max:
        max=number
print(max)
