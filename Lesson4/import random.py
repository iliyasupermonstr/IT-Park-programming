class EnigmaMachine:
    def __init__(self, rotor1, rotor2, rotor3, reflector):
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3
        self.reflector = reflector

    def encrypt(self, message):
        encrypted_message = ""
        for char in message:
            if char.isalpha():
                char = char.upper()
                encrypted_char = self.rotor3.forward(self.rotor2.forward(self.rotor1.forward(char)))
                encrypted_char = self.reflector.reflect(encrypted_char)
                encrypted_char = self.rotor1.backward(self.rotor2.backward(self.rotor3.backward(encrypted_char)))
                encrypted_message += encrypted_char
                self.rotor1.rotate()
                if self.rotor1.position == self.rotor1.notch:
                    self.rotor2.rotate()
                    if self.rotor2.position == self.rotor2.notch:
                        self.rotor3.rotate()
            else:
                encrypted_message += char
        return encrypted_message

class Rotor:
    def __init__(self, wiring, notch):
        self.wiring = wiring
        self.notch = notch
        self.position = 'A'

    def forward(self, char):
        offset = ord(char) - ord('A')
        return self.wiring[(offset + ord(self.position) - ord('A')) % 26]

    def backward(self, char):
        offset = ord(char) - ord('A')
        return chr(((self.wiring.index(char) - ord('A')) - (ord(self.position) - ord('A'))) % 26 + ord('A'))

    def rotate(self):
        self.position = chr((ord(self.position) - ord('A') + 1) % 26 + ord('A'))
        if self.position == self.notch:
            return True
        return False

class Reflector:
    def __init__(self, wiring):
        self.wiring = wiring

    def reflect(self, char):
        return self.wiring[self.wiring.index(char)]

# Пример настройки машины Энигма
rotor1_wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor2_wiring = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor3_wiring = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
reflector_wiring = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

rotor1 = Rotor(list(rotor1_wiring), 'R')
rotor2 = Rotor(list(rotor2_wiring), 'F')
rotor3 = Rotor(list(rotor3_wiring), 'W')
reflector = Reflector(list(reflector_wiring))

enigma = EnigmaMachine(rotor1, rotor2, rotor3, reflector)

# Введите сообщение для шифрования
message = input("Введите сообщение для шифрования: ")
encrypted_message = enigma.encrypt(message)
print("Зашифрованное сообщение:", encrypted_message)