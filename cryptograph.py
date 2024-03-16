#part 1
def caesar_decryption(cipher_text,key):#create function to decrypt text
    key=-key                
    for i in range(len(cipher_text)):#iterate among the leanth of the text
        letter=cipher_text[i]
        if ord(letter)==32:#to return space as it is
            print(" ",end="")
        elif 64<ord(letter)<91:#getting uppercase decryption via calculation\ASCII
            s=chr((ord(letter)-65+key)%26+65)
            print(s,end="")
        elif 96<ord(letter)<123:#getting lowercase decryption via calculation\ASCII
            s=chr((ord(letter)-97+key)%26+97)
            print(s,end="")
        else:# to return symbols as it is
            print(letter,end="")
    return""# to avoid printing "none"



def caesar_encryption(text,key):#create function to encrypt text
    for i in range(len(text)):#iterate among the leanth of the text 
        letter=text[i]
        if ord(letter)==32:#to return space as it is
            print(" ",end="")
        elif 64<ord(letter)<91:# getting uppercase encryption via calculation\ASCII 
            s=chr((ord(letter)-65+key)%26+65)
            print(s,end="")
        elif 96<ord(letter)<123:#getting lowercase encryption via calculation\ASCII
            s=chr((ord(letter)-97+key)%26+97)
            print(s,end="")
        else:# to return symbols as it is
            print(letter,end="")
    return""# to avoid printing "none"



#part 2



def encrypt_affine(text, key1, key2):
             
        for t in range(len(text)):#iterate inside a text
            letter=text[t]
            if ord(letter)==32:#to print space 
                print(" ",end="")
            elif 64<ord(letter)<91:#uppercase encryption
                s=chr((( key1*(ord(letter) - 65) + key2 ) % 26) + 65)
                print(s,end="")
            elif 96<ord(letter)<123:#lowercase encryption
                s=chr((( key1*(ord(letter) - 97) + key2 ) % 26) + 97)
                print(s,end="")
            else:# to print symbols as it is

                print(letter,end="")
        return""
    
def affine_decryption(text,key1,key2):
    inv=0
    for i in range(1,27):# to specifi 
        if (key1*i)% 26==1: #getting the invers
            inv = i
            break

    for i in range(len(text)):#iterate inside a text
        letter=text[i]
        if ord(letter)==32:
            print(" ",end="")
        elif 64<ord(letter)<91:#applaing the opration using the invers
            s=chr(((inv*((ord(letter)-65)-key2))%26)+65)
            print(s,end="")
        elif 96<ord(letter)<123:#applaing the opration using the invers
            s=chr(((inv*((ord(letter)-97)-key2))%26)+97)
            print(s,end="")
        else:
            print(letter,end="")
    return""
try:#handling the value error

        while True:
                    question=input("\nplease enter A to use Affain Cipher, C for the Casere Cipher or -1 to end the program : ")#choosing the process
                    if question == "-1":# to end the program
                        break

                    elif question== "C" :#caser cipher
                        question2=input("choose either to encrypt or decrypt your text :")
                        if question2=="encrypt":
                            text=str(input("enter your text: "))# take text from user to do the procces
                            key=int(input("enter the key that you want to use: " ))#key to do the procces based on it
                            print(caesar_encryption(text,key))
                        elif question2=="decrypt":
                            text=str(input("enter your text: "))# take text from user to do the procces
                            key=int(input("enter the key that you want to use: " ))#key to do the procces based on it
                            print(caesar_decryption(text,key))
                        else:
                            print("Enter encrypt or decrypt only")

                            
                    elif question== "A" :#affine cipher
                        question2=input("choose either to encrypt or decrypt your text :")
                        if question2=="encrypt":
                            text=str(input("enter your text: "))# take text from user to do the procces
                            x = True
                            while x:#spicific keys for affain cipher as requirment
                                key1=int(input("enter the key number 1 from range 1 to 25 that will be using " ))
                                if key1 not in range (1,26,2):
                                    print("please enter odd numbers from range 1 to 25 only")
                                    continue
                                key2=int(input("enter the key number 2 that will be using " ))        
                                x = False
                            print(encrypt_affine(text,key1,key2))
                        elif question2=="decrypt":
                            text=str(input("enter your text: "))# take text from user to do the procces
                            y=True
                            while y:#spicific keys for affain cipher as requirment
                                key1=int(input("enter the key number 1 from range 1 to 25 that will be using " ))
                                if key1 not in range (1,26,2):
                                    print("please enter odd numbers from range 1 to 25")
                                    continue
                                key2=int(input("enter the key number 2 that will be using " ))        
                                y = False
                            print(affine_decryption(text,key1,key2))
                        else:
                            print("Enter encrypt or decrypt only")
             
                    else:
                        print("Enter -1 or A or C only")

except ValueError:
    print("The key is only number")
    
    
    
     
