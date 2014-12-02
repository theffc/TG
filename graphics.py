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

		elif event.type == pygame.MOUSEBUTTONDOWN: #clicou
			local = Grafo.verificarClique(event.pos)
			Grafo.selecionado = local
			print local
			clock.tick_busy_loop(FPS*0.1)
			localEhUmVertice = isinstance(local, Vertice)

			if pygame.event.get(pygame.MOUSEBUTTONDOWN) and not localEhUmVertice: # doubleclick
				Rect=pygame.draw.circle(SCREEN,(0,100,255),event.pos,RECT_SIZE, RECT_SIZE/10)
				Grafo.newV(Rect)
				Grafo.mostrarV()
				continue
		
			elif not local: # clicou no vazio
				continue

			elif localEhUmVertice and pygame.mouse.get_pressed()[0] : # botao esquerdo do mouse continua pressionado
				disclique = pygame.event.get(pygame.MOUSEBUTTONUP)
				while not disclique:
					pygame.event.set_allowed(None)
					pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
					disclique=pygame.event.wait()
					print disclique
					
				local2 = Grafo.verificarClique(disclique.pos)
				print local2
				if isinstance(local2, Vertice):
					aresta = Grafo.newA(local, local2)
					print Grafo.iTotalArestas
					pygame.draw.line(SCREEN, (255,0,255), local.tCenter, local2.tCenter )	# desclicou num vertice para criar uma aresta
					
				else:
					# Mover o rect do vertice
					SCREEN.fill((0,0,0), local.Rect)
					local.Rect = pygame.draw.circle(SCREEN,(0,100,255),disclique.pos,RECT_SIZE, RECT_SIZE/10)
					local.tCenter = local.Rect.center
					local.iMudouPos = len(local.setAdjs)


			elif True: # verificar se o usuario apertou o delete
				pass

		pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN])

	
	pygame.display.update()
	clock.tick(FPS)


pygame.quit()



