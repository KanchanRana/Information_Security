'''Ques 5. Write a program that can encrypt and
           Decrypt using a 2 X 2 Hill Cipher'''

import numpy as np

#index of character is its value
alpha_list=['A','B','C','D','E','F','G','H',
            'I','J','K','L','M','N','O','P',
            'Q','R','S','T','U','V','W','X','Y','Z']

''' hill_cipher_encrypt() is a function which takes an
    argument - plain_text and returns the cipher_text '''

def hill_cipher_encrypt(plain_text):
    #hill key
    key=np.array([[7,8],[11,11]])
    cipher_text=""
    #iterate the plain_text
    for i in range(0,len(plain_text),2):
        #encryp is column matrix containing 2 char plain_text value
        encryp=np.array([[alpha_list.index(plain_text[i])],[alpha_list.index(plain_text[i+1])]])
        #multiplying hill matrix with column matrix and then taking mod 26
        encryp_two=(np.dot(key,encryp))%26
        #getting encrpyted char of above two plain_text char and adding in the output
        cipher_text+=alpha_list[encryp_two[0,0]]+alpha_list[encryp_two[1,0]]
    #returning the encrypted message
    return cipher_text

''' hill_cipher_decrypt() is a function which takes an
    arguments - cipher_text and returns the plain_text '''

def hill_cipher_decrypt(cipher_text):
    #hill key for encryption
    key=np.array([[7,8],[11,11]])
    #hill key inverse for decryption
    key_inv=np.array([[25,22],[1,23]])
    plain_text=""
    #iterate the cipher_text
    for i in range(0,len(cipher_text),2):
        #decryp is column matrix containing 2 char cipher_text value
        decryp=np.array([[alpha_list.index(cipher_text[i])],[alpha_list.index(cipher_text[i+1])]])
        #multiplying hill matrix inverse with column matrix and then taking mod 26
        decryp_two=(np.dot(key_inv,decryp))%26
        #getting decrpyted char of above two plain_text char and adding in the output
        plain_text+=alpha_list[decryp_two[0,0]]+alpha_list[decryp_two[1,0]]
    return plain_text

def main():
    #counter to run the input loop
    choice='Y'
    #Menu driven for input and output
    while(choice=='Y'):
        print('''Hill Cipher
What do you want to do :
Press
1.Encryption
2.Decryption
 ''' )
        option=int(input("Enter your choice: "))
        
        if option==1:
            #for encryption taking plain_text as input
            #and calling the encrypt function
            plain_text=input("Enter the plain text : ").upper()
            print("Encrypted message : ",hill_cipher_encrypt(plain_text))

        elif option==2:
            #for decryption taking cipher_text as input
            #and calling the decrypt function
            cipher_text=input("Enter the cipher text : ").upper()
            print("Encrypted message : ",hill_cipher_decrypt(cipher_text))

        else:
             print("Wrong Choice : ")

        choice=input("Want to continue (Enter 'Y' for yes ) :")

main()
