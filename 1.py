massiv = list(map(int, input("Введите элементы массива через пробел: ").split()))

n = len(massiv)
for i in range(n):
    for j in range(n - i - 1):
        if massiv[j] > massiv[j + 1]:
            temp = massiv[j]
            massiv[j] = massiv[j+1]
            massiv[j+1] = temp
result = ' '.join(map(str, massiv))
print(result)
