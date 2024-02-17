def encrypt_decrypt(text, shift_keys, ifdecrypt):
    """
    Encrypts a text using Caesar Cipher with a list of shift keys.
    Args:
        text: The text to encrypt.
        shift_keys: A list of integers representing the shift values for each character.
        ifdecrypt: flag if decrypt or encrypt
    Returns:
        A string containing the encrypted text if encrypt and plain text if decrypt
    """
    
    result = []
    key = []
    letters = list(text)
    shiftkeys = shift_keys.split()
    
    for i in range(len(text)):
        key += (shiftkeys[i % len(shiftkeys)]).split()
    
    for i in range(len(text)):
        if ifdecrypt: result += chr((ord(letters[i]) - int(key[i]) - 32) % 94 + 32) 
        else: result += chr((ord(letters[i]) + int(key[i]) - 32 + 94) % 94 + 32)
        print(i, letters[i], key[i], result[i])
    print("----------")
    
    for i in range(len(text)):
        print(i, result[i], key[i], letters[i])
        outcome = "".join(result)
    print("----------")
    
    return outcome

# Example usage
text = input()
shift_keys = input()

x = encrypt_decrypt(text, shift_keys, ifdecrypt = False)

print("Text:", text)
print("Shift keys:", shift_keys)
print("Cipher:", x)
print("Decrypted text:", text)