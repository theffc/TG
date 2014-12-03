from __future__ import print_function		

class Grafo(object):
	"""docstring for Grafo"""

	lVertices=[]
	lArestas=[]
	iTotalVertices=0
	iTotalArestas=0
	selectedV=None
	selectedA=None
	lDirtyRects = []
		
	@staticmethod
	def newV(Rect):
		v= Vertice(Rect)
		Grafo.lVertices.append(v)
		Grafo.iTotalVertices+=1
		Grafo.selectedV = v

	@staticmethod
	def mostrarV():
		print('[ VERTICES')	
		for x in Grafo.lVertices:
			x.mostrar()
		print('VERTICES ]')


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
						Grafo.selectedA=aresta
						return aresta

		Grafo.selectedA = None
		Grafo.selectedV = None
		return None

	@staticmethod
	def verificarDisclique(ponto):

		for vertice in Grafo.lVertices:
			if vertice.Rect.collidepoint(ponto):
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
		return aresta



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
		self.iMudouPos = 0
		self.bMudouPos = True

	def mostrar(self):
		#print ( str(self.iID)+ ' - ' + str(self.Rect) , ',', '')
		print(self.iID, self.Rect.center, sep=' - ')
		
		

class Aresta(object):
	"""docstring for Aresta"""

	def __init__(self, v1, v2):
		super(Aresta, self).__init__()
		self.Rect = v1.Rect.union(v2.Rect)
		self.t = (v1, v2)
		self.bMudouPos = True
		
		

