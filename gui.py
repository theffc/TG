import tkinter.filedialog as tk
import os.path
import pygame
import random

pygame.init()

vidInfo = pygame.display.Info()

WIDTH = int(vidInfo.current_w * 0.8)
HEIGHT = int(vidInfo.current_h * 0.8)
RESOLUTION = (WIDTH, HEIGHT)
RECT_SIZE = int(WIDTH * 0.02)
CIRCLE = int(WIDTH * 0.0025)
LINE = int(WIDTH * 0.002)
SCREEN = pygame.display.set_mode(RESOLUTION, pygame.RESIZABLE)#, pygame.FULLSCREEN)
TEXTO = pygame.font.Font(None, 30)

BLUE = (10,100,255)
PINK = (255,0,255)
BLACK = (25,25,25)
GREEN = (0,255,100)
ORANGE = (255, 120, 30)
GRAY = (100,100,100)
WHITE = (255,255,255)

def getRectSize():
	return RECT_SIZE

# desenha todas as coisas na tela
def desenhar(grafo):
	SCREEN.fill(BLACK)

	if grafo.antigoRect:
		pygame.draw.circle(SCREEN, GRAY, grafo.antigoRect.center, RECT_SIZE, CIRCLE)

	for v in grafo.lVertices:
		v.Rect = pygame.draw.circle(SCREEN,BLUE,v.Rect.center,RECT_SIZE, CIRCLE)

	for a in grafo.lArestas:
		if a.pertenceArvore:
			cor = ORANGE
		else:
			cor = PINK
		
		a.Rect = pygame.draw.line(SCREEN, cor, a.t[0].Rect.center, a.t[1].Rect.center, LINE)

	if grafo.selectedV:
		grafo.selectedV.Rect = pygame.draw.circle(SCREEN,GREEN,grafo.selectedV.Rect.center,RECT_SIZE, CIRCLE)

	if grafo.selectedA:
		grafo.selectedA.Rect = pygame.draw.line(SCREEN,GREEN,grafo.selectedA.t[0].Rect.center,grafo.selectedA.t[1].Rect.center, LINE)

	for v in grafo.lVertices:
		sVid = str(v.iID)
		textSurf = TEXTO.render(sVid, 1, WHITE )
		SCREEN.blit(textSurf, v.Rect.center)

	if grafo.iConexo:
		texto = str(grafo.iConexo) + "-CONEXO"
		textSurf = TEXTO.render(texto,1, ORANGE)
	else:
		textSurf = TEXTO.render("NAO conexo",1, PINK)
	SCREEN.blit(textSurf, (10,10))



	pygame.display.update()
#desenhar end

# desenha apenas o vertice e a aresta que foi passada
def desenharPouco(grafo, v=None, a=None):
	rv = None
	ra = None
	rsv = None
	rsa = None

	if v:
		rv = pygame.draw.circle(SCREEN,BLUE,v.Rect.center,RECT_SIZE, CIRCLE)

	if a:
		if a.pertenceArvore:
			cor = ORANGE
		else:
			cor = PINK
		ra = pygame.draw.line(SCREEN, cor, a.t[0].Rect.center, a.t[1].Rect.center, LINE)

	if grafo.selectedV:
		rsv = pygame.draw.circle(SCREEN,GREEN,grafo.selectedV.Rect.center,RECT_SIZE, CIRCLE)

	if grafo.selectedA:
		rsa = pygame.draw.line(SCREEN,GREEN,grafo.selectedA.t[0].Rect.center,grafo.selectedA.t[1].Rect.center, LINE)

	pygame.display.update([rv, ra, rsv, rsa])
#desenharPouco end


def saveFileAs():
	f = tk.asksaveasfile(mode='wb', filetypes=[('graph files', '*.ffc')], defaultextension='.ffc', initialdir=os.path.join(os.path.dirname(__file__), 'saved'), initialfile=random.randint(1,999), title='Choose where to save your graph')
	
	return f

def openFile():
	f = tk.askopenfile(mode='rb', filetypes=[('graph files', '*.ffc')], defaultextension='.ffc', initialdir=os.path.join(os.path.dirname(__file__), 'saved'), title='Choose which graph you want to open' )

	return f