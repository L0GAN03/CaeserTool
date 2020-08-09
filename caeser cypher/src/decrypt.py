import sys
import time
import os

alphabet = "abcdefghijklmnopqrstuvwxyz"

def decrypt():
    print("Entering decryption mode... \n" "  ")
    time.sleep(0.5)
    mode_select = input("Do you want to brute force or manually decrypt the cipher: (B/M): ")

    if mode_select == "B" or mode_select == "b":
        user_string = input("please enter the string to be edited: \n") 

        user_string_lower = user_string.lower()
        user_string_list = user_string_lower.split()

        shift_amount = 1
        WORD = 0    
        i = 0
        print(user_string_list)

        for i in range(1, 26):
                secret_decrypt = "".join([alphabet[(alphabet.find(c)-shift_amount)%26] for c in user_string_list[WORD]])
                shift_amount = shift_amount + 1
                print("decrypting with a shift key of", (shift_amount - 1))
                print(secret_decrypt)
                print(" ")
                time.sleep(0.5)




    elif mode_select == "M" or mode_select == "m":
        user_string = input("please enter the string to be edited: \n") 
        shift_amount = int(input("please enter how many letters you want to shift by: \n"))

        
        user_string_lower = user_string.lower()

        user_string_list = user_string_lower.split()
        #print(user_string_list)

        WORD = 0

        for words in user_string_list:
            secret = "".join([alphabet[(alphabet.find(c)-shift_amount)%26] for c in user_string_list[WORD]])
    
            print(secret, end=" ", flush=True)
    
            WORD = WORD + 1
        
        return None



    else:
        print("An error occured")






decrypt()