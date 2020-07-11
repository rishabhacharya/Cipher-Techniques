
#-------------------------------------------------------------------------------
# Name:        Caesar Cipher
#
# Author:      Rishabh Acharya
#
# Created:     10-07-2020
#
# Project:     Caesar Cipher
#-------------------------------------------------------------------------------

def main():
    print()

    plaintext = input('Enter your Plain text : ')
    key = int(input('Enter key: '))
    print()

    ciphertext = caesarEncryption(plaintext, key)

    plaintext = caesarDecryption(ciphertext, key)

    print()
    print("Encrypted ciphertext is : ", ciphertext)

    return

def caesarDecryption(ciphertext, key):
    plaintext = ''

def caesarEncryption(plaintext, key):
    ciphertext = ''

    for letter in plaintext:
        ascii = ord(letter)
        if letter.isalpha():
            temp = ascii + key
            if (temp > 90 and letter.isupper()) or (temp > 122 and letter.islower()):
                ciphertext += chr(temp - 26)
            else:
                ciphertext += chr(temp)

    return ciphertext

if __name__ == "__main__":
    main()