import pygame, sys, random
import pygame.event as GAME_EVENTS

pygame.init()

windowWidth = 500
windowHeight = 300

window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Pygame Keyboard!')

white = (255,255,255)
black = (0,0,0)
die1 = (100, 100, 100, 100)
die2 = (300, 100, 100, 100)

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

def quitGame():
	pygame.quit()
	sys.exit()

def clearDice():
	pygame.draw.rect(window, white, die1)
	pygame.draw.rect(window, white, die2)
	pygame.display.update()

while True:
	for event in GAME_EVENTS.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				quitGame()
			if event.key == pygame.K_r:
				clearDice()
				Firstdice = random.randint(1,6)
				Seconddice = random.randint(1,6)
				if Firstdice == 1:					
					dice1(die1)
				elif Firstdice == 2:
					dice2(die1)
				elif Firstdice == 3:					
					dice3(die1)
				elif Firstdice == 4:					
					dice4(die1)
				elif Firstdice == 5:					
					dice5(die1)
				elif Firstdice == 6:					
					dice6(die1)
				if Seconddice == 1:					
					dice1(die2)
				elif Seconddice == 2:					
					dice2(die2)
				elif Seconddice == 3:					
					dice3(die2)
				elif Seconddice == 4:					
					dice4(die2)
				elif Seconddice == 5:					
					dice5(die2)
				elif Seconddice == 6:					
					dice6(die2)
	pygame.display.update()