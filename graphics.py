import pygame
from tg import *



FPS=50
quitGame=False
BLUE = (0,100,255)
PINK = (255,0,255)


pygame.init()
vidInfo = pygame.display.Info()

WIDTH = vidInfo.current_w
HEIGHT = vidInfo.current_h
RESOLUTION = (WIDTH, HEIGHT)
RECT_SIZE = int(WIDTH * 0.02)
LINE = int(WIDTH * 0.005)

SCREEN = pygame.display.set_mode(RESOLUTION)#, pygame.FULLSCREEN)

pygame.event.set_blocked([pygame.USEREVENT, pygame.VIDEOEXPOSE, pygame.MOUSEMOTION, pygame.ACTIVEEVENT, pygame.VIDEORESIZE, pygame.JOYAXISMOTION, pygame.JOYBALLMOTION, pygame.JOYHATMOTION, pygame.JOYBUTTONUP, pygame.JOYBUTTONDOWN])
#pygame.event.set_allowed(None)


clock = pygame.time.Clock()
pygame.mouse.set_visible(1)


while not quitGame:
	
	events = pygame.event.get()
	for event in events:

		if event.type == pygame.QUIT:
			quitGame=True
			break

		#1 clicou
		elif event.type == pygame.MOUSEBUTTONDOWN: 
			local = Grafo.verificarClique(event.pos)
			print local
			clock.tick_busy_loop(FPS*0.1)
			localEhUmVertice = isinstance(local, Vertice)

			#2 doubleclick
			if pygame.event.get(pygame.MOUSEBUTTONDOWN) and not localEhUmVertice: 
				Rect=pygame.draw.circle(SCREEN,BLUE,event.pos,RECT_SIZE, RECT_SIZE/10)
				Grafo.newV(Rect)
				Grafo.mostrarV()
				continue
		
			#2 clicou no vazio
			elif not local:
				continue


			#2 botao esquerdo do mouse continua pressionado
			elif localEhUmVertice and pygame.mouse.get_pressed()[0] : 
				
				#3 pegar o disclique
				disclique = pygame.event.get(pygame.MOUSEBUTTONUP)
				while not disclique:
					pygame.event.set_allowed(None)
					pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
					disclique=pygame.event.wait()
					print disclique
				local2 = Grafo.verificarClique(disclique.pos)
				print local2

				#3 desclicou num vertice para criar uma aresta
				if isinstance(local2, Vertice):
					aresta = Grafo.newA(local, local2)
					print Grafo.iTotalArestas
					pygame.draw.line(SCREEN, PINK, local.Rect.center, local2.Rect.center )
				
				#3 desclicou no vazio-> Mover o rect do vertice
				else:
					SCREEN.fill((0,0,0), local.Rect)
					local.Rect = pygame.draw.circle(SCREEN, BLUE,disclique.pos,RECT_SIZE, LINE)
					local.iMudouPos = len(local.setAdjs)
					local.bMudouPos = True

			#2 usuario apertou o delete
			elif True: 
				pass

		#1 pygame pega apenas eventos interesssantes
		pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN])

	#for end
	
	pygame.display.update()
	clock.tick(FPS)

#while end

pygame.quit()



