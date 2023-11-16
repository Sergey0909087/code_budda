month_number = int(input("Введите порядковый номер месяца (от 1 до 12): "))

if month_number in (3, 4, 5):
    season = "весна"
elif month_number in (6, 7, 8):
    season = "лето"
elif month_number in (9, 10, 11):
    season = "осень"
else:
    season = "зима"

print("Месяц номер", month_number, "относится к сезону", season)
