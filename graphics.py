import pygame

FPS=30
quitGame=False

pygame.init()
vidInfo = pygame.display.Info()
WIDTH = vidInfo.current_w
HEIGHT = vidInfo.current_h
RESOLUTION = (WIDTH, HEIGHT)

SCREEN = pygame.display.set_mode(RESOLUTION, pygame.FULLSCREEN)

pygame.event.set_blocked([pygame.JOYAXISMOTION, pygame.JOYBALLMOTION, pygame.JOYHATMOTION, pygame.JOYBUTTONUP, pygame.JOYBUTTONDOWN])

clock = pygame.time.Clock()


click=0
disclick=0
while not quitGame:

	events = pygame.event.get([pygame.QUIT, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN])
	for x in events:
		if x.type == pygame.QUIT:
			quitGame=True
			break
		elif x.type == pygame.MOUSEBUTTONDOWN :
			click+=1
			print x
			pygame.Surface.fill(SCREEN,(255,0,0))
			continue
			if click>=2 and clock.tick()<FPS:
				##graph.newV(pygame.mouse.get_pos())
				pygame.Surface.fill(SCREEN, (0,255,0))
				click=0
		elif x.type == pygame.MOUSEBUTTONUP:
			disclick-=1

	pygame.display.update()

	click=0
	disclick=0
	clock.tick(FPS)

pygame.quit()



