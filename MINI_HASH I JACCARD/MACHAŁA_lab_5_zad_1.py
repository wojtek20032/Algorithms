import os
import time
import matplotlib.pyplot as plt

M = 200
K = 20
mixers = [int.from_bytes(os.urandom(8), byteorder="little") for i in range(M)]


def minHashAlgorithm(filename, M, K):
    testfile = open(filename, "r", encoding="utf8").read()
    hashtable = [[] for i in range(M)]
    for j in range(0, len(testfile) - K + 1):
        h = hash(testfile[j: j + K])
        for i in range(M):
            hashtable[i].append(h ^ mixers[i])
    return [min(row) for row in hashtable]


def Jaccard_prob(set1, set2):
    num_hashes = len(set1)
    num_matching_hashes = 0
    for val1, val2 in zip(set1, set2):
        num_matching_hashes += val1 == val2
    prob = (num_matching_hashes / num_hashes)
    return prob


if __name__ == '__main__':
    podo1 = Jaccard_prob(minHashAlgorithm("Sienkiewicz_2.txt", M, K), minHashAlgorithm("Sienkiewicz_1.txt", M, K))
    print(f"Podobienstwo: {podo1}")
    podo2 = Jaccard_prob(minHashAlgorithm("Prus_1.txt", M, K), (minHashAlgorithm("Sienkiewicz_1.txt", M, K)))
    print(f"Podobienstwo drugie: {podo2}")

    start = time.time()
    Jaccard_prob(minHashAlgorithm("Sienkiewicz_2.txt", M, K), minHashAlgorithm("Sienkiewicz_1.txt", M, K))
    koniec = time.time()

    ile = abs(start - koniec)
    print(f"czas dzialania {ile}")
    q = [10, 20, 40]
    M = [100, 200]
    times = []
    for i in q:
        t1 = time.time()
        Jaccard_prob(minHashAlgorithm("Sienkiewicz_2.txt", 100, i), minHashAlgorithm("Sienkiewicz_1.txt", 100, i))
        t2 = time.time()
        times.append(t2 - t1)
        t3 = time.time()
        Jaccard_prob(minHashAlgorithm("Sienkiewicz_2.txt", 200, i), minHashAlgorithm("Sienkiewicz_1.txt", 200, i))
        t4 = time.time()
        times.append(t4 - t3)
    plt.plot(times, color="green", marker="+")
    plt.show()
