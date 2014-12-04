from __future__ import print_function
from pygame import display		

class Grafo(object):
	"""docstring for Grafo"""

	lVertices=[]
	lArestas=[]
	iTotalVertices=0
	iTotalArestas=0
	selectedV=None
	selectedA=None
	antigoRect=None
	lDirtyRects = []
	conexo = False
	visited = {}
		
	@staticmethod
	def newV(Rect):
		v= Vertice(Rect)
		Grafo.lVertices.append(v)
		Grafo.iTotalVertices+=1
		Grafo.selectedV = v
		Grafo.conexo=False

	@staticmethod
	def removeArestasDoV(v):
		lcopia=Grafo.lArestas[:]
		for a in lcopia:
			if a.t[0].iID == v.iID or a.t[1].iID == v.iID:
				Grafo.removeA(a, v)


	@staticmethod
	def removeV():
		print ("entrei no removeV")
		v = Grafo.selectedV

		if len(v.setAdjs)>1:
			Grafo.removeArestasDoV(v)

		Grafo.lVertices.remove(v)
		Grafo.iTotalVertices -= 1
		Grafo.selectedV = None
		Grafo.selectedA = None
		Grafo.conexo = Grafo.ehConexo()

		print ("sai do removeV")

	@staticmethod
	def mostrarV():
		print('[ VERTICES')	
		for x in Grafo.lVertices:
			x.mostrar()
		print('VERTICES ]')


	@staticmethod
	def mostrarA():
		print('[ ARESTAS')	
		for x in Grafo.lArestas:
			x.mostrar()
		print('ARESTAS ]')

	@staticmethod
	def verificarClique(ponto):

		for vertice in Grafo.lVertices:
			if vertice.Rect.collidepoint(ponto):
				Grafo.selectedV = vertice
				Grafo.selectedA = None
				return vertice
		
		if Grafo.selectedV :
			for aresta in Grafo.lArestas:			
				if aresta.t[0].iID == Grafo.selectedV.iID or aresta.t[1].iID == Grafo.selectedV.iID:
					if aresta.Rect.collidepoint(ponto):
						if Grafo.selectedA == aresta:
							continue
						Grafo.selectedA = aresta
						return aresta

		for aresta in Grafo.lArestas:
			if aresta.Rect.collidepoint(ponto):
				if Grafo.selectedA == aresta:
						continue
				Grafo.selectedA = aresta
				Grafo.selectedV = None
				return aresta

		return None

	@staticmethod
	def verificarDisclique(ponto ,id):

		for vertice in Grafo.lVertices:
			if vertice.Rect.collidepoint(ponto) and not vertice.iID == id:
				Grafo.selectedV = vertice
				return vertice

		return None

	@staticmethod
	def newA(v1, v2):

		# ja existe essa aresta
		if v1.iID in v2.setAdjs:
			return None

		aresta= Aresta(v1,v2)
		Grafo.lArestas.append(aresta)
		Grafo.iTotalArestas+=1
		v1.setAdjs.add(v2.iID)
		v2.setAdjs.add(v1.iID)
		if not Grafo.conexo:
			Grafo.conexo= Grafo.ehConexo()
		return aresta

	@staticmethod
	def removeA(a, v=0):
		a.t[0].setAdjs.discard(a.t[1].iID)
		a.t[1].setAdjs.discard(a.t[0].iID)
		Grafo.lArestas.remove(a)
		Grafo.iTotalArestas -= 1
		Grafo.selectedA = None
		if not v:
			Grafo.conexo=Grafo.ehConexo()

	@staticmethod
	def mostrar():
		Grafo.mostrarV()
		Grafo.mostrarA()


	@staticmethod
	def busca_profundidade(v=0):
		visited[v.iID]=True

   	if not v:
        v=Grafo.lArestas[0]

   	for x in v.lAdjs:
        if not visited[x.iID]:
            busca_profundidade(x)


	@staticmethod
	def ehConexo():
		if Grafo.iTotalArestas < Grafo.iTotalVertices-1 :
			return False

		conjunto = set()
		#conjunto.add(Grafo.lArestas[0].t[0].iID)
		for a in Grafo.lArestas:
			conjunto = a.t[0].setAdjs & a.t[1].setAdjs
			if not conjunto:
				return False

		x=len(conjunto)
		print ("Conjunto: ", x)
		if x > 0:
			return True		
		return False


class Vertice(object):
	"""docstring for Vertice"""

	iVid=0

	def __init__(self, Rect):
		super(Vertice, self).__init__()
		self.Rect = Rect
		self.iID = int( Vertice.iVid ) +1
		Vertice.iVid += 1
		self.setAdjs=set()
		self.setAdjs.add(self.iID)

	def mostrar(self):
		#print ( str(self.iID)+ ' - ' + str(self.Rect) , ',', '')
		print(self.iID, self.Rect.center, sep=' - ')
		
		

class Aresta(object):
	"""docstring for Aresta"""

	def __init__(self, v1, v2):
		super(Aresta, self).__init__()
		self.Rect = v1.Rect.union(v2.Rect)
		self.t = (v1, v2)
		self.fazParteDaArvore=False
		
	def mostrar(self):
		#print ( str(self.iID)+ ' - ' + str(self.Rect) , ',', '')
		print("(", self.Rect.center,' )')	

