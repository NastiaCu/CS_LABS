def caeser1(text, key, operation):
    if key < 1 or key > 25:
        print("Choose from 1 to 25")
        return ""
    
    text = text.replace(" ", "").upper()
    result = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for char in text:
        if char.isalpha():
            if operation == 1:
                shifted_index = (alphabet.index(char) + key) % 26
            elif operation == 2:
                shifted_index = (alphabet.index(char) - key) % 26
            
            shifted_char = alphabet[shifted_index]
            result += shifted_char
        else:
            result += char
    
    return result


print(caeser1("FLIUXOFHCDU", 3, 1))