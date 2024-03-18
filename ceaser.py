Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text


def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
...     for char in text:
...         if char.isalpha():
...             if char.islower():
...                 decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
...             elif char.isupper():
...                 decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
...         else:
...             decrypted_text += char
...     return decrypted_text
... 
... 
... def main():
...     while True:
...         choice = input("Enter 'e' for encryption, 'd' for decryption, or 'q' to quit: ").lower()
... 
...         if choice == 'e':
...             message = input("Enter the message to encrypt: ")
...             shift = int(input("Enter the shift value: "))
...             encrypted_message = caesar_cipher_encrypt(message, shift)
...             print("Encrypted message:", encrypted_message)
... 
...         elif choice == 'd':
...             message = input("Enter the message to decrypt: ")
...             shift = int(input("Enter the shift value: "))
...             decrypted_message = caesar_cipher_decrypt(message, shift)
...             print("Decrypted message:", decrypted_message)
... 
...         elif choice == 'q':
...             print("Goodbye!")
...             break
... 
...         else:
...             print("Invalid choice. Please enter 'e', 'd', or 'q'.")
... 
... 
... if name == "main":
