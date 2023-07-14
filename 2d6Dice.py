import Dice as D
import battleActions as bA
import actionRoom as aR

chooseRoll = ""

while chooseRoll != "0":
    D.clear()
    print("Main Menu")
    print()
    print("Select option for dice roll:")
    print("1: 1D3")
    print("2: 1D6")
    print("3: 2D6")
    print("4: D66")
    print("5: Battle Menu")
    print("6: Create Room")
    print()
    print()
    print("0: Quit")
    print()
    chooseRoll = input("? ")

    if chooseRoll == "1":
        print("Rolling 1D3 ...")
        pd = D.roll_1D3()
        dice_face_diagram = D.generate_dice_faces_diagram([pd],"   1D3   ")
        print(f"\n{dice_face_diagram}")
        input("Press Enter key to continue")
    elif chooseRoll == "2":
        print("Rolling 1D6 ...")
        pd = D.roll_1D6()
        dice_face_diagram = D.generate_dice_faces_diagram([pd],"   1D6   ")
        print(f"\n{dice_face_diagram}")
        input("Press Enter key to continue")
    elif chooseRoll == "3":
        print("Rolling 2D6 ...")
        print("You rolled ", D.roll_2D6())
        input("Press Enter key to continue")
    elif chooseRoll == "4":
        print("Rolling D66 ...")
        pd = D.roll_1D6()
        sd = D.roll_1D6()
        dice_face_diagram = D.generate_dice_faces_diagram([pd,sd]," Primary   Secondary")
        print(f"\n{dice_face_diagram}")
        input("Press Enter key to continue")
    elif chooseRoll == "5":
        bA.battleMenu()
    elif chooseRoll == "6":
        aR.createRoom()
    elif chooseRoll == "0":
        print("Bye")
        break
    else:
        print("Not a valid option")
