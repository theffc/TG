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

pygame.event.set_blocked([pygame.USEREVENT, pygame.VIDEOEXPOSE, pygame.MOUSEMOTION, pygame.ACTIVEEVENT, pygame.KEYDOWN, pygame.KEYUP, pygame.VIDEORESIZE, pygame.JOYAXISMOTION, pygame.JOYBALLMOTION, pygame.JOYHATMOTION, pygame.JOYBUTTONUP, pygame.JOYBUTTONDOWN])

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

		elif event.type == pygame.MOUSEBUTTONDOWN: #clicou
			local = Grafo.verificarClique(event.pos)
			clock.tick_busy_loop(FPS*0.1)
			if pygame.event.get(pygame.MOUSEBUTTONDOWN) and not isinstance(local, Vertice): # doubleclick
				Rect=pygame.draw.circle(SCREEN,(0,0,255),event.pos,RECT_SIZE, RECT_SIZE/10)
				Grafo.newV(Rect)
				Grafo.mostrarV()
				continue
		
			if not local: # clicou no vazio
				continue

			local.bSelecionado=True
			if pygame.mouse.get_pressed()[0]: # botao esquerdo do mouse continua pressionado
				disclique = pygame.event.get(MOUSEBUTTONUP)
				while not disclique:
					pygame.event.wait()
					disclique = pygame.event.get(MOUSEBUTTONUP)
					
				local2 = verificarClique(disclique.pos)
				if isinstance(local2, Vertice):
					# criar uma nova aresta
					pass

				else:
					# Mover o rect do vertice
					pass



		

	pygame.display.update()
	
	clique=0
	disclique=0
	clock.tick(FPS)

pygame.quit()



