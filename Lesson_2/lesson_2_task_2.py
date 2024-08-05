def is_year_leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0): # Проверка на високосность.
        return True                                            # если да, то год високосный
    else:
        return False                                           # если нет, то год не високосный

year = int(input("Введите год: "))                             # предлагаем ввести год для проверки 
result = is_year_leap(year)                                    # сохраняем результат выполнения функции в переменной 
print(f"Год {year} високосный: {result}")                      # распечатываем результат
