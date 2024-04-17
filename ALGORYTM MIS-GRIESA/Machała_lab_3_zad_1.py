import random


def misr_gries(lista, k):
    dictionary = {}
    n = len(dictionary.keys())
    for i in lista:
        if i in dictionary:
            dictionary[i] += 1
        elif len(dictionary.keys()) < k:
            dictionary[i] = 1
        else:
            for j in list(dictionary.keys()):
                dictionary[j] -= 1
                if dictionary[j] == 0:
                    del dictionary[j]

    dictionary2 = {}
    for i in lista:
        if i in dictionary:
            if i in dictionary2:
                dictionary2[i] += 1
            else:
                dictionary2[i] = 1

    for i in dictionary2:
        if i < len(dictionary2) / k:
            del i

    sorted1 = {j: z for j, z in sorted(dictionary.items(), key=lambda b: b[1], reverse=True)}
    return sorted1


if __name__ == '__main__':
    k = int(input("Podaj parametr k"))
    lista = [1, 4, 5, 4, 4, 5, 4, 4]
    print(misr_gries(lista, k))
    lista2 = [1, 1, 1, 1, 2, 31]
if __name__ == '__main__':
    k2 = 1
    lista2 = [1, 1, 1, 1, 1, 1, 31, 4, 3]
    print(misr_gries(lista2, k2))
