import random

#######################
#Variables            #
#######################

#Choose Class
classChosen=False
classExists=True

#Chapter 1


#######################
#Choose Class         #
#######################
while (classChosen==False):
    print("What Class do you choose?")
    print("Warrior, Mage, Thief")
    playerClass=input()
    if (playerClass=="Warrior" or playerClass=="warrior"):
        print("Warrior Stats:")
        print("Strength: 10")
        print("Intelligence: 5")
        print("Agility: 5")
        playerClass="warrior"
    elif (playerClass=="Mage" or playerClass=="mage"):
        print("Warrior Stats:")
        print("Strength: 5")
        print("Intelligence: 10")
        print("Agility: 5")
        playerClass="mage"
    elif (playerClass=="Thief" or playerClass=="thief"):
        print("Warrior Stats:")
        print("Strength: 5")
        print("Intelligence: 5")
        print("Agility: 10")
        playerClass="thief"
    else:
        print("This Class does not exist!")
        classExists=False
    if (classExists==True):
        print("Confirm? Y/N")
        classChosen=input()
        if (classChosen=="y" or classChosen=="Y"):
            if (playerClass=="warrior"):
                print("You are a Warrior!")
                classChosen=True
            elif (playerClass=="mage"):
                print("You are a Mage!")
                classChosen=True
            elif (playerClass=="thief"):
                print("You are a Thief!")
                classChosen=True
        else:
            classChosen=False

#######################
#Chapter 1            #
#######################
for i in range(1500):
    print(" ")


