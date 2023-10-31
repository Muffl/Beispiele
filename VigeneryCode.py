def vigenere_encrypt(text, key):
    encrypted_text = ""
    key_full = key * (len(text) // len(key)) + key[:len(text) % len(key)]
    
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key_full[i].upper()) - ord('A')
            if char.isupper():
                encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char

    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_full = key * (len(encrypted_text) // len(key)) + key[:len(encrypted_text) % len(key)]

    for i, char in enumerate(encrypted_text):
        if char.isalpha():
            shift = ord(key_full[i].upper()) - ord('A')
            if char.isupper():
                decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char

    return decrypted_text

# Test
text = "HELLO WORLD"
key = "KEY"
encrypted = vigenere_encrypt(text, key)
print(f"Verschlüsselt: {encrypted}")
print(f"Entschlüsselt: {vigenere_decrypt(encrypted, key)}")
