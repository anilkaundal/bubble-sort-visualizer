import sys
import pygame
from random import randint

# setting window size 
screen = pygame.display.set_mode((1200, 720))
height = [200, 50, 130, 90, 250, 61, 110,
		88, 33, 80, 70, 159, 180, 20]
# width of each bar
width = 70
# initial position
x = 40
y = 90
 

def show(height):
	for i in range(len(height)):
		pygame.draw.rect(screen, (255, 0, 0), (x + 80 * i, y, width, height[i]))

def part(screen, height):
	rect = pygame.Rect(0, 80, 1200, 10)
	color = 60, 60, 60
	pygame.draw.rect(screen, color, rect)
	text_color = (30,30,30)
	font = pygame.font.SysFont("comicsans", 30)
	info_1 = "PRESS 'ENTER' TO PERFORM SORTING."
	image = font.render(info_1, True, text_color)
	screen.blit(image, (40, 40))
	info_2 = font.render("ALGORITHM USED: BUBBLE SORT", 1, text_color)
	screen.blit(info_2, (820, 40))
	show(height)
	
def draw():
	pygame.init()
	# setting title to the window
	pygame.display.set_caption("Bubble Sort")
	img = pygame.image.load('screenshot\sort_icon.png')
	pygame.display.set_icon(img)
	bg_color = (230, 230, 230)
	# infinite loop
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					# start sorting using bubble sort technique
					for i in range(len(height) - 1):
						# after this iteration max element will come at last
						for j in range(len(height) - i - 1):
							# starting is greater then next element
							if height[j] > height[j + 1]:
								# save it in temporary variable
								# and swap them using temporary variable  
								t = height[j] 
								height[j] = height[j + 1] 
								height[j + 1] = t 
							screen.fill((230, 230, 230))
							part(screen, height)    
							show(height)
							# time delay 
							pygame.time.delay(100)
							# update the display
							pygame.display.update()  
				
		screen.fill(bg_color)
		part(screen, height) 
		pygame.display.flip()
draw()


