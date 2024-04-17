from stos import *


def nawiasy_ext(tekst):
    Stack = Stos()
    for char in tekst:
        if char == "(" or char == "{" or char == "[":
            Stack.push(char)
        elif char == ")" or char == "]" or char == "}":
            if Stack.is_empty():
                return False
            else:
                Stack.pop()

    if Stack.is_empty() != 0:
        print("CORRECT")
    else:
        print("INCORRECT")
