#implements of the game
#challenges and damage rules




import random

#challenge 1
def challenge1(intel):
    challenge_1=0
    while challenge_1 < 4:
        lvl=random.randint(1,6)
        challenge_1 = intel + lvl
        if challenge_1 < 4:
            return False, lvl
        else:
            return True, lvl

#challenge 2       
def challenge2(dex):
    challenge_2=0
    while challenge_2 < 3:
        lvl=random.randint(1,6)
        challenge_2 = dex + lvl
        if challenge_2 < 3:
            return False, lvl
        else:
            return True, lvl

#challenge 3       
def challenge3(magic):
    challenge_3=0
    while challenge_3 < 5:
        lvl=random.randint(1,6)
        challenge_3 = magic + lvl
        if challenge_3 < 5:
            return False, lvl
        else:
            return True, lvl
        
#health deduction from failing challenges
def deducthp(hp,dmg):
    newhp=0
    newhp=hp-dmg
    return newhp
