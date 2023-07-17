# battleActions.py
import Dice as D

def attackHero(battleRound, extraShift):
    pd = D.roll_XDX(6)
    sd = D.roll_XDX(6)
    D.print_page_header()
    print(f"\tCombat round:", battleRound, "Additional shift:", extraShift)
    print()
    print("You attack with:")
    dice_face_diagram = D.generate_dice_faces_diagram([pd,sd]," Primary  Secondary")
    print(f"\n{dice_face_diagram}")
    print()
    if battleRound >= 7:
        print("Ignore all movement interupts for enemy")
        print()
    if pd == 1 and sd == 1:
        print("You made a mishap roll and completely miss the enemy")
        print()
    if pd == 6 and sd == 6:
        print("You made a Prime attack and can use any attack and not miss")
        print()
    print("If enemy is still alive, they attack next")

def attackEnemy(battleRound, extraShift):
    pd = D.roll_XDX(6)
    sd = D.roll_XDX(6)
    D.print_page_header()
    print(f"\tCombat round:", battleRound, "Additional shift:", extraShift)
    print()
    print("Enemy attacks with")
    dice_face_diagram = D.generate_dice_faces_diagram([pd,sd]," Primary  Secondary")
    print(f"\n{dice_face_diagram}")
    if pd == 1 and sd == 1:
        print("Your enemy made a mishap roll and completely missed you")
    if pd == 6 and sd == 6:
        print("Your enemy made a Prime attack,")
        print("follow the Prime Attck instructions on enemy card")

def actionPotion(battleRound, extraShift):
    D.print_page_header()
    print(f"\tCombat round:", battleRound, "Additional shift:", extraShift)
    print()
    if battleRound >= 7:
        print()
        print("Ignore all movement interupts for enemy")
        print()
    print("You quaff the Magic Potion ...")
    print("You have consumed the potion")
    print()
    print("If enemy still alive, they attack next")
    
def actionScroll(battleRound, extraShift):
    D.print_page_header()
    print(f"\tCombat round:", battleRound, "Additional shift:", extraShift)
    print()
    if battleRound >= 7:
        print()
        print("Ignore all movement interupts for enemy")
    print("You read the magic scroll ...")
    pd = D.roll_XDX(6)
    sd = D.roll_XDX(6)
    dice_face_diagram = D.generate_dice_faces_diagram([pd,sd]," Primary  Secondary")
    print(f"\n{dice_face_diagram}")
    print()
    print("Your scroll disappears into dust")
    print("You gain 5xp")
    print()
    print("If enemy still alive, they attack next")
    
def throwWeapon():
    D.print_page_header()
    print("Throw weapon ...",)
    pd = D.roll_XDX(6)
    sd = D.roll_XDX(6)    
    dice_face_diagram = D.generate_dice_faces_diagram([pd,sd]," Primary  Secondary")
    print(f"\n{dice_face_diagram}")
    lostWeapon = D.roll_XDX(6)
    dice_face_diagram = D.generate_dice_faces_diagram([lostWeapon],"Retrieve weapon?")
    print(f"\n{dice_face_diagram}")
    if lostWeapon >= 1 and lostWeapon <= 3:
        print("Your weapon flies off into the dungeon and is lost")
    else:
        print("You successfully retrieve your weapon from the ground")
    print()
    print("If the enemy is still alive, you can now engage them in combat")


def battleMenu():
    battleRound = 0
    extraShift = 0
    battleOption = ""
    potionUsed = 0
    scrollUsed = 0
    weaponThrown = 0
    
    while True:
        D.print_page_header()
        # Print menu ang get option
        print(f"\t\t\tBattle Menu")
        print(f"\t\t\t===========")
        print()
        print(f"\tCombat round:", battleRound, "Additional shift:", extraShift)
        print()
        print(f"\t1: Roll for Hero attack (this starts a new round)")
        print(f"\t2: Roll for Enemy attack")
        print(f"\t3: Quaff Magic potion")
        if scrollUsed == 0 and battleRound == 0:
            print(f"\t4: Use Magic Scroll, only available when 'Combat round' is 0. Uses up 1st combat round")
        if weaponThrown == 0 and battleRound == 0:
            print(f"\t5: Throw weapon, only available when 'Combat round' is 0. Does not use up a combat round")
        print()
        print(f"\t0: return to top menu")
        print()
        battleOption = input("\tSelect battle option: ")
        
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
        
        
        D.print_page_footer()