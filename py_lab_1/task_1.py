numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
id_null = None
avg = 0
count = 0
s = 0
for i in range(0, len(numbers)):
    if numbers[i] is None:
        id_null = i
    else:
        s += numbers[i]

numbers[id_null] = s / len(numbers)

print("Измененный список:", numbers)
