"""
Получение подсписков
7 уровень, 3 лекция

Напишите программу, которая создает список из 10 элементов.
Программа просит пользователя ввести строку, а потом проверяет - есть она в списке или нет.
Требования:
•	Программа должна создать список, содержащий 10 элементов.
•	Программа должна запросить у пользователя ввод строки.
•	Программа должна проверить, содержится ли введенная пользователем строка в списке.
•	Программа должна вывести результат проверки: находится введенная строка в списке или нет.
"""
my_list = []
for i in range(10):
    user_input = input("insert the string: ")
    my_list.append(user_input)
print(my_list)
string_to_check = input("insert the string to be checked: ")
if string_to_check in my_list:
    print("yes, string is present in list")
else:
    print("no, string is not present in list")



