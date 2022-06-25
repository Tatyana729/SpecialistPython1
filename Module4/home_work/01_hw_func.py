# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
   ticket_num = str(ticket_number)
   len1 = float(len(ticket_num) / 2)
   part1 = list(ticket_num [0:round(len1)])
   part2 = list(ticket_num [-round(len1):])
   sum_part1 = 0
   sum_part2 = 0
   if round(len1) != len1:
        return 'нечетное количество цифр в билете'
   else:
        for aa in part1:
            sum_part1 +=int(aa)
        for bb in part2:
            sum_part2 +=int(bb)
            if sum_part1==sum_part2:
                return 'счастливый билет'
        return "несчастливый билет"

#
# # # Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(435777))
print(lucky_ticket(221500))
