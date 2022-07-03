# Бегун проводил ежедневные тренировки и записывал расстояния которые пробегал за занятия в метрах:
distances = [600, 755, 321.6, 1234, 231, 456.6, 4561, 1200, 456]
# Переведите все значения в футы (получить и вывести новый список)
fut_metr = 0.3048
distances_in_fut =[]
for el in distances:
    new_el = el/fut_metr
    distances_in_fut.append(new_el)
print(distances_in_fut)
