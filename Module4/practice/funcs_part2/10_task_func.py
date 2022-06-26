# Напишите функцию, находящую среднее арифметическое всех аргументов
# Функция должна вызываться с любым количеством аргументов
def average(*args):
    sum_el = 0
    for el in args:
        sum_el +=el
    average_el= sum_el/len(args)
    return f'{average_el:.3}'


print(average(3, 4, 8))
print(average(1, 4, 5, -3, 8, 4))
print(average(-10, 12, 6.3, -5.5, 7, 0.2))
