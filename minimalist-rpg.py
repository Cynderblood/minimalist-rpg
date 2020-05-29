from pathlib import Path
import random
import os
import time
#Alpha 3, 29.05.2020

#######################
#Variables            #
#######################

#Savestate(s in the future)
savestate_exists = "none"
create_new_savestate = "none"
load_savestate = "none"
strength_path = Path('./savestate1/player/strength.txt')
intelligence_path = Path('./savestate1/player/intelligence.txt')
agility_path = Path('./savestate1/player/agility.txt')
class_path = Path('./savestate1/player/class.txt')

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
        os.mkdir('savestate1/player')
    else:
        raise SystemExit
elif (savestate_exists == True):
    print("A savestate was found.")
    print(" ")
    print("Class: "+class_path.read_text())
    print("Strength: "+strength_path.read_text())
    print("Intelligence: "+intelligence_path.read_text())
    print("Agilty: "+agility_path.read_text())
    print(" ")
    print("Do you want to load it? Y/N")
    load_savestate = input()
    if (load_savestate == "y" or load_savestate == "Y"):
        class_chosen = True
        strength = strength_path
        intelligence = intelligence_path
        agility = agility_path
    else:
        print("Do you want to create a new savestate? Y/N")
        create_new_savestate = input()
        if (create_new_savestate == "y" or create_new_savestate == "Y"):
            print("This will overwrite your old savestate.")
            print("Are you sure? Y/N")
            create_new_savestate = input()
            print(" ")
            if (create_new_savestate == "y" or create_new_savestate == "Y"):
                class_chosen = False
            else:
                #Search for a better solution than this
                raise SystemExit

#######################
#Choose Class         #
#######################
while (class_chosen == False):
    print("What Class do you choose?")
    print("Warrior, Mage, Thief")
    player_class = input()
    print(" ")
    if (player_class == "Warrior" or player_class == "warrior"):
        print("Warrior Stats:")
        print("Strength: 10")
        print("Intelligence: 5")
        print("Agility: 5")
        class_exists = True
        player_class = "Warrior"
    elif (player_class == "Mage" or player_class == "mage"):
        print("Mage Stats:")
        print("Strength: 5")
        print("Intelligence: 10")
        print("Agility: 5")
        class_exists = True
        player_class = "Mage"
    elif (player_class == "Thief" or player_class == "thief"):
        print("Thief Stats:")
        print("Strength: 5")
        print("Intelligence: 5")
        print("Agility: 10")
        class_exists = True
        player_class = "Thief"
    else:
        print("This Class does not exist!")
        class_exists = False
        class_chosen = False
    if (class_exists == True):
        print(" ")
        print("Confirm? Y/N")
        class_chosen = input()
        print(" ")
        if (class_chosen == "y" or class_chosen == "Y"):
            if (player_class == "Warrior"):
                print("You are a Warrior!")
                class_path.write_text('Warrior')
                strength_path.write_text('10')
                intelligence_path.write_text('5')
                agility_path.write_text('5')
                class_chosen = True
                time.sleep(1)
            elif (player_class == "Mage"):
                print("You are a Mage!")
                class_path.write_text('Mage')
                strength_path.write_text('5')
                intelligence_path.write_text('10')
                agility_path.write_text('5')
                class_chosen = True
                time.sleep(1)
            elif (player_class == "Thief"):
                print("You are a Thief!")
                class_path.write_text('Thief')
                strength_path.write_text('5')
                intelligence_path.write_text('5')
                agility_path.write_text('10')
                class_chosen = True
                time.sleep(1)
        else:
            class_chosen = False

#######################
#Chapter 1            #
#######################
for i in range(150):
    print(" ")
