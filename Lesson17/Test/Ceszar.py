
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            shifted = (ord(char) - shift_amount + shift) % 26 + shift_amount
            result += chr(shifted)
        else:
            result += char
    return result

text = "Hello, World!"
shift = 3
encrypted_text = caesar_cipher(text, shift)
print("Зашифрованный текст:", encrypted_text)