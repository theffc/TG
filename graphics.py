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
			localEhUmVertice = isinstance(local, Vertice)

			if pygame.event.get(pygame.MOUSEBUTTONDOWN) and not localEhUmVertice: # doubleclick
				Rect=pygame.draw.circle(SCREEN,(0,0,255),event.pos,RECT_SIZE, RECT_SIZE/10)
				Grafo.newV(Rect)
				Grafo.mostrarV()
				continue
		
			elif not local: # clicou no vazio
				continue

			Grafo.selecionado = local
			if pygame.mouse.get_pressed()[0] and localEhUmVertice: # botao esquerdo do mouse continua pressionado
				disclique = pygame.event.get(MOUSEBUTTONUP)
				while not disclique:
					pygame.event.wait()
					disclique = pygame.event.get(MOUSEBUTTONUP)
					
				local2 = verificarClique(disclique.pos)
				if isinstance(local2, Vertice):
					Grafo.newA(loacal1, local2)
					
				else:
					# Mover o rect do vertice
					pass


			if : # verificar se o usuário apertou o delete
				pass


		

	pygame.display.update()
	
	clique=0
	disclique=0
	clock.tick(FPS)

pygame.quit()



