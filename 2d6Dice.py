import Dice as D
import battleActions as bA
import actionRoom as aR

chooseRoll = ""

while chooseRoll != "0":
    D.print_page_header()
    print(f"\t\t\tMain Menu")
    print(f"\t\t\t=========")
    print()
    print(f"\t1: 1D3")
    print(f"\t2: 1D6")
    print(f"\t3: 2D6")
    print(f"\t4: D66")
    print(f"\t5: XDX, select the number of dice to be thrown and max number on dice")
    print(f"\t6: Battle Menu")
    print(f"\t7: Create Room")
    print()
    print()
    print(f"\t0: Quit")
    print()
    chooseRoll = input("\tSelect option for dice roll: ")

    if chooseRoll == "1":
        D.print_page_header()
        print("Rolling 1D3 ...")
        pd = D.roll_XDX(3)
        dice_face_diagram = D.generate_dice_faces_diagram([pd],"   1D3   ")
        print(f"\n{dice_face_diagram}")
        D.print_page_footer()
    elif chooseRoll == "2":
        D.print_page_header()
        print("Rolling 1D6 ...")
        pd = D.roll_XDX(6)
        dice_face_diagram = D.generate_dice_faces_diagram([pd],"   1D6   ")
        print(f"\n{dice_face_diagram}")
        D.print_page_footer()
    elif chooseRoll == "3":
        D.print_page_header()
        print("Rolling 2D6 ...")
        dice_total = 0
        current_dice_value = 0
        no_of_dice = 2
        max_dice = 6
        for i in range(no_of_dice):
            current_dice_value = D.roll_XDX(max_dice)
            print("Dice",i+1,":", current_dice_value)
            dice_total += current_dice_value
            dice_face_diagram = D.generate_dice_faces_diagram([current_dice_value],"         ")
            print(f"{dice_face_diagram}")
        print("The total of this 2D6 roll is", dice_total)
        D.print_page_footer()
    elif chooseRoll == "4":
        D.print_page_header()
        print("Rolling D66 ...")
        pd = D.roll_XDX(6)
        sd = D.roll_XDX(6)
        dice_face_diagram = D.generate_dice_faces_diagram([pd,sd]," Primary  Secondary")
        print(f"\n{dice_face_diagram}")
        D.print_page_footer()
    elif chooseRoll == "5":
        D.print_page_header()
        print(f"\t\tSelect dice to roll")
        print()
        dice_total = 0
        current_dice_value = 0
        no_of_dice = int(input("Enter the number of dice you want to throw? "))
        max_dice = int(input("How many sides do these dice have? "))
        for i in range(no_of_dice):
            current_dice_value = D.roll_XDX(max_dice)
            print("Dice",i+1,":", current_dice_value)
            dice_total += current_dice_value
        print("The total of all dice rolled is", dice_total)
        D.print_page_footer()
    elif chooseRoll == "6":
        bA.battleMenu()
    elif chooseRoll == "7":
        aR.createRoom()
    elif chooseRoll == "0":
        print("Bye")
        break
    else:
        print("Not a valid option")
