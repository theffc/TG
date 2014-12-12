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
	bConexo = False
	dVisited = {}
		
	@staticmethod
	def newV(Rect):
		v= Vertice(Rect)
		Grafo.lVertices.append(v)
		Grafo.iTotalVertices+=1
		Grafo.selectedV = v
		Grafo.bConexo=False
		return v

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

		if v.lAdjs:
			Grafo.removeArestasDoV(v)

		Grafo.lVertices.remove(v)
		Grafo.iTotalVertices -= 1
		Grafo.selectedV = None
		Grafo.selectedA = None
		Grafo.ehConexo()

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
		
		lcopia = Grafo.lArestas[:]		
		if Grafo.selectedV :
			for i, aresta in enumerate(lcopia):
				if aresta.t[0].iID == Grafo.selectedV.iID or aresta.t[1].iID == Grafo.selectedV.iID:
					if aresta.Rect.collidepoint(ponto):
						if Grafo.selectedA == aresta:
							del Grafo.lArestas[i]
							Grafo.lArestas.append(aresta)
							continue
						Grafo.selectedA = aresta
						return aresta
			lcopia = Grafo.lArestas[:]

		for i, aresta in enumerate(lcopia):
			if aresta.Rect.collidepoint(ponto):
				if Grafo.selectedA == aresta:
					del Grafo.lArestas[i]
					Grafo.lArestas.append(aresta)
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
		if v1 in v2.lAdjs:
			return None

		aresta= Aresta(v1,v2)
		Grafo.lArestas.append(aresta)
		Grafo.iTotalArestas+=1
		v1.lAdjs.append(v2)
		v2.lAdjs.append(v1)
		if not Grafo.bConexo:
			Grafo.ehConexo()
		return aresta

	@staticmethod
	def removeA(a, v=0):
		a.t[0].lAdjs.remove(a.t[1])
		a.t[1].lAdjs.remove(a.t[0])
		Grafo.lArestas.remove(a)
		Grafo.iTotalArestas -= 1
		Grafo.selectedA = None
		if not v:
			Grafo.ehConexo()

	@staticmethod
	def mostrar():
		Grafo.mostrarV()
		Grafo.mostrarA()


	@staticmethod
	def busca_profundidade(v):
		Grafo.dVisited[v.iID]=True

		for x in v.lAdjs:
			if not x.iID in Grafo.dVisited:
				Grafo.busca_profundidade(x)


	@staticmethod
	def ehConexo():
		if Grafo.iTotalVertices==1:
			Grafo.bConexo=True
			return

		if Grafo.iTotalArestas==0 or Grafo.iTotalVertices==0:
			Grafo.bConexo = False
			return

		if Grafo.iTotalArestas < Grafo.iTotalVertices-1 :
			Grafo.bConexo = False
			return

		if Grafo.dVisited:
			Grafo.dVisited.clear()

		Grafo.busca_profundidade(Grafo.lVertices[0])

		t=len(Grafo.dVisited)

		print(Grafo.dVisited)
		print("Total:", Grafo.iTotalVertices)
		print("tamanho: ", t)

		if t != Grafo.iTotalVertices:
			Grafo.bConexo = False
		else:
			Grafo.bConexo = True



class Vertice(object):
	"""docstring for Vertice"""

	iVid=0

	def __init__(self, Rect):
		super(Vertice, self).__init__()
		self.Rect = Rect
		self.iID = int( Vertice.iVid ) +1
		Vertice.iVid += 1
		self.lAdjs=[]


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

