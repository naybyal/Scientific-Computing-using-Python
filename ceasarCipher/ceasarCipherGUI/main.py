global distance


def ceasarEncrypt(message):
    encryptedMessage = ""
    for ch in message:
        ordinalValue = ord(ch)
        cipherValue = ordinalValue + distance
        if cipherValue > ord('z'):
            cipherValue = ord('a') + distance - (ord('z') - ordinalValue + 1)

        encryptedMessage += chr(cipherValue)
    return encryptedMessage


def ceasarDecrypt(encryptedMessage):
    message = ""
    for ch in encryptedMessage:
        cipherValue = ord(ch)
        originalValue = cipherValue - distance
        if originalValue < ord('a'):
            originalValue = ord('z') - distance + (ord('z') - cipherValue + 1)
        message += chr(originalValue)
    return message

