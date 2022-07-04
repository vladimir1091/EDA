from itertools import count
from tkinter import N
import numpy as np
number = np.random.randint(1, 100)
count = 0
while True:
    count += 1
    predict_number = int(input('Угадайте число от 1 до 100: '))
    if predict_number > number:
        print('Число должно быть меньше')
    elif predict_number < number:
        print('Число должно быть больше')
    else:
        print(f'Вы угодали число, это {number}, число попыток {count}')
        break