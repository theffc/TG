import random
import copy
from pygame import display	
from gui import COR_ARESTA, COR_VERTICE, COR_ARVORE, LIGHTGRAY


class Vertice(object):
	"""docstring for Vertice"""

	def __init__(self, Grafo, Rect):
		super(Vertice, self).__init__()
		self.Rect = Rect
		self.iID = int( Grafo.iVid ) +1
		Grafo.iVid += 1
		self.lAdjs=[]
		self.cor=0

	def mostrar(self):
		#print ( str(self.iID)+ ' - ' + str(self.Rect) , ',', '')
		print(self.iID, self.Rect.center, sep=' - ')
		

class Aresta(object):
	"""docstring for Aresta"""

	def __init__(self, v1, v2):
		super(Aresta, self).__init__()
		self.Rect = v1.Rect.union(v2.Rect)
		self.t = (v1, v2)
		self.cor = COR_ARESTA
		
	def mostrar(self):
		#print ( str(self.iID)+ ' - ' + str(self.Rect) , ',', '')
		print("(", self.Rect.center,' )')	



class Grafo(object):
	"""docstring for Grafo"""

	def __init__(self):
		self.lVertices=[]
		self.lArestas=[]
		self.iTotalVertices=0
		self.iTotalArestas=0
		self.selectedV=None # referencia ao Vertice selecionado
		self.selectedA=None # referencia a Aresta selecionada
		self.antigoRect=None # usado apenas para printar a bolinha cinza quando o usuario estiver mudando um vertice de lugar
		self.iConexo = -1 # inteiro que representa a K-conectividade do grafo
		self.sNome = False # Path do arquivo em que o grafo esta salvo
		self.iVid=0 # inteiro usado para diferenciar vertices
		self.setVisited=set() # conjunto de ids de vertices usado na busca em profundidade
		self.iCores= 0 # numero minimo de cores para colorir os vertices do grafo

	def newV(self, Rect):
		v= Vertice(self, Rect)
		self.lVertices.append(v)
		self.iTotalVertices+=1
		self.selectedV = v
		return v

	def removeArestasDoV(self, v):
		lcopia=self.lArestas[:]
		for a in lcopia:
			if a.t[0].iID == v.iID or a.t[1].iID == v.iID:
				self.removeA(a)

	def removeV(self, vertice=None):
		if not vertice:
			v = self.selectedV
		else:
			v = vertice

		if v.lAdjs:
			self.removeArestasDoV(v)

		self.lVertices.remove(v)
		self.iTotalVertices -= 1
		self.selectedV = None
		self.selectedA = None

	def mostrarV(self):
		print('[ VERTICES')	
		for x in self.lVertices:
			x.mostrar()
		print('VERTICES ]')

	def mostrarA(self):
		print('[ ARESTAS')	
		for x in self.lArestas:
			x.mostrar()
		print('ARESTAS ]')

	def newA(self, v1, v2, esconder=False):
		if v1.iID == v2.iID:
			return None

		# ja existe essa aresta
		for v in v2.lAdjs:
			if v.iID == v1.iID:
				return None

		aresta= Aresta(v1,v2)
		self.lArestas.append(aresta)
		self.iTotalArestas+=1
		v1.lAdjs.append(v2)
		v2.lAdjs.append(v1)
		if esconder:
			aresta.cor=LIGHTGRAY
		return aresta

	def removeA(self, a):
		a.t[0].lAdjs.remove(a.t[1])
		a.t[1].lAdjs.remove(a.t[0])
		self.lArestas.remove(a)
		self.iTotalArestas -= 1
		self.selectedA = None

	def mostrar(self):
		self.mostrarV()
		self.mostrarA()

	def busca_profundidade(self, v):
		self.setVisited.add(v.iID)
		for x in v.lAdjs:
			if not x.iID in self.setVisited:
				self.busca_profundidade(x)

	def getMenorGrau(self):
		iGrauMinimo = len(self.lVertices[0].lAdjs)
		for v in self.lVertices:
			grau = len(v.lAdjs)
			if grau < iGrauMinimo:
				iGrauMinimo = grau
		return iGrauMinimo

	def esconderArestas(self):
		for a in self.lArestas:
			a.cor= LIGHTGRAY

	def completar(self):
		if(self.iTotalVertices * (self.iTotalVertices-1)/2) == self.iTotalArestas: #grafo completo
			return
		for v1 in self.lVertices:
			for v2 in self.lVertices:
				self.newA(v1, v2)

	def prepareToSave(self):
		contador=0
		for v in self.lVertices:
			contador+=1
			v.iID = contador		
		self.iVid = contador

	def reset(self, vertices=True, arestas=True):
		if vertices:
			for v in self.lVertices:
				v.cor= 0
		if arestas:
			for a in self.lArestas:
				a.cor= COR_ARESTA
		self.iConexo= -1
		self.iCores= 0


	#end Grafo