def xor_encrypt(plaintext, key):
    """Encrypts plaintext using XOR cipher with the given key, printing bits involved."""
    ciphertext = bytearray()
    for i in range(len(plaintext)):
        plaintext_byte = plaintext[i]
        key_byte = key[i % len(key)]
    
        print(f"Plaintext byte: {format(plaintext_byte, '08b')} = {chr(plaintext_byte)}")
        print(f"Key byte:       {format(key_byte, '08b')} = {chr(key_byte)}")
        
        xor_result = plaintext_byte ^ key_byte
        print(f"XOR result:     {format(xor_result, '08b')} = {chr(xor_result)}")
        print("--------------------")
        ciphertext.append(xor_result)
        
        
    return ciphertext
    
    encrypted = xor_encrypt(plaintext, key)
    print("Ciphertext: ", encrypted.decode())

def xor_decrypt(ciphertext, key):
    """Decrypts ciphertext using XOR cipher with the given key."""
    return xor_encrypt(ciphertext, key)  # XOR decryption is the same as encryption
    
    decrypted = xor_decrypt(encrypted, key)
    print("Decrypted: ", decrypted.decode())
# Example usage:
plaintext = bytes(input().encode())
key = bytes(input().encode())


if len(plaintext.decode()) == len(key.decode()):
    print("Plaintext should not be equal to the key")
elif len(plaintext.decode()) <= len(key.decode()):
    print("Plaintext length should be equal or greater than the length of key")
else:
    encrypted = xor_encrypt(plaintext, key)
    print("Ciphertext: ", encrypted.decode())
    decrypted = xor_decrypt(encrypted, key)
    print("Decrypted: ", decrypted.decode())