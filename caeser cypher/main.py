#get the imports
import sys
import time
import os


#set the size of the window
os.system('mode con: cols=200 lines=60')

def startup():
    ascii_text = """

    /$$        /$$$$$$   /$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$         /$$$$$$   /$$$$$$  /$$$$$$$$  /$$$$$$  /$$$$$$$$ /$$$$$$$        /$$$$$$$$ /$$$$$$   /$$$$$$  /$$      
    | $$       /$$__  $$ /$$__  $$ /$$__  $$| $$$ | $$ /$$__  $$       /$$__  $$ /$$__  $$| $$_____/ /$$__  $$| $$_____/| $$__  $$      |__  $$__//$$__  $$ /$$__  $$| $$      
    | $$      | $$  \ $$| $$  \__/| $$  \ $$| $$$$| $$| $$  \__/      | $$  \__/| $$  \ $$| $$      | $$  \__/| $$      | $$  \ $$         | $$  | $$  \ $$| $$  \ $$| $$      
    | $$      | $$  | $$| $$ /$$$$| $$$$$$$$| $$ $$ $$|  $$$$$$       | $$      | $$$$$$$$| $$$$$   |  $$$$$$ | $$$$$   | $$$$$$$/         | $$  | $$  | $$| $$  | $$| $$      
    | $$      | $$  | $$| $$|_  $$| $$__  $$| $$  $$$$ \____  $$      | $$      | $$__  $$| $$__/    \____  $$| $$__/   | $$__  $$         | $$  | $$  | $$| $$  | $$| $$      
    | $$      | $$  | $$| $$  \ $$| $$  | $$| $$\  $$$ /$$  \ $$      | $$    $$| $$  | $$| $$       /$$  \ $$| $$      | $$  \ $$         | $$  | $$  | $$| $$  | $$| $$      
    | $$$$$$$$|  $$$$$$/|  $$$$$$/| $$  | $$| $$ \  $$|  $$$$$$/      |  $$$$$$/| $$  | $$| $$$$$$$$|  $$$$$$/| $$$$$$$$| $$  | $$         | $$  |  $$$$$$/|  $$$$$$/| $$$$$$$$
    |________/ \______/  \______/ |__/  |__/|__/  \__/ \______/        \______/ |__/  |__/|________/ \______/ |________/|__/  |__/         |__/   \______/  \______/ |________/
                                                                                                                                                                            
    """
    into_text = """LOGANS CA1ESER TOOL VERSION 1.0(BETA)
    as this is a unfinished version it may contain missing features and/or bugs which have yet to be fixed or included.
    as I am a single person developing this program any help is appreciated and can be sent to me on discord (zeeqoh#1545) and updated into latest versions
    """

    for char in ascii_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0)


    for char in into_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    
startup()

#get the users desired mode

encryption = 1
decryption = 2
settings = 3

print("Anyways, thank you for using my caeser tool \n" " ")
time.sleep(1)
print("""What operation do you wish to perform?
         enter 1 for encyption
         enter 2 for decryption
         enter 3 for settings
        """)


user_response = int(input(": "))

if user_response == encryption:
    from encrypt import encrypt

       





