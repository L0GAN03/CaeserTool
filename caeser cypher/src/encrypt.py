import sys
import time
import os

from main import user_settings

alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt(): 
    print("Entering encryption mode... \n" "  ")
    time.sleep(user_settings.pause_timers)
    user_string = input("please enter the string to be edited: \n") 
    shift_amount = int(input("please enter how many letters you want to shift by: \n"))

    user_string_lower = user_string.lower()

    user_string_list = user_string_lower.split()
    #print(user_string_list)

    WORD = 0

    for words in user_string_list:
        secret = "".join([alphabet[(alphabet.find(c)+shift_amount)%26] for c in user_string_list[WORD]])
    
        print(secret, end=" ", flush=True)
    
        WORD = WORD + 1
        
    return None

encrypt()

