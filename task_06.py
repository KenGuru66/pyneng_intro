"""
Так как это первое задание, где нужно запросить что-то у пользователя,
эта часть уже написана
number_as_str = input("Введите число: ")

input ожидает ввода пользователя и после нажатия enter то, что пользователь
написал, попадает в переменную number_as_str. При этом input всегда возвращает
строку. Поэтому дальше строку number_as_str мы превращаем в integer функцией int.
В задании добавлен вывод pprint, чтобы посмотреть на значение переменных
number_as_str, number. Используется именно pprint, потому что обычный print
выводит на экран в одинаковом виде строку "4" и число 4.

Теперь надо написать условие, которое будет проверять значение переменной number
и выводить текст "correct", если number меньше или равно 10: "wrong".

Пример работы задания
$ python task_06.py
Введите число больше 10: 4
'4'
4
wrong

$ python task_06.py
Введите число больше 10: 20
'20'
20
correct
"""

from pprint import pprint


number_as_str = input("Введите число больше 10: ")
number = int(number_as_str)
pprint(number_as_str)
pprint(number)
if number > 10:
    print('correct')
else:
    print('wrong')
