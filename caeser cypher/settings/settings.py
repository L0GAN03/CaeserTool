import sys
import os
import time

def settings():
    print("entering settings mode... \n")
    time.sleep(0.5)
    animation = input("Do you wish to skip the intro text animation? (Y/N): ")

    if animation == "Y" or animation == "y":

        working_dir = os.path.dirname(os.path.realpath(__file__))
        print(working_dir)
        with  open(r"D:\Coding\Python Coding\caeser cypher\settings\settings.txt", "a") as store:
            store.write("\n" "0")









        

settings()

    