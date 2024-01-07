# actionRoom.py
import Dice as D

def roll_Exits():
    exitDiceRoll = D.diceRoll(6)
    dice_face_diagram = D.generate_dice_faces_diagram([exitDiceRoll],"Exit Roll")
    print(f"\n{dice_face_diagram}")
    if exitDiceRoll == 1:
        return 0
    if exitDiceRoll == 2 or exitDiceRoll == 3:
        return 1
    if exitDiceRoll == 4 or exitDiceRoll == 5:
        return 2
    if exitDiceRoll == 6:
        return 3

def lockedDoor():
    lockeddoorDice = D.diceRoll(6)
    dice_face_diagram = D.generate_dice_faces_diagram([lockeddoorDice],"Locked status")
    print(f"\n{dice_face_diagram}")

    if lockeddoorDice == 6:
        print("Door is locked")
        return
    if lockeddoorDice >= 1 and lockeddoorDice <= 3:
        print("Door is unlocked")
        return
    if lockeddoorDice >= 4 and lockeddoorDice <= 5:
        print("Metal door is locked")
    if lockeddoorDice == 5:
        print("Reinforced door is locked")

def createRoom():
    x_dim = "0"
    y_dim = "0"
    room_size = 0
    
    x_dim = D.diceRoll(6)
    y_dim = D.diceRoll(6)
    
    D.print_page_header()    
    print(f"\t\t\tRoom creation")
    print(f"\t\t\t=============")
    print()
    print("Room Size:")
    dice_face_diagram = D.generate_dice_faces_diagram([x_dim,y_dim],"    X         Y    ")
    print(f"{dice_face_diagram}")
   
   # Check for a double roll less than 6 + 6
    if x_dim < 6:
        if x_dim == y_dim:
            # Got a double less than 6 + 6
            x_dim2 = D.diceRoll(6)
            y_dim2 = D.diceRoll(6)
            x_dim += x_dim2
            y_dim += y_dim2
            print("You rolled a double, so dice rolled again and added to previous roll")
            dice_face_diagram = D.generate_dice_faces_diagram([x_dim2,y_dim2],"    X         Y     ")
            print(f"{dice_face_diagram}")
    
    # Check for a corridor
    if x_dim == 1 or y_dim == 1:
        print("You have rolled a corridor,") 
        print(f"that is X: {x_dim} wide and Y: {y_dim} deep")
        
        exitNumber = roll_Exits()
        if exitNumber > 0:
            print(f"There are a maximum of {exitNumber} exits off this corridor")
            print("All exits are open archways")
            print()
        else:
            print("This is a dead end with no exits")
        D.print_page_footer()
        return
    print(f"The room is: X: {x_dim} wide by Y: {y_dim} deep")
    print()
    print()
    room_size = x_dim * y_dim
    print("The room type is:")
    pd = D.diceRoll(6)
    sd = D.diceRoll(6)
    room_type_entry = pd + sd
    if room_size <= 6:
        dice_face_diagram = D.generate_dice_faces_diagram([pd,sd],"                   ")
        print(f"{dice_face_diagram}")
        print(f"Check entry {room_type_entry} in the 'Small Room' table for this level")
    elif room_size >= 32:
        dice_face_diagram = D.generate_dice_faces_diagram([pd,sd],"                   ")
        print(f"{dice_face_diagram}")
        print(f"Check entry {room_type_entry} in the 'Large Room' table for this level")
    else:
        dice_face_diagram = D.generate_dice_faces_diagram([pd,sd]," Primary  Secondary")
        print(f"{dice_face_diagram}")
        print("Check the 'Level Room' table")
    print()
    exitNumber = roll_Exits()
    if exitNumber > 0:
        print(f"This room has a maximum of {exitNumber} exits")
        print("")
    if room_size <= 6:
        if exitNumber > 0:
            print("All exits are open archways")
    else:
        if exitNumber > 0:
            print("Check the room table for room type exits.")
            print("If room type exit is random, check exit type table for:")
            print("")
            dice_face_diagram = D.generate_dice_faces_diagram([pd,sd]," Primary  Secondary")
            print(f"{dice_face_diagram}")            
            print("")
            for locked_exit in range(1,exitNumber):
                print(f"Door {locked_exit} status:")
                lockedDoor()
        else:
            print("This is a dead end with no exits")

    print()
    D.print_page_footer()