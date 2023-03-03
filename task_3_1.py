# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

import random
count_list = int(input("Введите длину списка: "))
list_numbers = []
desired_number = int(input("Введите искомое число: "))
count_desired_numbers = 0
difference_desired_number = 101
close_to_desired_number = 0

for number in range(0, count_list):
    list_numbers.append(random.randint(1, 100))

print("Ваш список:")
print(list_numbers)

for number in list_numbers:
    if number == desired_number:
        count_desired_numbers += 1

if count_desired_numbers == 0:
    for number in list_numbers:
        if difference_desired_number > abs(number - desired_number):
            difference_desired_number = abs(number - desired_number)
            close_to_desired_number = number
    print(f"Число {desired_number} не встречается в вашем списке. Максимально близкое к нему число - {close_to_desired_number}")
else:
    print(f"Число {desired_number} встречается {count_desired_numbers} раз, в вашем списке")