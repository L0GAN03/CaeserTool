import sys
import os
import time

from main import user_settings

def settings():
    print("entering settings mode... \n")
    time.sleep(user_settings.pause_timers)
    animation = input("Do you wish to skip the intro text animation? (Y/N): ")

    if animation == "Y" or animation == "y":

        working_dir = os.path.dirname(os.path.realpath(__file__))
        working_dir = working_dir + "\settings.txt"
        print(working_dir)
        with  open(working_dir, "a") as store:
            store.write("0 \n")
    
    elif animation == "N" or animation == "n":

        working_dir = os.path.dirname(os.path.realpath(__file__))
        working_dir = working_dir + "\settings.txt"

        with  open(working_dir, "a") as store:
            store.write("0.01 \n")


    pause_timer = input("Do you wish to stop any pause timers in the programn and have it run as fast as possible? (Y/N): ")

    if pause_timer == "Y" or pause_timer == "y":

        working_dir = os.path.dirname(os.path.realpath(__file__))
        working_dir = working_dir + "\settings.txt"
        #print(working_dir)
        
        with  open(working_dir, "a") as store:
            store.write("0 \n")

    elif pause_timer == "N" or pause_timer == "n":

        working_dir = os.path.dirname(os.path.realpath(__file__))
        working_dir = working_dir + "\settings.txt"

        with  open(working_dir, "a") as store:
            store.write("0.5\n")





def import_settings():
    working_dir = os.path.dirname(os.path.realpath(__file__))
    working_dir = working_dir + "\settings.txt"
    user_settings = list(open(working_dir))

    user_settings = [x.replace("\n", "") for x in user_settings]
    #print(user_settings)








settings()


    