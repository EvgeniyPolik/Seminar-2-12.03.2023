"""
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""
n = int(input('Введите число N: '))
power_two = 1
while power_two <= n:
    print(power_two)
    power_two *= 2