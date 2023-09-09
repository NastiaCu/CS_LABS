def caeser2(text, key1, key2, operation):
    
    if key1 < 1 or key1 > 25:
        return "Choose from 1 to 25"
    
    text = text.replace(" ", "").upper()

    result = ""

    new_alphabet = permutation(key2)
    if len(new_alphabet) != 26:
        return "Choose another key"

    for char in text:
        if char.isalpha():
            if operation == 1:
                shifted_index = (new_alphabet.index(char) + key1) % 26
            elif operation == 2:
                shifted_index = (new_alphabet.index(char) - key1) % 26
            
            shifted_char = new_alphabet[shifted_index]
            result += shifted_char
        else:
            result += char
    
    return result


def permutation(key2):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if key2.isalpha() == False or len(key2) < 7:
        return ""
    
    key2 = key2.upper()
    
    remaining_letters = ""

    for letter in alphabet:
        if letter not in key2:
            remaining_letters += letter

    modified_alphabed = key2 + remaining_letters

    seen = ""
    res = ""
    for char in modified_alphabed:
        if char not in seen:
            res += char
            seen += char

    return res

print(caeser2("BRUTE FORCE ATTACK", 17, "cryptography", 1))