import pygame
from tg import *



FPS=50
quitGame=False

pygame.init()
vidInfo = pygame.display.Info()

WIDTH = vidInfo.current_w
HEIGHT = vidInfo.current_h
RESOLUTION = (WIDTH, HEIGHT)
RECT_SIZE = int(WIDTH * 0.02)

SCREEN = pygame.display.set_mode(RESOLUTION)#, pygame.FULLSCREEN)

pygame.event.set_blocked([pygame.USEREVENT, pygame.VIDEOEXPOSE, pygame.MOUSEMOTION, pygame.ACTIVEEVENT, pygame.KEYDOWN, pygame.KEYUP, pygame.VIDEORESIZE, pygame.JOYAXISMOTION, pygame.JOYBALLMOTION, pygame.JOYHATMOTION, pygame.JOYBUTTONUP, pygame.JOYBUTTONDOWN, pygame.MOUSEBUTTONUP])

clock = pygame.time.Clock()
pygame.mouse.set_visible(1)



clique=0
disclique=0
while not quitGame:

	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			quitGame=True
			break
		elif event.type == pygame.MOUSEBUTTONDOWN :
			clique+=1
			clock.tick_busy_loop(FPS*0.1)
			if pygame.event.get(pygame.MOUSEBUTTONDOWN) and not Grafo.colidiuXY(event.pos):
				# Rect = pygame.Rect(event.pos[0]-RECT_SIZE/2, event.pos[1]-RECT_SIZE/2, RECT_SIZE, RECT_SIZE)
				Rect=pygame.draw.circle(SCREEN,(0,0,255),event.pos,RECT_SIZE, RECT_SIZE/10)
				Grafo.newV(Rect)
				#pygame.Surface.fill(SCREEN,(0,255,0))
				Grafo.mostrarV()
			else:
				#pygame.Surface.fill(SCREEN,(255,0,0))
				pass
		elif event.type == pygame.MOUSEBUTTONUP:
			disclique-=1

	pygame.display.update()
	
	clique=0
	disclique=0
	clock.tick(FPS)

pygame.quit()



