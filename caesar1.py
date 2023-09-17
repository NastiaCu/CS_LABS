alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar1():
    while True:
        text = input("Enter the text: ").replace(" ", "").upper()

        while True:
            key1 = int(input("Enter key 1 (an integer between 1 and 25): "))
            if 1 <= key1 <= 25:
                break
            else:
                print("Key 1 should be between 1 and 25.")

        operation = int(input("Enter the operation (1 for encryption, 2 for decryption): "))

        result = ""

        for char in text:
            if char.isalpha():
                if operation == 1:
                    shifted_index = (alphabet.index(char) + key1) % 26
                elif operation == 2:
                    shifted_index = (alphabet.index(char) - key1) % 26

                shifted_char = alphabet[shifted_index]
                result += shifted_char
            else:
                result += char

        return result


print(caesar1())
