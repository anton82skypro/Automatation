def month_to_season(month):
    season = ["Зима", "Весна", "Лето", "Осень"]
    month = int(month)
    if (month == 1) or (month == 2) or (month == 12):
        print(season[0])
    if (month == 3) or (month == 4) or (month == 5):
        print(season[1])
    if (month == 6) or (month == 7) or (month == 8):
        print(season[2])
    if (month == 9) or (month == 10) or (month == 11):
        print(season[3])
    elif month < 1 or month > 12:
        print("Введите целое число от 1 до 12.")
        
month = input("Введите номер месяца: ")
month_to_season(month)