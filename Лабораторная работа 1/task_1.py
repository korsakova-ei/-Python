numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# Находим индекс пропущенного элемента
index = numbers.index(None)

# Создаем новый список без пропущенного элемента
new_numbers = [num for num in numbers if num is not None]

# Вычисляем среднее арифметическое
sr_arifm = sum(new_numbers) / len(numbers)

# Заменяем пропущенный элемент средним арифметическим
numbers[index] = sr_arifm
# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
