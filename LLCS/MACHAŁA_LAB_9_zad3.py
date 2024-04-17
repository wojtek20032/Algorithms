import random
import statistics
import string
import time


def bigger(a, b):
    if a > b:
        return a
    else:
        return b


def create_matrix(narrow, longv):
    matrix = [[0] * (narrow + 1) for _ in range(longv + 1)]
    return matrix


def create_full_matrix_wo_LLCS(A, B):
    m = len(A)
    n = len(B)

    matrix = create_matrix(n, m)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = bigger(matrix[i - 1][j], matrix[i][j - 1])
    return matrix


def LLCS(A, B, visualize=False):
    m = len(A)
    n = len(B)

    matrix = create_matrix(n, m)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = bigger(matrix[i - 1][j], matrix[i][j - 1])

    if visualize == True:
        for row in matrix:
            print(' '.join(f'{num:2d}' for num in row))

    return matrix[m][n]


from string import *


def generate_word(alpha, length, alpha_length):
    word = []
    for i in range(length):
        random_num = random.randint(0, alpha_length - 1)
        word.append(alpha[random_num])

    return word


alphabet1 = ['A', 'C', 'G', 'T']
alphabet2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
alphabet3 = list(string.ascii_letters + string.digits)
alphabets = [alphabet1, alphabet2, alphabet3]
times = []
llcs = []
for alpha in alphabets:
    for i in range(101):
        word1 = generate_word(alpha, 8, len(alpha))
        word2 = generate_word(alpha, 8, len(alpha))
        t1 = time.time_ns()
        llcs.append(LLCS(word1, word2, False))
        t2 = time.time_ns()
        times.append(t2 - t1)

    print(
        f"sredni czas dla {alpha} 8 dlugosc to {statistics.mean(times)}us, mediana to {statistics.median(times)}us, a srednia llcs to {statistics.mean(llcs)}")
    times = []
    llcs = []
    for i in range(101):
        word1 = generate_word(alpha, 32, len(alpha))
        word2 = generate_word(alpha, 32, len(alpha))
        t1 = time.time_ns()
        llcs.append(LLCS(word1, word2, False))
        t2 = time.time_ns()
        times.append(t2 - t1)
    print(
        f"sredni czas dla {alpha} 32 dlugosc to {statistics.mean(times)}us, mediana to {statistics.median(times)}us, a srednia llcs to {statistics.mean(llcs)}")
    times = []
    llcs = []
    for i in range(101):
        word1 = generate_word(alpha, 128, len(alpha))
        word2 = generate_word(alpha, 128, len(alpha))
        t1 = time.time_ns()
        llcs.append(LLCS(word1, word2, False))
        t2 = time.time_ns()
        times.append(t2 - t1)
    print(
        f"sredni czas dla {alpha} 128 dlugosc to {statistics.mean(times)}us, mediana to {statistics.median(times)}us, a srednia llcs to {statistics.mean(llcs)}")
    times = []
    llcs = []
    for i in range(101):
        word1 = generate_word(alpha, 512, len(alpha))
        word2 = generate_word(alpha, 512, len(alpha))
        t1 = time.time_ns()
        llcs.append(LLCS(word1, word2, False))
        t2 = time.time_ns()
        times.append(t2 - t1)
    print(
        f"sredni czas dla {alpha} 512 dlugosc to {statistics.mean(times)}us, mediana to {statistics.median(times)}us, a srednia llcs to {statistics.mean(llcs)}")
