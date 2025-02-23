import pygame, sys, random
import pygame.event as GAME_EVENTS
import Dice as D
import battleActions as bA
import actionRoom as aR

pygame.init()

windowWidth = 500
windowHeight = 300

window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Pygame Keyboard!')

white = (255,255,255)
black = (0,0,0)
die1 = (100, 100, 100, 100)
die2 = (300, 100, 100, 100)

game_state = "main_menu"

def dice6(cur_die):
	pygame.draw.circle(window, black,(cur_die[0] + 20,cur_die[1] + 20),10,0)
	pygame.draw.circle(window, black,(cur_die[0] + 80,cur_die[1] + 20),10,0)
	pygame.draw.circle(window, black,(cur_die[0] + 20,cur_die[1] + 50),10,0)
	pygame.draw.circle(window, black,(cur_die[0] + 80,cur_die[1] + 50),10,0)
	pygame.draw.circle(window, black,(cur_die[0] + 20,cur_die[1] + 80),10,0)
	pygame.draw.circle(window, black,(cur_die[0] + 80,cur_die[1] + 80),10,0)

def dice5(cur_die):
	pygame.draw.circle(window, black,(cur_die[0] + 20,cur_die[1] + 20),10,0)
	pygame.draw.circle(window, black,(cur_die[0] + 80,cur_die[1] + 20),10,0)
	pygame.draw.circle(window, black,(cur_die[0] + 50,cur_die[1] + 50),10,0)
	pygame.draw.circle(window, black,(cur_die[0] + 20,cur_die[1] + 80),10,0)
	pygame.draw.circle(window, black,(cur_die[0] + 80,cur_die[1] + 80),10,0)
	
def dice4(cur_die):
	pygame.draw.circle(window, black,(cur_die[0] + 20,cur_die[1] + 20),10,0)
	pygame.draw.circle(window, black,(cur_die[0] + 80,cur_die[1] + 20),10,0)
	pygame.draw.circle(window, black,(cur_die[0] + 20,cur_die[1] + 80),10,0)
	pygame.draw.circle(window, black,(cur_die[0] + 80,cur_die[1] + 80),10,0)

def dice3(cur_die):
	pygame.draw.circle(window, black,(cur_die[0] + 20,cur_die[1] + 20),10,0)
	pygame.draw.circle(window, black,(cur_die[0] + 50,cur_die[1] + 50),10,0)
	pygame.draw.circle(window, black,(cur_die[0] + 80,cur_die[1] + 80),10,0)

def dice2(cur_die):
	pygame.draw.circle(window, black,(cur_die[0] + 20,cur_die[1] + 50),10,0)
	pygame.draw.circle(window, black,(cur_die[0] + 80,cur_die[1] + 50),10,0)

def dice1(cur_die):
	pygame.draw.circle(window, black,(cur_die[0] + 50,cur_die[1] + 50),10,0)

def draw_main_menu():
    fontSize = 18
    window.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', fontSize)
    title1 = font.render('2D6 Dungeon Tools', True, (255, 255, 255))
    title2 = font.render('Main Menu', True, (255, 255, 255))
    title3 = font.render('=========', True, (255, 255, 255))
    start_button1 = font.render('1: 1D6', True, (255, 255, 255))
    start_button2 = font.render('2: 2D6', True, (255, 255, 255))
    start_button3 = font.render('3: 1D3', True, (255, 255, 255))
    start_button4 = font.render('4: D66', True, (255, 255, 255))
    start_button5 = font.render('5: XDX, select the number of dice to be thrown and max number on dice', True, (255, 255, 255))
    start_button6 = font.render('6: Create room', True, (255, 255, 255))
    start_button7 = font.render('7: Battle menu', True, (255, 255, 255))
    start_button0 = font.render('0 or escape: Quit', True, (255, 255, 255))
    info_button0 = font.render('Select option for dice roll:', True, (255, 255, 255))
    window.blit(title1, (windowWidth/2 - title1.get_width()/2, fontSize * 1))
    window.blit(title2, (windowWidth/2 - title2.get_width()/2, fontSize *2))
    window.blit(title3, (windowWidth/2 - title3.get_width()/2, fontSize *3))
    window.blit(start_button1, (20, fontSize * 5))
    window.blit(start_button2, (20, fontSize * 6))
    window.blit(start_button3, (20, fontSize * 7))
    window.blit(start_button4, (20, fontSize * 8))
    window.blit(start_button5, (20, fontSize * 9))
    window.blit(start_button6, (20, fontSize * 10))
    window.blit(start_button7, (20, fontSize * 11))
    window.blit(start_button0, (20, fontSize * 12))
    window.blit(info_button0, (windowWidth/2 - info_button0.get_width()/2, 250))
    pygame.display.update()

def quitGame():
	pygame.quit()
	sys.exit()

def clearDice():
    window.fill((0, 0, 0))
    pygame.draw.rect(window, white, die1)
    pygame.draw.rect(window, white, die2)
    pygame.display.update()

while True:
    if game_state == "main_menu":
       draw_main_menu()
    for event in GAME_EVENTS.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_0:
                quitGame()
            if event.key == pygame.K_2:
                clearDice()
                font = pygame.font.SysFont('arial', 18)
                title1 = font.render("Rolling 2D6 ...", True, (255, 255, 255))
                window.blit(title1, (windowWidth/2 - title1.get_width()/2, 20))
                game_state = "game"
                
                Firstdice = random.randint(1,6)
                Seconddice = random.randint(1,6)
                print("dice1: ", Firstdice, "dice2: ", Seconddice)
                match Firstdice:
                    case "1":					
                        dice1(die1)
                    case "2":
                        dice2(die1)
                    case "3":					
                        dice3(die1)
                    case "4":					
                        dice4(die1)
                    case "5":					
                        dice5(die1)
                    case "6":					
                        dice6(die1)
                match Seconddice:
                    case "1":					
                        dice1(die2)
                    case "2":					
                        dice2(die2)
                    case "3":					
                        dice3(die2)
                    case "4":					
                        dice4(die2)
                    case "5":					
                        dice5(die2)
                    case "6":					
                        dice6(die2)
                dice_total = Firstdice + Seconddice
                totalDice_string = "The total of this 2D6 roll is " + str(dice_total)
                title1 = font.render(totalDice_string, True, (255, 255, 255))
                window.blit(title1, (windowWidth/2 - title1.get_width()/2, 230))               
            if event.key == pygame.K_m:
                game_state = "main_menu"
                
                
    pygame.display.update()