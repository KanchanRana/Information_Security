'''Ques 3. Write a program that can perform a letter
           frequency attack on an additive cipher
           without human intervention. Your software
           should produce possible plain text in rough
           order of likelihood. It would be good if your
           user interface allows user to specify
           " Give me top 10 possible plain texts"'''

#index of character is its value
alpha_list=['A','B','C','D','E','F','G','H','I',
              'J','K','L','M','N','O','P','Q','R',
              'S','T','U','V','W','X','Y','Z']
            
'''we call this function after finding the key using frequency attack
   decrypt_the_cipher_text() is a function that take two argument :
   cipher_text and key , and returns the plain_text'''
  
def decrypt_the_cipher_text(cipher_text,key):
    plain_text=''
    #iterate the plain_text
    for cipher_text_alphabet in cipher_text:
        #shifting each character of plain_text
        plain_alphabet=(alpha_list.index(cipher_text_alphabet)-key)%26
        #adding the shifted character to the output
        plain_text+=alpha_list[plain_alphabet]
    #returning the encrypted text in lower case
    return plain_text.lower()

'''decrypt_the_cipher_text_frequency_attack() is a function
   which take two arguments : cipher_text and no_of_plain_text you
   want see.This function find the key and call the decrypt function
   of additive cipher and return possible plain_text of given cipher text'''

def decrypt_the_cipher_text_frequency_attack(cipher_text,no_of_plain_text=1):
    #this dictionary contain the frequency of each char in cipher text
    frequency_Dict={}
    #index 0 contain the highest freqency char 
    precedence=['E','T','A','O','I','N','S','H','R','D']
    #creating the frequency dictionary by iterating the cipher text
    for i in  cipher_text:
        frequency_Dict.setdefault(i, 0)
        frequency_Dict[i]=frequency_Dict[i]+1
    #iterate over the above created dictionary to get the most frequent char
    max_frequency=0
    max_frequency_char=''
    for i,j in frequency_Dict.items():
        if j>max_frequency:
            max_frequency=j
            max_frequency_char=i
    #find the key
    #comparing the most frequent char of cipher text
    #with highest frequency char from frequency table one by one
    for most_frequent in precedence:
        key_1=alpha_list.index(most_frequent)#plain
        key_2=alpha_list.index(max_frequency_char)#cipher
        if key_1<key_2:
            key=key_2-key_1
        else :
            key=26-key_2+key_1
        #after finding the key call the decrypt function of additive cipher  
        print(decrypt_the_cipher_text(cipher_text,key))
        #if user want only  first possible plain text
        if no_of_plain_text==1:
            break

def main():
    #counter to run the input loop
    choice='Y'
    #Menu driven for input and output
    #Sample input 
    #cipher_text="XLILSYWIMWRSAJSVWEPIJSVJSYVQMPPMSRHSPPEVWMXMWASVXLQSVILYVVCFIJSVIXLIWIPPIVVIGIMZIWQSVISJJIVW"
    while(choice=='Y'):
        print('''Frequency Attack
What do you want to do :
Press
1.First Possible plain_text
2.Top 10 possible plain texts
 ''' )
        option=int(input("Enter your choice: "))
        
        if option==1:
            #taking the cipher text as input and
            #calling the function to get first possible plain text
            cipher_text=input("Enter the cipher text : ").upper()
            print("First Possible Plain Text : ")
            decrypt_the_cipher_text_frequency_attack(cipher_text,1)

        elif option==2:
            #taking the cipher text as input and
            #calling the function to get top 10 possible plain text
            cipher_text=input("Enter the cipher text : ").upper()
            print("Top 10 Possible Plain Text : ")
            decrypt_the_cipher_text_frequency_attack(cipher_text,10)
        else:
             print("Wrong Choice : ")

        choice=input("Want to continue (Enter 'Y' for yes ) :")

main()


