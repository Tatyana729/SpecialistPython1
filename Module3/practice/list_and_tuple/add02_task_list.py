# Пользователь вводит на экран дату в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.

# Подсказка: создайте списки с названием дней и названиями месяцев
# Примечание: для экономии времени, можно ограничить номер дня десятью.
# Примечание: склонениями названий можно принебречь

day = ['','первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое', 'десятое']
month = ['','января', 'февраля', 'марта','апреля', 'мая', 'июня','июля','августа','сентября','октября','ноября','декабря']
date_t = input('Введите число в фармате ДДММГГГ: ')

date_as_list = date_t.split('.')

str1 = int(date_as_list[0])
str2 = int(date_as_list[1])
str3 = int(date_as_list[2])

print(day[str1],month[str2],str3)
