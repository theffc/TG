from __future__ import print_function		

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
		
	@staticmethod
	def newV(Rect):
		v= Vertice(Rect)
		Grafo.lVertices.append(v)
		Grafo.iTotalVertices+=1
		Grafo.selectedV = v

	@staticmethod
	def removeArestasDoV(v):
		lcopia=Grafo.lArestas[:]
		for a in lcopia:
			if a.t[0].iID in v.setAdjs and a.t[1].iID in v.setAdjs:
				Grafo.removeA(a)


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

		Grafo.selectedA = None
		Grafo.selectedV = None
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
		return aresta

	@staticmethod
	def removeA(a):
		a.t[0].setAdjs.discard(a.t[1].iID)
		a.t[1].setAdjs.discard(a.t[0].iID)
		Grafo.lArestas.remove(a)
		Grafo.iTotalArestas -= 1
		Grafo.selectedA = None

	@staticmethod
	def mostrar():
		Grafo.mostrarV()
		Grafo.mostrarA()


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
		
	def mostrar(self):
		#print ( str(self.iID)+ ' - ' + str(self.Rect) , ',', '')
		print("(", self.Rect.center,' )')	

