import pygame
import time
import tkFileDialog
import pickle
from tg import *
import os.path


FPS=50
quitGame=False
BLUE = (10,100,255)
PINK = (255,0,255)
BLACK = (25,25,25)
GREEN = (0,255,100)
GRAY = (100,100,100)

pygame.init()
vidInfo = pygame.display.Info()

WIDTH = int(vidInfo.current_w * 0.8)
HEIGHT = int(vidInfo.current_h * 0.8)
RESOLUTION = (WIDTH, HEIGHT)
RECT_SIZE = int(WIDTH * 0.02)
CIRCLE = int(WIDTH * 0.0025)
LINE = int(WIDTH * 0.002)
SCREEN = pygame.display.set_mode(RESOLUTION, pygame.RESIZABLE)#, pygame.FULLSCREEN)

pygame.event.set_blocked([pygame.USEREVENT, pygame.VIDEOEXPOSE, pygame.MOUSEMOTION, pygame.ACTIVEEVENT, pygame.VIDEORESIZE, pygame.JOYAXISMOTION, pygame.JOYBALLMOTION, pygame.JOYHATMOTION, pygame.JOYBUTTONUP, pygame.JOYBUTTONDOWN])
#pygame.event.set_allowed(None)

# desenha todas as coisas na tela
def desenhar(Surf):
	Surf.fill(BLACK)

	if grafo.antigoRect:
		pygame.draw.circle(Surf, GRAY, grafo.antigoRect.center, RECT_SIZE, CIRCLE)

	for v in grafo.lVertices:
		v.Rect = pygame.draw.circle(Surf,BLUE,v.Rect.center,RECT_SIZE, CIRCLE)

	for a in grafo.lArestas:
		a.Rect = pygame.draw.line(Surf, PINK, a.t[0].Rect.center, a.t[1].Rect.center, LINE)

	if grafo.selectedV:
		grafo.selectedV.Rect = pygame.draw.circle(Surf,GREEN,grafo.selectedV.Rect.center,RECT_SIZE, CIRCLE)

	if grafo.selectedA:
		grafo.selectedA.Rect = pygame.draw.line(Surf,GREEN,grafo.selectedA.t[0].Rect.center,grafo.selectedA.t[1].Rect.center, LINE)

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

	if grafo.selectedV:
		rsv = pygame.draw.circle(SCREEN,GREEN,grafo.selectedV.Rect.center,RECT_SIZE, CIRCLE)

	if grafo.selectedA:
		rsa = pygame.draw.line(SCREEN,GREEN,grafo.selectedA.t[0].Rect.center,grafo.selectedA.t[1].Rect.center, LINE)

	pygame.display.update([rv, ra, rsv, rsa])
#desenharPouco end

houveMudancas = True
clock = pygame.time.Clock()
pygame.mouse.set_visible(1)
grafo = Grafo(time.strftime("%d %b %Y"))

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
			local = grafo.verificarClique(event.pos)
			print local
			clock.tick_busy_loop(FPS*0.1)

			#2 doubleclick
			if pygame.event.get(pygame.MOUSEBUTTONDOWN) and not isinstance(local, Vertice):
				houveMudancas = True
				grafo.selectedA = None
				Rect = pygame.Rect(event.pos[0]-RECT_SIZE/2, event.pos[1]-RECT_SIZE/2, RECT_SIZE, RECT_SIZE) 
				vertice=grafo.newV(Rect)
				grafo.mostrar()
				continue
		
			#2 clicou no vazio
			elif not local:
				houveMudancas=False
				a=grafo.selectedA
				v=grafo.selectedV
				grafo.selectedA = None
				grafo.selectedV = None
				desenharPouco(v, a)
				continue

			#2 botao esquerdo do mouse continua pressionado
			elif grafo.selectedV and not grafo.selectedA and pygame.mouse.get_pressed()[0] :
				grafo.antigoRect = local.Rect
				houveMudancas=True
				
				#3 pegar o disclique
				disclique = pygame.event.get(pygame.MOUSEBUTTONUP)
				while not disclique:
					disclique = pygame.event.get(pygame.MOUSEBUTTONUP)
					x,y = pygame.mouse.get_pos()
					local.Rect=pygame.Rect(x-RECT_SIZE/2, y-RECT_SIZE/2, RECT_SIZE, RECT_SIZE)
					desenhar(SCREEN)

				if isinstance(disclique, list): disclique = disclique[0]
				local2 = grafo.verificarDisclique(disclique.pos, local.iID)
				print local2

				#3 desclicou num vertice para criar uma aresta
				if isinstance(local2, Vertice):
					houveMudancas = True
					local.Rect = grafo.antigoRect
					aresta = grafo.newA(local, local2)
					print grafo.iTotalArestas

				grafo.antigoRect=None

			else:
				houveMudancas=True

		#1 keyboard click
		elif event.type == pygame.KEYDOWN:
			teclas = pygame.key.get_pressed()

			#2 delete or bakspace
			if teclas[pygame.K_BACKSPACE] or teclas[pygame.K_DELETE]:
				if grafo.selectedA:
					grafo.removeA(grafo.selectedA)
					houveMudancas = True
				elif grafo.selectedV:
					grafo.removeV()
					houveMudancas = True

			#2 ctrl+S
			# 	salvar as mudanças
			elif (teclas[pygame.K_RCTRL] or teclas[pygame.K_LCTRL]) and teclas[pygame.K_s]:
				houveMudancas=False
				if grafo.sNome:
					f = open(grafo.sNome, mode='w')
					if f:
						print "uhul"
						pickle.dump(grafo, f)
						f.close()
				else:
					f = tkFileDialog.asksaveasfile(mode='w', filetypes=[('graph files', '*.ffc')], defaultextension='.ffc', initialdir=os.path.join(os.path.dirname(__file__), 'saved'), initialfile=grafo.sNome, title='Choose where to save your graph')
					if f:
						grafo.sNome = f.name
						print grafo.sNome
						pickle.dump(grafo, f)
						f.close()

			#2 ctrl+shift+S
			#		salvar o grafo em um novo arquivo
			elif (teclas[pygame.K_RCTRL] or teclas[pygame.K_LCTRL]) and (teclas[pygame.K_RSHIFT] or teclas[pygame.K_LSHIFT]) and teclas[pygame.K_s]:
				houveMudancas=False
				f = tkFileDialog.asksaveasfile(mode='w', filetypes=[('graph files', '*.ffc')], defaultextension='.ffc', initialdir=os.path.join(os.path.dirname(__file__), 'saved'), initialfile=grafo.sNome, title='Choose where to save your graph')
				if f:
					grafo.sNome = f.name
					pickle.dump(grafo, f)
					f.close()

			#2 ctrl+O
			elif (teclas[pygame.K_RCTRL] or teclas[pygame.K_LCTRL]) and teclas[pygame.K_o]:
				houveMudancas = True
				f = tkFileDialog.askopenfile(mode='r', filetypes=[('graph files', '*.ffc')], defaultextension='.ffc', initialdir=os.path.join(os.path.dirname(__file__), 'saved'), title='Choose which graph you want to open' )
				if f:
					print f.name
					grafo = pickle.load(f)
					f.close()

					


		
	#for end

	crtl_foi_pressionado=False

	if houveMudancas:
		desenhar(SCREEN)
		houveMudancas =False
		if grafo.bConexo:
			print "CONEXO"
		else:
			print "NAO conexo"

	clock.tick(FPS)

#while end

pygame.quit()



