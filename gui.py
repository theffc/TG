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
TEXT_H = TEXTO.get_height()

COR_VERTICE = (10,100,255)
COR_ARESTA = (240,10,240)
COR_BACKGROUND = (25,25,25)
COR_SELECTED = (20,255,100)
COR_ARVORE = (255, 120, 30)
GRAY = (100,100,100)
WHITE = (255,255,255)
LIGHTGRAY = (112,128,144)

FOREST = (34,139,34)
YELLOW = (255,250,80)
RED = (255,40,40)
PURPLE = (115,100,235)
AQUAMARINE = (120,255,220)
BROWN = (139,69,19)
BEJE = (220,220,170)
AZULAO = (40,40,255)
ROSA = (220,20,220)
OLIVE = (128,160,0)
SAND = (244,164,96)
ORANGE = (255, 160, 0)

lCores = [COR_VERTICE,YELLOW,RED,PURPLE,BROWN, OLIVE, AZULAO, ROSA, AQUAMARINE, BEJE, ORANGE]


# desenha todas as coisas na tela
def desenhar(grafo):
	SCREEN.fill(COR_BACKGROUND)

	if grafo.antigoRect:
		pygame.draw.circle(SCREEN, GRAY, grafo.antigoRect.center, RECT_SIZE, CIRCLE)

	for v in grafo.lVertices:
		v.Rect = pygame.draw.circle(SCREEN,lCores[v.cor],v.Rect.center,RECT_SIZE, CIRCLE)

	for a in grafo.lArestas:
		a.Rect = pygame.draw.line(SCREEN, a.cor, a.t[0].Rect.center, a.t[1].Rect.center, LINE)

	if grafo.selectedV:
		grafo.selectedV.Rect = pygame.draw.circle(SCREEN,COR_SELECTED,grafo.selectedV.Rect.center,RECT_SIZE, CIRCLE)

	if grafo.selectedA:
		grafo.selectedA.Rect = pygame.draw.line(SCREEN,COR_SELECTED,grafo.selectedA.t[0].Rect.center,grafo.selectedA.t[1].Rect.center, LINE)

	for v in grafo.lVertices:
		sVid = str(v.iID)
		textSurf = TEXTO.render(sVid, 1, WHITE )
		SCREEN.blit(textSurf, v.Rect.center)

	if grafo.iConexo is not -1:
		if grafo.iConexo:
			texto = str(grafo.iConexo) + "-conexo"
			textSurf = TEXTO.render(texto,1, COR_ARVORE)
		else:
			textSurf = TEXTO.render("NAO conexo",1, LIGHTGRAY)
		SCREEN.blit(textSurf, (10,10))

	if grafo.iCores:
		if grafo.iCores==1:
			texto= str(grafo.iCores)+" cor"
		else:
			texto= str(grafo.iCores)+" cores"
		textSurf= TEXTO.render(texto, 1, lCores[1])
		SCREEN.blit(textSurf, (10, 10+TEXT_H))

	pygame.display.update()
#desenhar end

# desenha apenas o vertice e a aresta que foi passada
def desenharPouco(grafo, v=None, a=None, update=True):
	rv = None
	ra = None
	rsv = None
	rsa = None
	rant= None

	if not hasattr(desenharPouco, "dirtyRects"):
		desenharPouco.dirtyRects = []

	if grafo.antigoRect:
		rant = pygame.draw.circle(SCREEN, COR_BACKGROUND, grafo.antigoRect.center, RECT_SIZE, CIRCLE)

	if grafo.selectedV:
		rsv = pygame.draw.circle(SCREEN,COR_SELECTED,grafo.selectedV.Rect.center,RECT_SIZE, CIRCLE)

	if grafo.selectedA:
		rsa = pygame.draw.line(SCREEN,COR_SELECTED,grafo.selectedA.t[0].Rect.center,grafo.selectedA.t[1].Rect.center, LINE)

	if v:
		rv = pygame.draw.circle(SCREEN,lCores[v.cor],v.Rect.center,RECT_SIZE, CIRCLE)

	if a:
		ra = pygame.draw.line(SCREEN, a.cor, a.t[0].Rect.center, a.t[1].Rect.center, LINE)

	if update:
		x=[rant, rv, ra, rsv, rsa]+desenharPouco.dirtyRects
		pygame.display.update(x)
		desenharPouco.dirtyRects=[]
	else:
		desenharPouco.dirtyRects+= [rv,ra,rsv,rsa,rant]
#desenharPouco end


def saveFileAs():
	f = tk.asksaveasfile(mode='wb', filetypes=[('graph files', '*.ffc')], defaultextension='.ffc', initialdir=os.path.join(os.path.dirname(__file__), 'saved'), initialfile=random.randint(1,999), title='Choose where to save your graph')
	
	return f

def openFile():
	f = tk.askopenfile(mode='rb', filetypes=[('graph files', '*.ffc')], defaultextension='.ffc', initialdir=os.path.join(os.path.dirname(__file__), 'saved'), title='Choose which graph you want to open' )

	return f