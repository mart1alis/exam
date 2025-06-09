def input_matrix():
    matrix = []
    flag = 0
    while flag != 1:
        h = int(input("Введите количество строк: "))
        w = int(input("Введите количество столбцов: "))
        if h > 10 or w > 10:
            print ("Размер матрицы не должен превышать 10х10")
        else:
            flag = 1
    print("Введите элементы матрицы построчно, разделяя элементы пробелами: ")
    for n in range(h):
        h = list(map(float, input().split()))
        if len(h) != w:
            print("Неверное количество элементов в строке")
            exit()
        else:
            matrix.append(h)
    return matrix
matrix1 = input_matrix()
print("Полученная матрица 1: ")
for h in matrix1:
    print(h)
matrix2 = input_matrix()
print("Полученная матрица 2: ")
for h in matrix2:
    print(h)
    
def transpose_matrix(matrix):
    transposed = []
    for i in range(len(matrix[0])):
        new_h = []
        for j in range(len(matrix)):
            new_h.append(matrix[j][i])
        transposed.append(new_h)
    return transposed

def sum(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Матрицы должны быть одного размера для сложения")
        return None    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def multiply(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Число столбцов первой матрицы должно равняться числу строк второй")
        return None
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = 0
            for k in range(len(matrix2)):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        result.append(row)
    return result

operation = input("Введите тип операции (1 - транспонирование, 2 - сложение, 3 - умножение): ")

if operation == "1":
    print("Транспонированная матрица 1:")
    for h in transpose_matrix(matrix1):
        print(h)
    print("Транспонированная матрица 2:")
    for h in transpose_matrix(matrix2):
        print(h)
elif operation == "2":
    sum_matrix = sum(matrix1, matrix2)
    if sum_matrix:
        print("Результат сложения матриц:")
        for row in sum_matrix:
            print(row)           
elif operation == "3":
    matrix = multiply(matrix1, matrix2)
    if matrix:
        print("Результат умножения матриц:")
        for row in matrix:
            print(row)
else:
    print("Неверный код операции")
