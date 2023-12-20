# dice.py
import random as r
from os import system, name

DICE_ART = {
    1: (
        "┌───────┐",
        "│       │",
        "│   ●   │",
        "│       │",
        "└───────┘",
    ),
    2: (
        "┌───────┐",
        "│ ●     │",
        "│       │",
        "│     ● │",
        "└───────┘",
    ),
    3: (
        "┌───────┐",
        "│ ●     │",
        "│   ●   │",
        "│     ● │",
        "└───────┘",
    ),
    4: (
        "┌───────┐",
        "│ ●   ● │",
        "│       │",
        "│ ●   ● │",
        "└───────┘",
    ),
    5: (
        "┌───────┐",
        "│ ●   ● │",
        "│   ●   │",
        "│ ●   ● │",
        "└───────┘",
    ),
    6: (
        "┌───────┐",
        "│ ●   ● │",
        "│ ●   ● │",
        "│ ●   ● │",
        "└───────┘",
    ),
}
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "


def generate_dice_faces_diagram(dice_values, dice_text):
    # Generate a list of dice faces from DICE_ART
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])

    # Generate a list containing the dice faces rows
    dice_faces_rows = []
    for row_idx in range(DIE_HEIGHT):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)

    # Generate header with the passed text centered
    width = len(dice_faces_rows[0])
    diagram_header = dice_text.center(width, "~")

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram

def diceRoll(hi):
    return r.randint(1,hi)
           
def d1x6Throw():
    print("Rolling 1D6 ...")
    pd = diceRoll(6)
    dice_face_diagram = generate_dice_faces_diagram([pd],"   1D6   ")
    print(f"\n{dice_face_diagram}")
    
def d2x6Throw():
    print("Rolling 2D6 ...")
    dice_total = 0
    current_dice_value = 0
    no_of_dice = 2
    max_dice = 6
    for i in range(no_of_dice):
        current_dice_value = diceRoll(max_dice)
        print(f"Dice {i+1}: {current_dice_value}")
        dice_total += current_dice_value
        dice_face_diagram = generate_dice_faces_diagram([current_dice_value],"         ")
        print(f"{dice_face_diagram}")
    print(f"The total of this 2D6 roll is {dice_total}")
    
def d1x3Throw():
    print("Rolling 1D3 ...")
    pd = diceRoll(3)
    dice_face_diagram = generate_dice_faces_diagram([pd],"   1D3   ")
    print(f"\n{dice_face_diagram}")
    
def d66Throw():
    print("Rolling D66 ...")
    pd = diceRoll(6)
    sd = diceRoll(6)
    dice_face_diagram = generate_dice_faces_diagram([pd,sd]," Primary  Secondary")
    print(f"\n{dice_face_diagram}")
    
def multiThrow():
    print(f"\t\tSelect dice to roll")
    print()
    dice_total = 0
    current_dice_value = 0
    no_of_dice = int(input("Enter the number of dice you want to throw? "))
    max_dice = int(input("How many sides do these dice have? "))
    for i in range(no_of_dice):
        current_dice_value = diceRoll(max_dice)
        print(f"Dice {i+1}: {current_dice_value}")
        dice_total += current_dice_value
    print(f"The total of all dice rolled is {dice_total}")

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def print_page_header():
    clear()
    print(f"\t\t2D6 Dungeon Tools")
    print()
    
def print_page_footer():
    print()
    input("Press Enter key to continue")

