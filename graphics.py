import pygame
from tg import *

FPS=50
quitGame=False
BLUE = (10,100,255)
PINK = (255,0,255)
BLACK = (25,25,25)
GREEN = (0,255,100)
GRAY = (100,100,100)

pygame.init()
vidInfo = pygame.display.Info()

WIDTH = vidInfo.current_w -200
HEIGHT = vidInfo.current_h -80
RESOLUTION = (WIDTH, HEIGHT)
RECT_SIZE = int(WIDTH * 0.02)
CIRCLE = int(WIDTH * 0.0025)
LINE = int(WIDTH * 0.002)

SCREEN = pygame.display.set_mode(RESOLUTION, pygame.RESIZABLE)#, pygame.FULLSCREEN)

pygame.event.set_blocked([pygame.USEREVENT, pygame.VIDEOEXPOSE, pygame.MOUSEMOTION, pygame.ACTIVEEVENT, pygame.VIDEORESIZE, pygame.JOYAXISMOTION, pygame.JOYBALLMOTION, pygame.JOYHATMOTION, pygame.JOYBUTTONUP, pygame.JOYBUTTONDOWN])
#pygame.event.set_allowed(None)

houveMudancas = True
clock = pygame.time.Clock()
pygame.mouse.set_visible(1)

# desenha todas as coisas na tela
def desenhar(Surf):
	Surf.fill(BLACK)

	if Grafo.antigoRect:
		pygame.draw.circle(Surf, GRAY, Grafo.antigoRect.center, RECT_SIZE, CIRCLE)

	for v in Grafo.lVertices:
		v.Rect = pygame.draw.circle(Surf,BLUE,v.Rect.center,RECT_SIZE, CIRCLE)

	for a in Grafo.lArestas:
		a.Rect = pygame.draw.line(Surf, PINK, a.t[0].Rect.center, a.t[1].Rect.center, LINE)

	if Grafo.selectedV:
		Grafo.selectedV.Rect = pygame.draw.circle(Surf,GREEN,Grafo.selectedV.Rect.center,RECT_SIZE, CIRCLE)

	if Grafo.selectedA:
		Grafo.selectedA.Rect = pygame.draw.line(Surf,GREEN,Grafo.selectedA.t[0].Rect.center,Grafo.selectedA.t[1].Rect.center, LINE)

	pygame.display.update()
#desenhar end

# desenha apenas o vertice e a aresta que foi passada
def desenharPouco(v=None, a=None):
	rv = None
	ra = None
	rsv = None
	rsa = None

	if v:
		rv = pygame.draw.circle(SCREEN,BLUE,v.Rect.center,RECT_SIZE, CIRCLE)

	if a:
		ra = pygame.draw.line(SCREEN, PINK, a.t[0].Rect.center, a.t[1].Rect.center, LINE)

	if Grafo.selectedV:
		rsv = pygame.draw.circle(SCREEN,GREEN,Grafo.selectedV.Rect.center,RECT_SIZE, CIRCLE)

	if Grafo.selectedA:
		rsa = pygame.draw.line(SCREEN,GREEN,Grafo.selectedA.t[0].Rect.center,Grafo.selectedA.t[1].Rect.center, LINE)

	pygame.display.update([rv, ra, rsv, rsa])
#desenharPouco end

#loop principal
while not quitGame:
	
	events = pygame.event.get()
	for event in events:

		if event.type == pygame.QUIT:
			quitGame=True
			houveMudancas=False
			break

		#1 mouse click
		elif event.type == pygame.MOUSEBUTTONDOWN:
			local = Grafo.verificarClique(event.pos)
			print local
			clock.tick_busy_loop(FPS*0.1)

			#2 doubleclick
			if pygame.event.get(pygame.MOUSEBUTTONDOWN) and not isinstance(local, Vertice):
				houveMudancas = True
				Grafo.selectedA = None
				Rect = pygame.Rect(event.pos[0]-RECT_SIZE/2, event.pos[1]-RECT_SIZE/2, RECT_SIZE, RECT_SIZE) 
				vertice=Grafo.newV(Rect)
				Grafo.mostrar()
				continue
		
			#2 clicou no vazio
			elif not local:
				houveMudancas=False
				a=Grafo.selectedA
				v=Grafo.selectedV
				Grafo.selectedA = None
				Grafo.selectedV = None
				desenharPouco(v, a)
				continue

			#2 botao esquerdo do mouse continua pressionado
			elif Grafo.selectedV and not Grafo.selectedA and pygame.mouse.get_pressed()[0] :
				Grafo.antigoRect = local.Rect
				houveMudancas=True
				
				#3 pegar o disclique
				disclique = pygame.event.get(pygame.MOUSEBUTTONUP)
				while not disclique:
					disclique = pygame.event.get(pygame.MOUSEBUTTONUP)
					x,y = pygame.mouse.get_pos()
					local.Rect=pygame.Rect(x-RECT_SIZE/2, y-RECT_SIZE/2, RECT_SIZE, RECT_SIZE)
					desenhar(SCREEN)

				if isinstance(disclique, list): disclique = disclique[0]
				local2 = Grafo.verificarDisclique(disclique.pos, local.iID)
				print local2

				#3 desclicou num vertice para criar uma aresta
				if isinstance(local2, Vertice):
					houveMudancas = True
					local.Rect = Grafo.antigoRect
					aresta = Grafo.newA(local, local2)
					print Grafo.iTotalArestas

				Grafo.antigoRect=None

			else:
				houveMudancas=True

		#1 keyboard click
		elif event.type == pygame.KEYDOWN:
			
			#2 delete or bakspace
			if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
				houveMudancas = True
				if Grafo.selectedA:
					Grafo.removeA(Grafo.selectedA)
				elif Grafo.selectedV:
					Grafo.removeV()
		
	#for end

	if houveMudancas:
		desenhar(SCREEN)
		houveMudancas =False
		if Grafo.bConexo:
			print "CONEXO"
		else:
			print "NAO conexo"

	clock.tick(FPS)

#while end

pygame.quit()



