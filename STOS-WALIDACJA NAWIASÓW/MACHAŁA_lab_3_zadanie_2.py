from stos import Stos
if __name__ == '__main__':
    Stack = Stos()

    Stack.push(12)
    Stack.push(17)
    Stack.push(16)
    Stack.push(14)
    Stack.push(13)
    Stack.push(11)

    print(f"{Stack.items} STOS PO DODANIU")
    print(f"{Stack.size()} ILOŚĆ ELEMENTÓW")
    print(f"{Stack.peek()} OSTATNI ELEMENT  (BEZ USUWANIA)")
    print(f"{Stack.items}")
    print(f"{Stack.pop()} OSTATNI ELEMENT Z USUNIĘCIEM")
    print(f"{Stack.items}")
    Stack.clear()
    print(f"{Stack.items}")
    print(Stack.is_empty())
    Stack.push(12)
    Stack.push(17)
    print(Stack.is_empty())
    Stack.print_stack()




