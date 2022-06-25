# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
# import random
# numbers = []
# print(random.randint(10, 20))  # раскомментируйте, чтобы посмотреть работу функции randint
# TODO: your code here

import random
numbers = [100,-100]
n = int(input('кол-во чисел:'))
list_total =[]
i = 0
while i<n:
     a = random.randint(numbers[1], numbers[0])
     list_total.append(a)
     i +=1
print(','.join(map(str,list_total)))

# вариант 2
# print(str(list_total).strip('[]'))
