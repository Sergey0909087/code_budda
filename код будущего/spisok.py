a = [1, 2, 3, 4, 5, 6]

i = 0
while i < len(a):
    if a[i] % 2 != 0:
        del a[i]
    else:
        a[i] = a[i] // 2
        i += 1

print(a)
