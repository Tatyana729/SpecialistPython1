# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

# TODO: your code here

tuple1 = 1,2,3,4,5
tuple2 = 1,6,7,8,9
tuple3 = 10,11,12,9,8
i = 0

tuple_total = tuple3+tuple2+tuple1

for el_tuple in tuple_total:
    if tuple_total.count(el_tuple)>1:
        i+=0.5
print(int(i))
