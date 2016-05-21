from RSA import *
from options import *

def new_cipher():
    cipher = RSA_Cipher()
    print(cipher)
    print()
    save = input('Would you like to save this as your new cipher? [y/n]\n> ')
    if 'y' in save:
        options = Options()
        options.change_cipher(cipher.public_key, cipher.private_key)
        options.save()
        print('saved')
        
        
def encrypt(message):
    '''
    Encrypts ciphertext, with public key.
    '''    
    
    options = Options()
    
    e = options.public_key[1]
    n = options.public_key[0]    
    
    cipher_text = ''
    
    ascii_mess = [ord(char) for char in str(message[8:])]

    for num in ascii_mess:
        cipher_text += str((num ** e) % n)
        cipher_text += (' ')
    
    print('Encrypted using your current cipher:')
    print(cipher_text[:-1])
    
    
def decrypt(cipher_text):
    '''
    Decrypts ciphertext, with private key.
    '''
    
    options = Options()
    
    d = options.private_key[1]
    n = options.private_key[0]    

    encrypted_ascii_mess = cipher_text[8:].split(' ')

    decrypted_mess = ''
    
    for char in encrypted_ascii_mess:
        decrypted_mess += chr(pow(int(char), d, n))
        
    print('Decrypted using your current cipher:\n')
    print(decrypted_mess)