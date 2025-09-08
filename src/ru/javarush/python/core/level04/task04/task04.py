"""
Напиши программу, которая делит целое число на целое. Выведи на экран тип результата.
Требования:
•	Программа должна выполнить операцию деления целого числа на целое.
•	Программа должна определить тип результата операции деления.
•	Программа должна вывести тип результата на экран.
"""
while True:
    try:
        x = int(input("Please insert number to be divided: "))
        break
    except ValueError:
        print(" Invalid input. Please enter an integer.")

while True:
    try:
        y = int(input("Please insert number to divide by (non-zero): "))
        if y == 0:
            print(" Division by zero is not allowed. Try again.")
        else:
            break
    except ValueError:
        print(" Invalid input. Please enter an integer.")

z = x / y
print(f" Result is {z}, type: {type(z).__name__}")
