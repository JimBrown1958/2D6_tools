# battleActions.py
import Dice as D

def attackHero(battleRound, extraShift):
    pd = D.roll_1D6()
    sd = D.roll_1D6()
    D.clear()
    print("Combat round:", battleRound, "Additional shift:", extraShift)

    print("You attack with a Primary:", pd, "and a Secondary:", sd)
    if battleRound >= 7:
        print("Ignore all movement interupts for enemy")

    if pd == 1 and sd == 1:
        print("You made a mishap roll and completely miss the enemy")
    if pd == 6 and sd == 6:
        print("You made a Prime attack and can use any attack and not miss")
    
    print("If enemy is still alive, they attack next")

def attackEnemy(battleRound, extraShift):
    pd = D.roll_1D6()
    sd = D.roll_1D6()
    D.clear()
    print("Combat round:", battleRound, "Additional shift:", extraShift)

    print("Enemy attacks with a Primary:",pd , "and a Secondary:", sd)
    
    if pd == 1 and sd == 1:
        print("Your enemy made a mishap roll and completely missed you")
    if pd == 6 and sd == 6:
        print("Your enemy made a Prime attack,")
        print("follow the Prime Attck instructions on enemy card")

def actionPotion(battleRound, extraShift):
    D.clear()
    print("Combat round:", battleRound, "Additional shift:", extraShift)
    if battleRound >= 7:
        print("Ignore all movement interupts for enemy")
    print("You quaff the Magic Potion ...")
    print("You have consumed the potion")
    print("If enemy still alive, they attack next")
    
def actionScroll(battleRound, extraShift):
    D.clear()
    print("Combat round:", battleRound, "Additional shift:", extraShift)
    if battleRound >= 7:
        print("Ignore all movement interupts for enemy")
    print("You read the magic scroll ...")
    print("Primary",D.roll_1D6(),"Secondary", D.roll_1D6())
    print("Your scroll disappears into dust")
    print("You gain 5xp")
    print("If enemy still alive, they attack next")
    
def throwWeapon():
    D.clear()
    print("Throw weapon ...",)
    print("Primary",D.roll_1D6(),"Secondary", D.roll_1D6())
    lostWeapon = D.roll_1D6()
    if lostWeapon >= 1 and lostWeapon <= 3:
        print("Your weapon flies off into the dungeon and is lost")
    else:
        print("You successfully retrieve your weapon from the ground")
    print("You can now attack the enemy")


def battleMenu():
    battleRound = 0
    extraShift = 0
    battleOption = ""
    potionUsed = 0
    scrollUsed = 0
    weaponThrown = 0
    
    while True:
        D.clear()
        # Print menu ang get option
        print("Battle Menu")
        print("===========")
        print()
        print("Combat round:", battleRound, "Additional shift:", extraShift)
        print()
        print("Select option for battle:")
        print("1: Roll for Hero attack (this starts a new round)")
        print("2: Roll for Enemy attack")
        print("3: Quaff Magic potion")
        if scrollUsed == 0 and battleRound == 0:
            print("4: Use Magic Scroll, only available when 'Combat round' = 0. Uses up 1st combat round")
        if weaponThrown == 0 and battleRound == 0:
            print("5: Throw weapon, only available when 'Combat round' = 0. Does not use up a combat round")
        print()
        print("0: return to top menu")
        battleOption = input("? ")
        
        # Process option selected
        if battleOption == "1":
            battleRound += 1
            if battleRound >= 4 and battleRound <= 6:
                extraShift += 1
            attackHero(battleRound, extraShift)

        elif battleOption == "2":
            attackEnemy(battleRound, extraShift)
            
        elif battleOption == "3":
            battleRound += 1
            if battleRound >= 4 and battleRound <= 6:
                extraShift += 1
            actionPotion(battleRound, extraShift)
            potionUsed += 1

        elif battleOption =="4" and scrollUsed == 0 and battleRound == 0:
            battleRound += 1
            if battleRound >= 4 and battleRound <= 6:
                extraShift += 1
            actionScroll(battleRound, extraShift)
            scrollUsed +=1

        elif battleOption == "5" and weaponThrown == 0 and battleRound == 0:
            throwWeapon()
            weaponThrown += 1
            
        elif battleOption == "0":
            break
            
        else:
           print("Not a valid option, please try again")
        
        
        input("Press Enter key to continue")
