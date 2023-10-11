import fairy
import elf
import game


name=input("Please provide your name: ")
print("Welcome to The Magical Forest", name)
print("You must retrieve The Golden Goose from the heart of the forest!")
print("These are the available classes")
print("Class 1, Fairy - 5 hearts, (+1) dexterity, (-1) intelligence, and (+2) magic")
print("Class 2, Elf - 5 hearts, (-1) dexterity, (+2) intelligence, and (+1) magic")
status=True
while status:
    role=eval(input("Select Class 1 or 2: "))
    if role==1:
        print("You've selected the Fairy class")
        stats=fairy.setFairy()
        break
    elif role==2:
        print("You've selectred the Elf class")
        stats=elf.setElf()
        break
    else:
        print("Invalid, please select 1 or 2")  
hp=(stats[0])
dex=(stats[1])
intel=(stats[2])
magic=(stats[3])
dmg=2

print("To enter, prove your worth to The Gatekeeper Owl with an intelligence of 4 or higher")
challenge1result=False
while challenge1result==False:
    challenge1result=game.challenge1(intel)
    if challenge1result==False:
        newhp=game.deducthp(hp,dmg)
        print("lost hp",newhp)
        hp=newhp
        if hp <= 0:
            print("you died")
            exit(1)

print("CHALLENGE 1 COMPLETED")
print("Now pass The Werewolf Den without distrubing the cubs with a dexterity of 3 or higher")
challenge2result=False
while challenge2result==False:
    challenge2result=game.challenge2(dex)
    if challenge2result==False:
        newhp=game.deducthp(hp,dmg)
        print("lost hp",newhp)
        hp=newhp
        if hp <= 0:
            print("you died")
            exit(1)

print("CHALLENGE 2 COMPLETED")
print("The Golden Goose is locked behind a magic door. Unlock the door with magic of 5 or higher")
challenge3result=False
while challenge3result==False:
    challenge3result=game.challenge3(magic)
    if challenge3result==False:
        newhp=game.deducthp(hp,dmg)
        print("lost hp",newhp)
        hp=newhp
        if hp <= 0:
            print("you died")
            exit(1)

print("CHALLENGE 3 COMPLETED")
print("You win")