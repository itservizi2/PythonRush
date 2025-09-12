"""
Напишите программу, которая запрашивает у пользователя вещественное число и
округляет его вниз (с использованием math.floor()), вверх (с использованием math.ceil())
 и до ближайшего целого числа (с использованием round()). Выведите результаты всех трех
 округлений.
Требования:
•	Программа должна включать переменную number, которой присваивается введенное
пользователем вещественное число.
•	Программа должна использовать функцию math.floor() для округления числа вниз.
•	Программа должна использовать функцию math.ceil() для округления числа вверх.
•	Программа должна использовать функцию round() для округления числа до ближайшего целого числа.
•	Программа должна выводить результаты всех трех методов округления
(вниз, вверх и до ближайшего целого числа).
"""
import math
try:
    number = float(input("insert a float number: "))
    rounded_down = math.floor(number)
    rounded_up = math.ceil(number)
    rounded_nearest = round(number)

    print("rounded_down", rounded_down)
    print("rounded_up", rounded_up)
    print("rounded_nearest", rounded_nearest)
except ValueError:
    print("number is not float")
