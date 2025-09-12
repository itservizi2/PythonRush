"""
Напишите программу, которая запрашивает у пользователя два вещественных числа и
сравнивает их с использованием допустимой погрешности epsilon. Выведите результат
сравнения на экран.
Требования:
•	Запрос ввода первого числа
•	Запрос ввода второго числа
•	Сравнение чисел с использованием допустимой погрешности epsilon
•	Вывод результата сравнения на экран
"""
import math
epsilon = 0.00001
try:
    number1 = float(input("number1: "))
    number2 = float(input("number2: "))
    if abs(number1 - number2) < epsilon:
        print("number1 is equal to number2")
    else:
        print("number1 is not equal to number2")
except ValueError:
    print("number is not float")

