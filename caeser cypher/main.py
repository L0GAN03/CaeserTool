#get the imports
import sys
import time
import os


#set the size of the window
os.system('mode con: cols=200 lines=60')

#get the users settings
class user_settings():
    working_dir = os.path.dirname(os.path.realpath(__file__))
    working_dir = working_dir + "\settings\settings.txt"

    print(working_dir)

    with  open(working_dir, "a") as store:
        store.write("0.01\n0.5")

    user_settings = list(open(working_dir))

    user_settings = [x.replace("\n", "") for x in user_settings]
    #print(user_settings)
        
    animation = 0
    pause_timers = 0

    animation = float(user_settings[0])
    pause_timers = float(user_settings[1])



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

    intro_text = """LOGANS CAESER TOOL VERSION 2.0
    as this is a unfinished version it may contain missing features and/or bugs which have yet to be fixed or included.
    as I am a single person developing this program any help is appreciated and can be sent to me on GITHUB (https://github.com/L0GAN03/CaeserTool) and updated into latest versions. 
    Any ideas send me them on discord (zeeqoh#1545)
    """

    for char in ascii_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0)


    for char in intro_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(user_settings.animation)
    
startup()

#get the users desired mode
encryption = 1
decryption = 2
settings = 3

print("Anyways, thank you for using my caeser tool \n" " ")
time.sleep(user_settings.pause_timers)
print("""What operation do you wish to perform?
        enter 1 for encyption
        enter 2 for decryption
        enter 3 for settings #currently not working
        """)

user_response = int(input(": "))


if user_response == encryption:
    from src.encrypt import encrypt
        


elif user_response == decryption:
    from src.decrypt import decrypt


elif user_response == settings:
    working_dir = os.path.dirname(os.path.realpath(__file__))
    working_dir = working_dir + "\settings\settings.txt"
    os.remove(working_dir)
    user_settings()
    from settings.settings import settings
        

        
       



 
#timer to close the program

def autoshut():
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

autoshut()