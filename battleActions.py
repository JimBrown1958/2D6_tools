# battleActions.py
import Dice as D

def inCombatDice():
    chooseAttackDice = ""
    while chooseAttackDice != "0":
        print(f"Throw dice for a successfull hit")
        print(f"\t1: 1D6 Combat Damage")
        print(f"\t2: XDX Combat Damage")
        print(f"\t0: End turn")
        print()
        chooseAttackDice = input("Select option for damage roll: ")
        match chooseAttackDice:
            case "1":
                D.d1x6Throw()
            case "2":
                D.multiThrow()
            case "0":
                print("Combat turn ended")
                break
            case _:
                print("Not a valid option")
            
def attackHero(battleRound, extraShift):
    pd = D.diceRoll(6)
    sd = D.diceRoll(6)
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
    inCombatDice()
    print("If enemy is still alive, they attack next")

def attackEnemy(battleRound, extraShift):
    pd = D.diceRoll(6)
    sd = D.diceRoll(6)
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
        print("follow the Prime Attack instructions on enemy card")
    inCombatDice()
        

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
    pd = D.diceRoll(6)
    sd = D.diceRoll(6)
    dice_face_diagram = D.generate_dice_faces_diagram([pd,sd]," Primary  Secondary")
    print(f"\n{dice_face_diagram}")
    print()
    if pd == sd:
        print("Your roll was successfull however check to see if this scroll has a 'Dispel Double' in scroll table")
        print()    
        if pd == 1:
            print("... but unfortunately the scroll will only do half damage, if it is a combat scroll")
        if pd == 6:
            print("... but luckily this scroll will do double damage, if it is a combat scroll") 
    print()
    print("Your scroll disappears into dust")
    print("You gain 5xp")
    print()
    print("If enemy still alive, they attack next")
    
def throwWeapon():
    D.print_page_header()
    print("Throw weapon ...",)
    pd = D.diceRoll(6)
    sd = D.diceRoll(6)    
    dice_face_diagram = D.generate_dice_faces_diagram([pd,sd]," Primary  Secondary")
    print(f"\n{dice_face_diagram}")
    print("On a successful throw the following apply:")
    print("Throwing Axes do 6 damage")
    print("Throwing knives do 4 damage")
    print("Throwing darts do 2 damage")
    lostWeapon = D.diceRoll(6)
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
            print(f"\t4: Use Magic Scroll. Uses up 1st combat round")
        if weaponThrown == 0 and battleRound == 0:
            print(f"\t5: Throw weapon. Does not use up 1st combat round")
        print()
        print(f"\t0: End Battle")
        print()
        battleOption = input("\tSelect battle option: ")
        
        # Process option selected
        match battleOption:
            case "1":
                battleRound += 1
                if battleRound >= 4 and battleRound <= 6:
                    extraShift += 1
                attackHero(battleRound, extraShift)

            case "2":
                attackEnemy(battleRound, extraShift)
            
            case "3":
                battleRound += 1
                if battleRound >= 4 and battleRound <= 6:
                    extraShift += 1
                actionPotion(battleRound, extraShift)
                potionUsed += 1
                D.print_page_footer()

            case "4":
                if scrollUsed == 0 and battleRound == 0:
                    battleRound += 1
                    if battleRound >= 4 and battleRound <= 6:
                        extraShift += 1
                    actionScroll(battleRound, extraShift)
                    scrollUsed +=1
                    D.print_page_footer()

            case "5":
                if weaponThrown == 0 and battleRound == 0:
                    throwWeapon()
                    weaponThrown += 1
                    D.print_page_footer()
            
            case "0":
                break
            
            case _:
               print("Not a valid option, please try again")
