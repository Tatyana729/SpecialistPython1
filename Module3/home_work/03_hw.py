# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
import random
numbers = [100,-100]
n = int(input('кол-во чисел:'))
sum_total = 0
i = 0
while i<=n:
     a = random.randint(numbers[1], numbers[0])
     if a>0 and a%2==0:
         sum_total += a
     i +=1
print(sum_total)
