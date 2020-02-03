def decal(letter, dec):
    res = ord(letter) + dec
    if res > 122:
        res -= 26
    if res < 97:
        res += 26
    return chr(res)

def cryptage_cesar(message, dec):
    return ''.join([decal(letter, dec) for letter in message])

def decrpytage_cesar(message, dec):
    return ''.join([decal(letter, -dec) for letter in message])


def cryptage_vigenere(message, clef):
    s = ''
    for i, letter in enumerate(message):
        s += decal(letter, ord(clef[i % len(clef)]) - 97)
    return s

# Ou en une ligne
def cryptage_vigenere(message, clef):
    return ''.join([decal(letter, ord(clef[i % len(clef)]) - 97) for i, letter in enumerate(message)])
