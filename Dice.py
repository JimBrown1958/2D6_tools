# dice.py
import random as r
from os import system, name

DICE_ART = {
    1: (
        "┌──────┐",
        "│       │",
        "│   ●   │",
        "│       │",
        "└──────┘",
    ),
    2: (
        "┌──────┐",
        "│ ●     │",
        "│       │",
        "│     ● │",
        "└──────┘",
    ),
    3: (
        "┌──────┐",
        "│ ●     │",
        "│   ●   │",
        "│     ● │",
        "└──────┘",
    ),
    4: (
        "┌──────┐",
        "│ ●   ● │",
        "│       │",
        "│ ●   ● │",
        "└──────┘",
    ),
    5: (
        "┌──────┐",
        "│ ●   ● │",
        "│   ●   │",
        "│ ●   ● │",
        "└──────┘",
    ),
    6: (
        "┌──────┐",
        "│ ●   ● │",
        "│ ●   ● │",
        "│ ●   ● │",
        "└──────┘",
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

def diceRoll(lo, hi):
    return r.randint(lo,hi)
        
def roll_1D3():
    return diceRoll(1,3)
            
def roll_1D6():
    return diceRoll(1,6)
    
def roll_2D6():
    return diceRoll(2,12)

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
