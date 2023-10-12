#the interactiviy with the user



import fairy
import elf
import game

#intro
name=input("Please provide your name: ")
print("Welcome to The Magical Forest", name)
print("You must retrieve The Golden Goose from the heart of the forest!\n")

#role selection
print("These are the available classes")
print("Class 1, Fairy - 5 hearts, (+1) dexterity, (-1) intelligence, and (+2) magic")
print("Class 2, Elf - 5 hearts, (-1) dexterity, (+2) intelligence, and (+1) magic")
status=True
while status:
    role=eval(input("Select Class 1 or 2: "))
    if role==1:
        print("You've selected the Fairy class\n")
        stats=fairy.setFairy() #implementing fairy attributes
        break
    elif role==2:
        print("You've selectred the Elf class\n")
        stats=elf.setElf() #implementing elf attributes
        break
    else:
        print("Invalid, please select 1 or 2\n")  
quest=True
while quest==True:
    hp=(stats[0]) #creating variables from chosen role's attributes
    dex=(stats[1])
    intel=(stats[2])
    magic=(stats[3])
    dmg=2
    response="N"
    print("To enter, prove your worth to The Gatekeeper Owl with an intelligence of 4 or higher")
    challenge1result=False
    dice=0
    while challenge1result==False:
        challenge1result, dice = game.challenge1(intel) #implementing challenge 1
        print("You've rolled a", dice)
        print("Your current intelligence is", intel)
        if challenge1result==False:
            newhp=game.deducthp(hp,dmg) #implementing damage if challenge is failed
            print("You lost 2 hearts, remaining hearts", newhp, "\n")
            hp=newhp
            if hp <= 0: #death
                print("You lost all your hearts, you have died")
                response=input("Would you like to try again? Y/N ").upper() #restart option
                if response != "Y":
                    break
    if response == "Y":
        continue

    print("CHALLENGE 1 COMPLETED\n")
    print("Now pass The Werewolf Den without distrubing the cubs with a dexterity of 3 or higher")
    challenge2result=False
    while challenge2result==False:
        challenge2result, dice = game.challenge2(dex) #implementing challenge 2
        print("You've rolled a", dice)
        print("Your current dexterity is", dex)
        if challenge2result==False:
            newhp=game.deducthp(hp,dmg) #implementing damage if challenge is failed
            print("You lost 2 hearts, remaining hearts", newhp, "\n")
            hp=newhp
            if hp <= 0: #death
                print("You lost all your hearts, you have died")
                response=input("Would you like to try again? Y/N ").upper() #restart option
                if response != "Y":
                    break
    if response == "Y":
        continue

    print("CHALLENGE 2 COMPLETED\n")
    print("The Golden Goose is locked behind a magic door. Unlock the door with magic of 5 or higher")
    challenge3result=False
    while challenge3result==False:
        challenge3result, dice = game.challenge3(magic) #implementing challenge 3
        print("You've rolled a", dice)
        print("Your current magic is", magic)
        if challenge3result==False:
            newhp=game.deducthp(hp,dmg) #implementing damage if challenge is failed
            print("You lost 2 hearts, remaining hearts", newhp, "\n")
            hp=newhp
            if hp <= 0: #death
                print("You lost all your hearts, you have died")
                response=input("Would you like to try again? Y/N ").upper() #restart option
                if response != "Y":
                    break
    if response == "Y":
        continue
    if challenge1result and challenge2result and challenge3result: #completion of all 3 challenges
        print("CHALLENGE 3 COMPLETED\n")
        print("Congratulations, you retrieved The Golden Goose and completed the quest!")
    quest=False