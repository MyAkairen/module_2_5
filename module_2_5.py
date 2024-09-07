#то решение, которое нужно
def get_matrix (n, m, value):
    matrix = []
    for i in range(n):
        new_matrix=[]
        matrix.append(new_matrix)
        for j in range(m):
            new_matrix.append(value)
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

#не то решение, которое нужно
import random
def get_matrix (n, m, value):
    matrix = []
    for i in range(n):
        matrix.append(value)
    print(str(matrix) * m)
get_matrix(int(input('Введите кол-во столбцов: ')),
           int(input('Введите кол-во строк: ')),
           random.randrange(0, 10))