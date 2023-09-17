def caesar2():
    while True:
        text = input("Enter the text: ").replace(" ", "").upper()

        while True:
            key1 = int(input("Enter key 1 (an integer between 1 and 25): "))
            if 1 <= key1 <= 25:
                break
            else:
                print("Key 1 should be between 1 and 25.")

        operation = int(input("Enter the operation (1 for encryption, 2 for decryption): "))
            

        while True:
            key2 = input("Enter key 2 (a permutation of the alphabet with at least 7 characters): ")
            if not key2.isalpha() or len(key2) < 7:
                print("Enter another key.")
            else:
                key2 = key2.upper()
                new_alphabet = permutation(key2)

                if len(new_alphabet) != 26:
                    print("Key 2 should be a permutation of the alphabet with exactly 26 unique characters.")
                else:
                    break

        result = ""

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
    key2 = key2.upper()
    
    if not key2.isalpha() or len(key2) < 7:
        return ""

    modified_alphabet = ""
    seen = ""

    for char in key2:
        if char.isalpha() and char not in seen:
            modified_alphabet += char
            seen += char

    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if char not in seen:
            modified_alphabet += char

    print(modified_alphabet)

    return modified_alphabet



print(caesar2())
