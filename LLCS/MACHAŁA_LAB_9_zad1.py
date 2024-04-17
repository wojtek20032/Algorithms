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


def show_matches(A, B, matrix):
    i = len(A)
    j = len(B)
    matching_sent = []

    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            matching_sent.append(A[i - 1])
            i -= 1
            j -= 1
        elif matrix[i - 1][j] > matrix[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(matching_sent[::-1])


print(LLCS("kaloryfer", "aktorzy", True))
print(show_matches("kaloryfer", "aktorzy", create_full_matrix_wo_LLCS("kaloryfer", "aktorzy")))
