number = float(input("Введите число: ")) # Запрашиваем ввод числа с клавиатуры. Преобразуем введенное число в число с плавающей запятой.
ans = "Положительное" if number > 0 else "Отрицательное" if number < 0 else "Ноль" # Используем тернарное выражение для проверки числа.
print(ans) # Выводим полученный ответ в консоль.