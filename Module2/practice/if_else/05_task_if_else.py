# Дано целое число m, задающее номер месяца года.
# Выведите строку — название времени года, соответствующего данному месяцу.
# Формат входных данных: дано целое число m (1 ≤ m ≤ 12).
# Формат выходных данных: требуется вывести название времени года

# TODO: your code here

m= int(input('введите число  от 1 до 12'))
if m == 1:
    print('январь')
elif m == 2:
    print('февраль')
elif m == 3:
    print('март')
elif m == 4:
    print('апрель')
elif m == 5:
    print('май')
elif m == 6:
    print('июнь')
elif m == 7:
    print('июль')
elif m == 8:
    print('август')
elif m == 9:
    print('сентябрь')
elif m == 10:
    print('октябрь')
elif m == 11:
    print('ноябрь')
elif m == 12:
    print('декабрь')
else:
    print('недопустимое число')
