import pygame
import time # time.strftime("%d %b %Y")
import pickle
import random

import gui
import model
import functions

FPS=50
quitGame=False


pygame.event.set_blocked([pygame.USEREVENT, pygame.VIDEOEXPOSE, pygame.MOUSEMOTION, pygame.ACTIVEEVENT, pygame.VIDEORESIZE, pygame.JOYAXISMOTION, pygame.JOYBALLMOTION, pygame.JOYHATMOTION, pygame.JOYBUTTONUP, pygame.JOYBUTTONDOWN])
#pygame.event.set_allowed(None)

houveMudancas = True
clock = pygame.time.Clock()
pygame.mouse.set_visible(1)
grafo = model.Grafo()

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
			print (local)
			clock.tick_busy_loop(FPS*0.1)

			#2 doubleclick
			if pygame.event.get(pygame.MOUSEBUTTONDOWN) and not isinstance(local, model.Vertice):
				houveMudancas = True
				grafo.selectedA = None
				Rect = pygame.Rect(event.pos[0]-gui.RECT_SIZE/2, event.pos[1]-gui.RECT_SIZE/2, gui.RECT_SIZE, gui.RECT_SIZE) 
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
				gui.desenharPouco(grafo, v, a)
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
					local.Rect=pygame.Rect(x-gui.RECT_SIZE/2, y-gui.RECT_SIZE/2, gui.RECT_SIZE, gui.RECT_SIZE)
					gui.desenhar(grafo)

				if isinstance(disclique, list): disclique = disclique[0]
				local2 = grafo.verificarDisclique(disclique.pos, local.iID)
				print (local2)

				#3 desclicou num vertice para criar uma aresta
				if isinstance(local2, model.Vertice):
					houveMudancas = True
					local.Rect = grafo.antigoRect
					aresta = grafo.newA(local, local2)
					print (grafo.iTotalArestas)

				grafo.antigoRect=None

			else:
				houveMudancas=True

		#1 keyboard click
		elif event.type == pygame.KEYDOWN:
			teclas = pygame.key.get_pressed()

			#2 delete or bakspace
			# 	deleta o vertice ou a aresta selecionada
			if teclas[pygame.K_BACKSPACE] or teclas[pygame.K_DELETE]:
				if grafo.selectedA:
					grafo.removeA(grafo.selectedA)
					houveMudancas = True
				elif grafo.selectedV:
					grafo.removeV()
					houveMudancas = True

			#2 ctrl+C
			#		completar o grafo, criando arestas entre todos os vertices
			elif (teclas[pygame.K_RCTRL] or teclas[pygame.K_LCTRL]) and (teclas[pygame.K_c]):
				grafo.completar()
				houveMudancas=True

			#2 ctrl+shift+S
			#		salvar o grafo em um novo arquivo
			elif (teclas[pygame.K_RCTRL] or teclas[pygame.K_LCTRL]) and (teclas[pygame.K_RSHIFT] or teclas[pygame.K_LSHIFT]) and teclas[pygame.K_s]:
				houveMudancas=True
				f = gui.saveFileAs()
				if f:
					grafo.sNome = f.name
					grafo.prepareToSave()
					pickle.dump(grafo, f)
					f.close()


			#2 ctrl+S
			# 	salvar as mudancas
			elif (teclas[pygame.K_RCTRL] or teclas[pygame.K_LCTRL]) and teclas[pygame.K_s]:
				houveMudancas=True
				if grafo.sNome:
					f = open(grafo.sNome, mode='wb')
					if f:
						grafo.prepareToSave()
						pickle.dump(grafo, f)
						f.close()
				else:
					f = gui.saveFileAs()
					if f:
						grafo.prepareToSave()
						grafo.sNome = f.name
						print(f.name)
						pickle.dump(grafo, f)
						f.close()

			#2 ctrl+O
			#		abrir arquivo
			elif (teclas[pygame.K_RCTRL] or teclas[pygame.K_LCTRL]) and teclas[pygame.K_o]:
				houveMudancas = True
				f = gui.openFile()
				if f:
					grafo = pickle.load(f)
					f.close()

			elif teclas[pygame.K_j]:
				houveMudancas = True
				functions.colorirVertices(random.sample(grafo.lVertices, len(grafo.lVertices)))

			elif teclas[pygame.K_k]:
				houveMudancas=True
				x=sorted(grafo.lVertices, key=lambda v: len(v.lAdjs), reverse=True)
				print(x)
				functions.colorirVertices(x)
				
	#for end

	if houveMudancas:
		gui.desenhar(grafo)
		houveMudancas =False

	clock.tick(FPS)

#while end

pygame.quit()
