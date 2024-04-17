from Machała_lab_3_zad_1 import misr_gries

if __name__ == '__main__':
    lista = []
    with open('Dickens', 'r', encoding='utf-8', ) as f:
        for line in f:
            lista += line.strip().split()

    k = int(input("podaj k: "))
    print(misr_gries(lista, k))
