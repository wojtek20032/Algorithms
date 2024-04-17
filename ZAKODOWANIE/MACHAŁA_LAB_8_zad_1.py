import math


def entropy_count(text):
    count_of_chars = {}
    all_chars = 0
    for char in text:
        if char in count_of_chars:
            count_of_chars[char] += 1
        else:
            count_of_chars[char] = 1
        all_chars += 1
    entropy = 0
    for count in count_of_chars.values():
        probability = count / all_chars
        entropy -= probability * math.log2(probability)

    return entropy


text = "Ala ma kota, a to lis!"
wynik = entropy_count(text)
print(wynik)


def dict_maker(text, symbol_count):
    for symbol in text:
        if symbol in symbol_count:
            symbol_count[symbol] += 1
        else:
            symbol_count[symbol] = 1


def elias_gamma_encode(text):
    symbol_count = {}
    dict_maker(text, symbol_count)
    symbol_mapping = {}
    sorted_symbols = sorted(symbol_count.keys())
    for i, symbol in enumerate(sorted_symbols):
        binary_code = bin(i + 1)[2:]
        symbol_mapping[symbol] = '0' * (len(binary_code) - 1) + binary_code
    encoded_text = []
    for symbol in text:
        encoded_text.append(symbol_mapping[symbol])

    return encoded_text, symbol_mapping


text = "Ala ma kota, a to lis!"

encoded_text, symbol_mapping = elias_gamma_encode(text)
print(symbol_mapping)
print("SYMBOLE ZMAPOWANE!!:")
for symbol, code in symbol_mapping.items():
    print(f"{symbol}-->> {code}")

print("____Encoded____")
print(" ".join(encoded_text))



