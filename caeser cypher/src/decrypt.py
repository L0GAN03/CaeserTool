import sys
import time
import os

from main import user_settings

alphabet = "abcdefghijklmnopqrstuvwxyz"

def decrypt():
    print("Entering decryption mode... \n" "  ")
    time.sleep(user_settings.pause_timers)
    mode_select = input("Do you want to brute force or manually decrypt the cipher: (B/M): ")

    if mode_select == "B" or mode_select == "b":
        user_string = input("please enter the string to be edited: \n") 

        user_string_lower = user_string.lower()
        user_string_list = user_string_lower.split()

        shift_amount = 1  
        print(user_string_list)

        for i in range(1, 26):
                secret_decrypt_one = "".join([alphabet[(alphabet.find(c)-shift_amount)%26] for c in user_string_list[0]])
                secret_decrypt_two = "".join([alphabet[(alphabet.find(c)-shift_amount)%26] for c in user_string_list[1]])
   
                shift_amount = shift_amount + 1
                print("decrypting with a shift key of", (shift_amount - 1))
                print(secret_decrypt_one, secret_decrypt_two)
                print(" ")
                time.sleep(user_settings.pause_timers)



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