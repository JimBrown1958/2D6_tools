import Dice as D
import battleActions as bA
import actionRoom as aR

chooseRoll = ""

while chooseRoll != "0":
    D.print_page_header()
    print(f"\t\t\tMain Menu")
    print(f"\t\t\t=========")
    print()
    print(f"\t1: 1D6")
    print(f"\t2: 2D6")
    print(f"\t3: 1D3")
    print(f"\t4: D66")
    print(f"\t5: XDX, select the number of dice to be thrown and max number on dice")
    print(f"\t6: Create Room")
    print(f"\t7: Start Battle!")
    print()
    print()
    print(f"\t0: Quit")
    print()
    chooseRoll = input("\tSelect option for dice roll: ")

    match chooseRoll:
        case "1":
            D.print_page_header()
            D.d1x6Throw()
            D.print_page_footer()
        case "2":
            D.print_page_header()
            D.d2x6Throw()
            D.print_page_footer()
        case "3":
            D.print_page_header()
            D.d1x3Throw()
            D.print_page_footer()
        case "4":
            D.print_page_header()
            D.d66Throw()
            D.print_page_footer()
        case "5":
            D.print_page_header()
            D.multiThrow()
            D.print_page_footer()
        case "6":
            aR.createRoom()
        case "7":
            bA.battleMenu()
        case "0":
            print("Bye")
            break
        case _:
            print("Not a valid option")
            