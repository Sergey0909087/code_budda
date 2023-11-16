number = input("Введите число: ")

if number == number[::-1]:
    print("Число", number, "является палиндромом")
else:
    print("Число", number, "не является палиндромом")
