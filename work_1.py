# Задание 1.
#
# Поработайте с переменными, создайте несколько,
# выведите на экран, запросите у пользователя несколько чисел и
# строк и сохраните в переменные, выведите на экран.
#
# Пример:
# Ведите ваше имя: Василий
# Ведите ваш пароль: vas
# Введите ваш возраст: 45
# Ваши данные для входа в аккаунт: имя - Василий, пароль - vas, возраст - 45

a = 5
b = 9
print(a, b)


s = str(input("Введите первую строку: "))
n = int(input("Введите первое число: "))
s2 = str(input("Введите вторую строку: "))
n2 = int(input("Введите второе число: "))
print("Введенные значения: ", s, n, s2, n2)


a = input("Введите ваше имя: ")
b = int(input("Введите ваш возраст: "))
c = str(input("Введите ваш пароль: "))
print("Ваши данные для входа в аккаунт: ", a, b, c)
