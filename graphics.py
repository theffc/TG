import pygame


FPS=30
quitGame=False

pygame.init()
vidInfo = pygame.display.Info()
WIDTH = vidInfo.current_w
HEIGHT = vidInfo.current_h
RESOLUTION = (WIDTH, HEIGHT)

SCREEN = pygame.display.set_mode(RESOLUTION)#, pygame.FULLSCREEN)

pygame.event.set_blocked([pygame.USEREVENT, pygame.VIDEOEXPOSE, pygame.MOUSEMOTION, pygame.ACTIVEEVENT, pygame.KEYDOWN, pygame.KEYUP, pygame.VIDEORESIZE, pygame.JOYAXISMOTION, pygame.JOYBALLMOTION, pygame.JOYHATMOTION, pygame.JOYBUTTONUP, pygame.JOYBUTTONDOWN])

clock = pygame.time.Clock()


clique=0
disclique=0
while not quitGame:

	events = pygame.event.get([pygame.QUIT, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN])
	for event in events:
		if event.type == pygame.QUIT:
			quitGame=True
			break
		elif event.type == pygame.MOUSEBUTTONDOWN :
			clique+=1
			clock.tick_busy_loop(FPS/5)
			if pygame.event.get(pygame.MOUSEBUTTONDOWN):
				##graph.newV(pygame.mouse.get_pos())
				pygame.Surface.fill(SCREEN,(0,255,0))
			else:
				pygame.Surface.fill(SCREEN,(255,0,0))
		elif event.type == pygame.MOUSEBUTTONUP:
			disclique-=1

	pygame.display.update()
	print clique
	clique=0
	disclique=0
	##clock.tick(FPS)
	clock.tick_busy_loop(FPS)

pygame.quit()



