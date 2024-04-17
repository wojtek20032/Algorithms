from stos import Stos


def nawiasy(tekst):
    Stack = Stos()
    for char in tekst:
        if char == "(":
            Stack.push(char)
        elif char == ")":
            if Stack.is_empty():
                return False
            else:
                Stack.pop()

    if Stack.is_empty() != 0:
        print("CORRECT")
    else:
        print("INCORRECT")
