import random
import time
import os

def print_matrix(M):
    for i in M:
        for j in i:
            print("%3d" % j, end=' ')
        print()
    print()

def submatrix(M):
    for i in range(size):
        M.append([0] * size)

try:
    K = int(input("Введите число К="))
    row_q = int(input("Введите чётное количество строк (столбцов) квадратной матрицы >5:"))
    while row_q < 5 or row_q % 2 != 0:
        row_q = int(input("Введите чётное!!! количество строк (столбцов) квадратной матрицы >5!!!:"))

    start = time.time()
    print("\n-----Результат работы программы-----\n -----Локальное время", time.ctime(), "-----")

    A, F, AF, AT, S = [], [], [], [], []  # Задаем матрицы
    for i in range(row_q):
        A.append([0] * row_q)
        F.append([0] * row_q)
        AF.append([0] * row_q)
        AT.append([0] * row_q)
        S.append([0] * row_q)

    for i in range(row_q):
        for j in range(row_q):
            A[i][j] = random.randint(-10, 10)

    print("A")
    print_matrix(A)

    for i in range(row_q):
        for j in range(row_q):
            F[i][j] = A[i][j]

    size = row_q // 2
    E = []
    submatrix(E)
    for i in range(size):
        for j in range(size):
            E[i][j] = F[i][j]

    n4 = 0
    for i in range(size):
        for j in range(size // 2):
            if E[i][j] == 0 and i % 2 == 1 and i > j and i + j < size - 1:
                n4 += 1

    n1 = 0
    for i in range(size // 2):
        for j in range(size):
            if E[i][j] < 0 and j % 2 == 0 and i > j and i + j < size - 1:
                n1 += 1

    if n4 > n1:
        B = []
        submatrix(B)
        for i in range(size):
            for j in range(size):
                if (i == 0) and (j < size - 1 - i) and (j > 0):
                    B[i][j], B[j][size - 1] = B[j][size - 1], B[i][j]
                if (i < j) and (j < size - 1 - i) and (i > 0):
                    B[i][j], B[j][size - 1 - i] = B[j][size - 1 - i], B[i][j]
        print_matrix(B)
        for i in range(size):
            for j in range(size):
                F[i][j] = B[i][j]
    else:
        for j in range(row_q // 2):
            for i in range(row_q // 2):
                F[i][j], F[row_q // 2 + row_q % 2 + i][row_q // 2 + row_q % 2 + j] \
                    = F[row_q // 2 + row_q % 2 + i][row_q // 2 + row_q % 2 + j], F[i][j]
    print("F")
    print_matrix(F)

    for i in range(row_q):  # F + A
        for j in range(row_q):
            S[i][j] = F[i][j] + A[i][j]
    print("F + A")
    print_matrix(S)

    for i in range(row_q):  # K * F
        for j in range(row_q):
            F[i][j] = K * F[i][j]
    print("K * F")
    print_matrix(F)

    for i in range(row_q):  # (F + A) – (K * F)
        for j in range(row_q):
            F[i][j] = S[i][j] - F[i][j]
    print("(F + A) – (K * F)")
    print_matrix(F)

    for i in range(row_q):  # AT
        for j in range(row_q):
            AT[i][j] = A[j][i]
    print("AT")
    print_matrix(AT)

    for i in range(row_q):  # ((F + A) – (K * F)) * AT
        for j in range(row_q):
            AF[i][j] = F[i][j] * AT[i][j]
    print("((F + A) – (K * F)) * AT")
    print_matrix(AF)

    finish = time.time()
    result = finish - start
    print("\nProgram time: " + str(result) + " seconds.")
    print("Program size: " + str(os.path.getsize('laba4.py')) + " bytes.")

except ValueError:
    print("\nВведенн(ый/ые) символ(/ы) не явля(ется/ются) числом")

except FileNotFoundError:
    print("\nФайл для определения размера не найден")