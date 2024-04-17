import heapq
import random
import time

from MACHALA_lab_6_ROBOT import print_tree

tablica = [1, 10, -2, 7, 14]
heapq.heapify(tablica)
print_tree(tablica)
print(tablica)

### ZAD 2
print("ZADANIE 2\n")
heapq.heappop(tablica)
print_tree(tablica)
tablica.append(15)
print_tree(tablica)
tablica.append(2)
print_tree(tablica)
heapq.heapify(tablica)
print_tree(tablica)

from MACHALA_lab_6_ROBOT import lista

lista2 = []
for i in lista:
    heapq.heappush(lista2, i)
    print_tree(lista2)
    print("PRZEJSCIE_______")

for i in range(len(lista2)):
    lista2[i] *= -1

heapq.heapify(lista2)
for i in range(len(lista2)):
    lista2[i] *= -1
print_tree(lista2)
print("\nZADANIE 5")
tab1 = []
tab2 = []
tab3 = []
sum = 0

print("\nDLA 100\n")
for i in range(5):
    for j in range(100):
        tab1.append(random.randint(-1000, 1000))
    t1 = time.time()
    heapq.heapify(tab1)
    t2 = time.time()
    tab1.clear()
    sum += (t2 - t1)
print(f"ZA POMOCA HEAPIFY {sum / 5}")
sum = 0
for i in range(5):
    t3 = time.time()
    for j in range(100):
        liczba = random.randint(-1000, 1000)
        heapq.heappush(tab1, liczba)
    t4 = time.time()
    sum += (t4 - t3)
print(f"ZA POMOCA HEAPPUSH {sum / 5}")
sum = 0
##############################################################
print("\nDLA 1000\n")
for i in range(5):
    for j in range(1000):
        tab1.append(random.randint(-1000, 1000))
    t1 = time.time()
    heapq.heapify(tab1)
    t2 = time.time()
    tab1.clear()
    sum += (t2 - t1)
print(f"ZA POMOCA HEAPIFY {sum / 5}")
sum = 0
for i in range(5):
    t3 = time.time()
    for j in range(1000):
        liczba = random.randint(-1000, 1000)
        heapq.heappush(tab1, liczba)
    t4 = time.time()
    sum += (t4 - t3)
print(f"ZA POMOCA HEAPPUSH {sum / 5}")
sum = 0
#####################################################
print("\nDLA 1000000\n")
for i in range(5):
    for j in range(1000000):
        tab1.append(random.randint(-1000, 1000))
    t1 = time.time()
    heapq.heapify(tab1)
    t2 = time.time()
    tab1.clear()
    sum += (t2 - t1)
print(f"ZA POMOCA HEAPIFY {sum / 5}")
sum = 0
for i in range(5):
    t3 = time.time()
    for j in range(1000000):
        liczba = random.randint(-1000, 1000)
        heapq.heappush(tab1, liczba)
    t4 = time.time()
    sum += (t4 - t3)

print(f"ZA POMOCA HEAPPUSH {sum / 5}")
suma = heapq.heappop(tab1) + heapq.heappop(tab1)
print(suma)
heapq.heappush(tab1, suma)
