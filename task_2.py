"""
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму
этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
"""
amount = int(input('Введите сумму загаданных чисел: '))
mul = int(input('Введите произведение загаданных чисел: '))
flag = False
for i in range(1000):
    for j in range(1000):
        if i + j == amount and i * j == mul:
            print(f'Число один: {i}, число два: {j}')
