'''Ques 1.  Write a program that can encrypt
            and decrypt using the Additive Cipher.'''
#index of character is its value
alpha_list=['A','B','C','D','E','F','G','H',
            'I','J','K','L','M','N','O','P',
            'Q','R','S','T','U','V','W','X','Y','Z']

''' encrypt_the_plain_text() is a function which takes
    two arguments - plain_text and a key, and
    returns the cipher_text '''

def encrypt_the_plain_text(plain_text,key):
    cipher_text=''
    #iterate the plain_text
    for plain_text_alphabet in plain_text:
        #shifting each character of plain_text 
        cipher_alphabet=(alpha_list.index(plain_text_alphabet)+key)%26
        #adding the shifted character to the output
        cipher_text+=alpha_list[cipher_alphabet]
    #returning the encrypted text
    return cipher_text

''' encrypt_the_cipher_text() is a function which takes
    two arguments - cipher_text and a key, and
    returns the plain_text '''

def decrypt_the_cipher_text(cipher_text,key):
    plain_text=''
    #iterate the cipher_text
    for cipher_text_alphabet in cipher_text:
        #shifting back each character of cipher_text 
        plain_alphabet=(alpha_list.index(cipher_text_alphabet)-key)%26
        plain_text+=alpha_list[plain_alphabet]
    #returning the decrypted text
    return plain_text

def main():
    #counter to run the input loop
    choice='Y'
    #Menu driven for input and output
    while(choice=='Y'):
        print('''Additive Cipher
What do you want to do :
Press
1.Encryption
2.Decryption
 ''' )
        option=int(input("Enter your choice: "))
        
        if option==1:
            #for encryption taking plain_text and key as input
            #and calling the encrypt function
            plain_text=input("Enter the plain text : ").upper()
            key=int(input("Enter the key : "))
            print("Encrypted message : ",encrypt_the_plain_text(plain_text,key))

        elif option==2:
            #for decryption taking cipher_text and key as input
            #and calling the decrypt function
            cipher_text=input("Enter the cipher text : ").upper()
            key=int(input("Enter the key : "))
            print("Encrypted message : ",decrypt_the_cipher_text(cipher_text,key))

        else:
             print("Wrong Choice : ")

        choice=input("Want to continue (Enter 'Y' for yes ) :")

main()
