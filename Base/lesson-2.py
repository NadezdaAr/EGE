# Типы данных

# Целое число / Integer / int
my_int = 5
print(type(my_int))

# Дробное число (вещественное, с плавающей точкой) / Float / float
my_float = 4.7
print(type(my_float))

# Строка / String / str
my_str_1 = "Hello"
my_str_2 ='World'
print(type(my_str_1))

# Примеры сложения переменных
# print(my_str_1 + my_str_2) - две строки ОК
# print(my_int + my_float) - два числа ОК
# print(my_str_1 + my_int) - строка и число, ошибка конкатинации (обьединение строк)
# print(my_int + my_str_1) - число и строка, ошибка сложения

# Список / List / list
my_list = ["Vladimir", 18, 140.5]
print(type(my_list))

# Кортеж / Tuple / tuple
my_tuple = ("Vladimir", 18, 140.5)
print(type(my_tuple))