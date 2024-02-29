global distance

def caesarEncrypt(message):
    encryptedMessage = ""
    for ch in message:
        ordinalValue = ord(ch)
        cipherValue = ordinalValue + distance
        if cipherValue > ord('z'):
            cipherValue = ord('a') + distance - (ord('z') - ordinalValue + 1)

        encryptedMessage += chr(cipherValue)
    return encryptedMessage


def caesarDecrypt(encryptedMessage):
    message = ""
    for ch in encryptedMessage:
        cipherValue = ord(ch)
        originalValue = cipherValue - distance
        if originalValue < ord('a'):
            originalValue = ord('z') - distance + (ord('z') - cipherValue + 1)
        message += chr(originalValue)
    return message


message = input('Reading the message : ')
distance = int(input("Reading the distance (k) : "))

encrypted = ceasarEncrypt(message)
print(encrypted)

decrypted = ceasarDecrypt(encrypted)
print(decrypted)
