#encryption function
def encrypt(text,s): 
    result = "" 
    for i in range(len(text)):                                 #traverse through the text
        char = text[i] 
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65)        #encryt for upper case
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97)      #encrypt for lower case
    return result 
print("ENCRYPTION")  
text = input("Enter the text to encrypt : ")
c=encrypt(text,3)
print("Text after encryption(cipher) : " +c) 

#decrption function
def decrypt(text,s): 
    result = "" 
    for i in range(len(text)):                               #traverse through the text
        char = text[i] 
        if (char.isupper()): 
            result += chr((ord(char) - s-65) % 26 + 65)      #decryt for upper case
        else: 
            result += chr((ord(char) - s - 97) % 26 + 97)    #decrypt for lower case
    return result 
print("DECRYPTION")
a=input("Accept cipher as input(yes/no) : ")
if(a=="yes"):
    text=c
else:
    text = input("Enter the text to decrypt : ")
print("Text after decrytion : " + decrypt(text,3)) 