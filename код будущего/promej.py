a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

total = 0
count = 0

for i in range(a, b+1):
    if i % 3 == 0:
        total += i
        count += 1

if count == 0:
    print("Нет чисел от", a, "до", b, "включительно, которые делятся на 3")
else:
    average = total / count
    print("Среднее значение всех чисел от", a, "до", b, "включительно, которые делятся на 3, равно", average)
