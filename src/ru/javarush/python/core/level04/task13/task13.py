"""
Напишите функцию generate_random_number(), которая выводит на экран случайноечисло
от -200 до 0.
Требования:
•	Программа должна импортировать модуль random для генерации случайных чисел.
•	Программа должна содержать функцию с именем generate_random_number.
•	Функция generate_random_number должна генерировать случайное число в диапазоне
от -200 до 0 включительно.
•	Функция generate_random_number должна выводить сгенерированное число на экран.
"""
import random
def generate_random_number():
    number = random.randint(-200, 0)
    print(f"Сгенерированное число: {number}")
generate_random_number()
