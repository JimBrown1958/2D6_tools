# actionRoom.py
import Dice as D

def roll_Exits():
    exitDiceRoll = D.roll_1D6()
    if exitDiceRoll == 1:
        return 0
    if exitDiceRoll == 2 or exitDiceRoll == 3:
        return 1
    if exitDiceRoll == 4 or exitDiceRoll == 5:
        return 2
    if exitDiceRoll == 6:
        return 3

def lockedDoor():    
    lockeddoorDice = D.roll_1D6()
    if lockeddoorDice == 6:
        print("All doors are locked")
        return
    if lockeddoorDice >= 1 and lockeddoorDice <= 3:
        print("All doors unlocked")
        return
    if lockeddoorDice >= 4 and lockeddoorDice <= 5:
        print("Metal doors are locked")
    if lockeddoorDice == 5:
        print("Reinforced doors are locked")

def createRoom():
    D.clear()
    
    x_dim = "0"
    y_dim = "0"
    room_size = 0
    
    print("Room creation")
    print("=============")
    print()
    x_dim = D.roll_1D6()
    y_dim = D.roll_1D6()
    

    # Check for a double roll less than 6 + 6
    if x_dim < 6:
        if x_dim == y_dim:
            # Got a double less than 6 + 6
            x_dim += D.roll_1D6()
            y_dim += D.roll_1D6()
    
    # Check for a corridor
    if x_dim == 1 or y_dim == 1:
        print("You have rolled a corridor,") 
        print("that is X:", x_dim, "Y:", y_dim)
        
        exitNumber = roll_Exits()
        if exitNumber > 0:
            print("There are a maximum of", roll_Exits(), "exits off this corridor")
            print("All exits are open archways")
            print()
        else:
            print("This is a dead end with no exits")
        
        input("Press Enter key to continue")
        return

    print("The room size is:")
    print("X:", x_dim, "Y:", y_dim)
    room_size = x_dim * y_dim
    print()
    print("The room type is Primary", D.roll_1D6(), "Secondary", D.roll_1D6())
    if room_size <= 6:
        print("Check the 'Small Room' table for this level")
    elif room_size >= 32:
        print("Check the 'Large Room' table for this level")
    else:
        print("Check the 'Level Room' table")
    print()
    exitNumber = roll_Exits()
    if exitNumber > 0:
        print("This room has a maximum of", exitNumber, "exits")
    print()
    if room_size <= 6:
        if exitNumber > 0:
            print("All exits are open archways")
    else:
        if exitNumber > 0:
            print("Check the room table for room type exits")
            print("")
            print("Door lock status:")
            lockedDoor()
        else:
            print("This is a dead end with no exits")

    print()
    input("Press Enter key to continue")
