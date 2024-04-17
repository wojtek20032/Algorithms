from Machała_lab_3_zad_1 import misr_gries
from pympler import asizeof


def brute_force(stream,k):
    counts = {}
    for item in stream:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    counts1 = {j: z for j, z in sorted(counts.items(), key=lambda b: b[1], reverse=True)}
    n = len(counts1.keys())
    for i in counts1:
        if i < n/k:
            del i
    return counts1


if __name__ == '__main__':
    k = 2
    lista = [1, 4, 5, 4, 4, 5, 4, 4]
    print(asizeof.asizeof(misr_gries(lista,k)))
    print(asizeof.asizeof(brute_force(lista,k)))
