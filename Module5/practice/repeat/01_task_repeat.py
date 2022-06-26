import random

n = int(input('введите длину списка: '))
start_number = int(input('начало диапазона: '))
end_number = int(input('конец диапазона: '))


def gen_list(size, of, to):
 i = 0
 my_list = []
 while i <n:
  number = random.randint(start_number, end_number)
  my_list.append(number)
  i +=1
 return my_list

print(gen_list(n,start_number,end_number))
