alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZȘȚ'
alphabet_length = len(alphabet)

def prepare_text(text):
    text = text.replace(" ", "").upper()
    return text

def display_range():
    print("Allowed characters are:", alphabet)

def vigenere(text, key, mode):
    prepared_text = prepare_text(text)
    prepared_key = prepare_text(key)
    result = ""

    for i in range(len(prepared_text)):
        char_text = prepared_text[i]
        char_key = prepared_key[i % len(prepared_key)]

        if char_text in alphabet:
            if mode == "encryption":
                index = (alphabet.index(char_text) + alphabet.index(char_key)) % alphabet_length
            elif mode == "decryption":
                index = (alphabet.index(char_text) - alphabet.index(char_key)) % alphabet_length

            result += alphabet[index]
        else:
            result += char_text

    return result

def main():
    while True:
        print("1. Encryption")
        print("2. Decryption")
        print("0. Exit")
        option = input("Select the desired operation: ")

        if option == "1":
            message = input("Enter the message: ")
            key = input("Enter the key (minimum length 7): ")
            if len(key) < 7:
                print("The key length must be at least 7 characters!")
                continue
            ciphertext = vigenere(message, key, "encryption")
            print("Ciphertext: ", ciphertext)

        elif option == "2":
            ciphertext = input("Enter the ciphertext: ")
            key = input("Enter the key (minimum length 7): ")
            if len(key) < 7:
                print("The key length must be at least 7 characters!")
                continue
            decrypted_message = vigenere(ciphertext, key, "decryption")
            print("Decrypted message: ", decrypted_message)

        elif option == "0":
            break

        else:
            print("Invalid option! Please select a valid option.")

if __name__ == "__main__":
    main()
