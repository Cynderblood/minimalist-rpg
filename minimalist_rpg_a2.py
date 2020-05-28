from pathlib import Path
import random
import os
import time
#Alpha 2, 28.05.2020

#######################
#Variables            #
#######################

#Savestate(s in the future)
savestate_exists = "none"
create_new_savestate = "none"
strength_path = Path('./savestate1/strength.txt')
intelligence_path = Path('./savestate1/intelligence.txt')
agility_path = Path('./savestate1/agility.txt')

#Player
player_class = "none"
strength = 0
intelligence = 0
agility = 0

#Choose Class
class_chosen = False
class_exists = True

#Chapter 1

#######################
#Savestate(s)         #
#######################
savestate_exists = os.path.isdir('savestate1')
if (savestate_exists == False):
    print("No Savestate was found.")
    print("Do you want to create a new one? Y/N")
    create_new_savestate = input()
    print(" ")
    if (create_new_savestate == "Y" or create_new_savestate == "y"):
        os.mkdir('savestate1')
    else:
        raise SystemExit
elif (savestate_exists == True):
    #implement savestate loading here
    print("Implement savestate loading here")
    print(" ")
    print("If you don't want to see this message,")
    print("delete the savestate1 folder in the cwd")
    time.sleep(1)
    raise SystemExit

#######################
#Choose Class         #
#######################
while (class_chosen == False):
    print("What Class do you choose?")
    print("Warrior, Mage, Thief")
    player_class = input()
    if (player_class == "Warrior" or player_class == "warrior"):
        print("Warrior Stats:")
        print("Strength: 10")
        print("Intelligence: 5")
        print("Agility: 5")
        class_exists = True
        player_class = "warrior"
    elif (player_class == "Mage" or player_class == "mage"):
        print("Mage Stats:")
        print("Strength: 5")
        print("Intelligence: 10")
        print("Agility: 5")
        class_exists = True
        player_class = "mage"
    elif (player_class == "Thief" or player_class == "thief"):
        print("Thief Stats:")
        print("Strength: 5")
        print("Intelligence: 5")
        print("Agility: 10")
        class_exists = True
        player_class = "thief"
    else:
        print("This Class does not exist!")
        class_exists = False
        class_chosen = False
    if (class_exists == True):
        print("Confirm? Y/N")
        class_chosen = input()
        if (class_chosen == "y" or class_chosen == "Y"):
            if (player_class == "warrior"):
                print("You are a Warrior!")
                strength_path.write_text('10')
                intelligence_path.write_text('5')
                agility_path.write_text('5')
                class_chosen = True
            elif (player_class == "mage"):
                print("You are a Mage!")
                strength_path.write_text('5')
                intelligence_path.write_text('10')
                agility_path.write_text('5')
                class_chosen = True
            elif (player_class == "thief"):
                print("You are a Thief!")
                strength_path.write_text('5')
                intelligence_path.write_text('5')
                agility_path.write_text('10')
                class_chosen = True
        else:
            class_chosen = False
time.sleep(1)
#######################
#Chapter 1            #
#######################
for i in range(150):
    print(" ")
