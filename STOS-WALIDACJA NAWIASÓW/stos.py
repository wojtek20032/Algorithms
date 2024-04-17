class Stos:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(len(self.items) - 1)

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def clear(self):
        i = len(self.items) - 1
        while True:
            self.items.pop()
            i -= 1
            if i < 0:
                return

    def is_empty(self):
        return self.size() == 0

    def print_stack(self):
        i = len(self.items) - 1
        while True:
            print(self.items[i])
            i -= 1
            if i < 0:
                return
