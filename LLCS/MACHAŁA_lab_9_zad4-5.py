import time
import tokenize
import difflib


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


def token_file(filename):
    with open(filename, 'rb') as file:
        tokens = []
        for token in tokenize.tokenize(file.readline):
            if token.type == tokenize.NAME or token.type == tokenize.OP:
                tokens.append(token.string)
        return tokens


A_tokens = token_file('A.py')
B_tokens = token_file('B.py')
C_tokens = token_file('C.py')


def LLCS_compact(tokens1, tokens2):
    same_tokens1 = []
    for token in tokens1:
        if token in tokens2:
            same_tokens1.append(token)

    same_tokens2 = []
    for token in tokens2:
        if token in tokens1:
            same_tokens2.append(token)

    print("Długości list na poczatku:")
    print(f"lista1: {len(tokens1)}, lista2: {len(tokens2)}")

    print("Nowa długość list po usuniecie:")
    print(len(same_tokens1), len(same_tokens2))

    redukowane1 = (1 - len(same_tokens1) / len(tokens1)) * 100
    redukowane2 = (1 - len(same_tokens2) / len(tokens2)) * 100

    print(f"Ile procent sie zmniejszyly listy: \nLISTA1:{redukowane1:.2f}%, \nLISTA2:{redukowane2:.2f}%")

    llcs_filtered = LLCS(same_tokens1, same_tokens2, False)
    min_length = min(len(same_tokens1), len(same_tokens2))
    similarity = llcs_filtered / min_length

    return similarity


similarity_AB = LLCS_compact(A_tokens, B_tokens)
similarity_BC = LLCS_compact(B_tokens, C_tokens)
similarity_AC = LLCS_compact(A_tokens, C_tokens)
print("Podobieństwo (A, B):", similarity_AB)
print("Podobieństwo (B, C):", similarity_BC)
print("Podobieństwo (A, C):", similarity_AC)
