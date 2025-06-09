s1 = set(map(int, input("Введите первое множество через пробел: ").split()))
s2 = set(map(int, input("Введите второе множество через пробел: ").split()))

operation = input("Выберите операцию (1 - объединение, 2 - пересечение, 3 - разность): ")
if operation == "1":
    result = s1 | s2
elif operation == "2":
    result = s1 & s2
elif operation == "3":
    result = s1 - s2
else:
    result = "Произошла ошибка"

print(result)
