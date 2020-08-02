#CAESER CYPHER / ROT ALGORITHM 
#MADE BY LOGAN (zeeqoh#1545 on discord)

#get the imports
import sys
import time
import os
from codecs import decode

#lets resize the cmd window
os.system('mode con: cols=200 lines=60')

#some fancy text cause why not
ascii_text ="""

 /$$        /$$$$$$   /$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$         /$$$$$$   /$$$$$$  /$$$$$$$$  /$$$$$$  /$$$$$$$$ /$$$$$$$        /$$$$$$$$ /$$$$$$   /$$$$$$  /$$      
| $$       /$$__  $$ /$$__  $$ /$$__  $$| $$$ | $$ /$$__  $$       /$$__  $$ /$$__  $$| $$_____/ /$$__  $$| $$_____/| $$__  $$      |__  $$__//$$__  $$ /$$__  $$| $$      
| $$      | $$  \ $$| $$  \__/| $$  \ $$| $$$$| $$| $$  \__/      | $$  \__/| $$  \ $$| $$      | $$  \__/| $$      | $$  \ $$         | $$  | $$  \ $$| $$  \ $$| $$      
| $$      | $$  | $$| $$ /$$$$| $$$$$$$$| $$ $$ $$|  $$$$$$       | $$      | $$$$$$$$| $$$$$   |  $$$$$$ | $$$$$   | $$$$$$$/         | $$  | $$  | $$| $$  | $$| $$      
| $$      | $$  | $$| $$|_  $$| $$__  $$| $$  $$$$ \____  $$      | $$      | $$__  $$| $$__/    \____  $$| $$__/   | $$__  $$         | $$  | $$  | $$| $$  | $$| $$      
| $$      | $$  | $$| $$  \ $$| $$  | $$| $$\  $$$ /$$  \ $$      | $$    $$| $$  | $$| $$       /$$  \ $$| $$      | $$  \ $$         | $$  | $$  | $$| $$  | $$| $$      
| $$$$$$$$|  $$$$$$/|  $$$$$$/| $$  | $$| $$ \  $$|  $$$$$$/      |  $$$$$$/| $$  | $$| $$$$$$$$|  $$$$$$/| $$$$$$$$| $$  | $$         | $$  |  $$$$$$/|  $$$$$$/| $$$$$$$$
|________/ \______/  \______/ |__/  |__/|__/  \__/ \______/        \______/ |__/  |__/|________/ \______/ |________/|__/  |__/         |__/   \______/  \______/ |________/
                                                                                                                                                                           
"""
into_text = """LOGANS CAESER TOOL VERSION 1.0(BETA)
as this is a unfinished version it may contain missing features and/or bugs which have yet to be fixed or included.
as I am a single person developing this program any help is appreciated and can be sent to me on discord (zeeqoh#1545) and updated into latest versions
"""

for char in ascii_text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.0001)


for char in into_text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.01)


#actual code now not some fancy text lol
#

alphabet = "abcdefghijklmnopqrstuvwxyz"

encrypt = 1
decrypt = 2
decrypt_fine = 1
decrypt_brute = 2
shift_amount = 0
print("Anyways, thank you for using my caeser tool")
print("")
time.sleep(1)
print("""What operation do you wish to perform?
         enter 1 for encyption
         enter 2 for decryption
        """)
user_response = int(input(": "))

#encyption part
if user_response == encrypt:
    print("Entering encryption mode...")
    print(" ")
    time.sleep(0.5)
    shift_amount = int(input("How many letters do you want to shift by? (1 - 25): "))
    while shift_amount < 1 or shift_amount > 25:
        print("invalid range, please restart")
        break

    else:
        time.sleep(0.5)
        print("beginning encryption")
        print(" ")
        user_string_raw = str(input("enter the phrase to be encrypted: "))
        user_string_lowercase = user_string_raw.lower()
        secret_encrypt = "".join([alphabet[(alphabet.find(c)+shift_amount)%26] for c in user_string_lowercase])
        print("your encrypted message is: ")
        print(secret_encrypt)
        print(" ")
        print("note this will not include spaces!")
        

#decryption part
if user_response == decrypt:
    print("Entering decryption mode...")
    print(" ")
    time.sleep(0.5)
    print("press 1 for a defined decryption")
    print("press 2 for brute forcing the decryption (trying all posibilites)")
    time.sleep(0.5)
    decrypt_style = int(input("enter the style of decryption: "))
    if decrypt_style == decrypt_fine:
        key_type = int(input("what shift amount do you want to use? "))
        user_string_raw = input("enter the encrypted message: ")
        user_string_lowercase = user_string_raw.lower()
        secret_decrypt = " ".join([alphabet[(alphabet.find(c)-key_type)%26] for c in user_string_lowercase])
        print(" ")
        print("your decrypted message is:")
        print(secret_decrypt)
#brute decrypt
    elif decrypt_style == decrypt_brute:
        key_type = 0
        user_string_raw = input("enter the encrypted message: ")
        user_string_lowercase = user_string_raw.lower()
        print("trying all shift methods...")
        print(" ")
        time.sleep(0.5)
        for i in range(1, 26):
            secret_decrypt = " ".join([alphabet[(alphabet.find(c)-key_type)%26] for c in user_string_lowercase])
            key_type = key_type + 1
            print("decrypting with a shift key of ", (key_type - 1))
            print(secret_decrypt)
            print(" ")
            time.sleep(0.5)



 #timer to close the program
print(" ")
print(" ")
when_to_stop = 0
while True:
    uin = 60
    try:
        when_to_stop = abs(int(uin))
    except KeyboardInterrupt:
        break
    except:
        print("Not a number!")
    while when_to_stop > 0:
        m, s = divmod(when_to_stop, 60)
        h, m = divmod(m, 60)
        time_left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
        print("\r", "program auto closing in: " , end=time_left)
        time.sleep(1)
        when_to_stop -= 1
    time.sleep(1)
    exit()




    