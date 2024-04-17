class Stos:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(len(self.items) - 1)

if __name__ == '__main__':
    stos_nowy = Stos()
    stos_nowy.push(12)
    stos_nowy.push(23)
    stos_nowy.push(43)
    stos_nowy.push(21)
    stos_nowy.push(13)
    print(stos_nowy.items)
    stos_nowy.pop()
    print(stos_nowy.items)

    stos_stringow = Stos()
    stos_stringow.push(str(4))
    stos_stringow.push(str(6))
    stos_stringow.push(str(7))
    stos_stringow.push(str(8))
    stos_stringow.push(str(9))
    print(stos_stringow.items)
    stos_stringow.pop()
    print(stos_stringow.items)