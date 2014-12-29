from __future__ import print_function
from pygame import display		

class Grafo(object):
	"""docstring for Grafo"""

	def __init__(self, data):
		self.lVertices=[]
		self.lArestas=[]
		self.iTotalVertices=0
		self.iTotalArestas=0
		self.selectedV=None
		self.selectedA=None
		self.antigoRect=None
		self.lDirtyRects = []
		self.bConexo = False
		self.dVisited = {}
		self.sNome = False
		self.iVid=0

	def newV(self, Rect):
		v= Vertice(self, Rect)
		self.lVertices.append(v)
		self.iTotalVertices+=1
		self.selectedV = v
		self.bConexo=False
		return v

	def removeArestasDoV(self, v):
		lcopia=self.lArestas[:]
		for a in lcopia:
			if a.t[0].iID == v.iID or a.t[1].iID == v.iID:
				self.removeA(a, v)


	def removeV(self):
		print ("entrei no removeV")
		v = self.selectedV

		if v.lAdjs:
			self.removeArestasDoV(v)

		self.lVertices.remove(v)
		self.iTotalVertices -= 1
		self.selectedV = None
		self.selectedA = None
		self.ehConexo()

		print ("sai do removeV")

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

	def verificarClique(self, ponto):

		for vertice in self.lVertices:
			if vertice.Rect.collidepoint(ponto):
				self.selectedV = vertice
				self.selectedA = None
				return vertice
		
		lcopia = self.lArestas[:]		
		if self.selectedV :
			for i, aresta in enumerate(lcopia):
				if aresta.t[0].iID == self.selectedV.iID or aresta.t[1].iID == self.selectedV.iID:
					if aresta.Rect.collidepoint(ponto):
						if self.selectedA == aresta:
							del self.lArestas[i]
							self.lArestas.append(aresta)
							continue
						self.selectedA = aresta
						return aresta
			lcopia = self.lArestas[:]

		for i, aresta in enumerate(lcopia):
			if aresta.Rect.collidepoint(ponto):
				if self.selectedA == aresta:
					del self.lArestas[i]
					self.lArestas.append(aresta)
					continue
				self.selectedA = aresta
				self.selectedV = None
				return aresta

		return None

	def verificarDisclique(self, ponto ,id):

		for vertice in self.lVertices:
			if vertice.Rect.collidepoint(ponto) and not vertice.iID == id:
				self.selectedV = vertice
				return vertice

		return None

	def newA(self, v1, v2):

		# ja existe essa aresta
		if v1 in v2.lAdjs:
			return None

		aresta= Aresta(v1,v2)
		self.lArestas.append(aresta)
		self.iTotalArestas+=1
		v1.lAdjs.append(v2)
		v2.lAdjs.append(v1)
		if not self.bConexo:
			self.ehConexo()
		return aresta

	def removeA(self, a, v=0):
		a.t[0].lAdjs.remove(a.t[1])
		a.t[1].lAdjs.remove(a.t[0])
		self.lArestas.remove(a)
		self.iTotalArestas -= 1
		self.selectedA = None
		if not v:
			self.ehConexo()

	def mostrar(self):
		self.mostrarV()
		self.mostrarA()


	def busca_profundidade(self, v):
		self.dVisited[v.iID]=True

		for x in v.lAdjs:
			if not x.iID in self.dVisited:
				self.busca_profundidade(x)


	def ehConexo(self):
		if self.iTotalVertices==1:
			self.bConexo=True
			return

		if self.iTotalArestas==0 or self.iTotalVertices==0:
			self.bConexo = False
			return

		if self.iTotalArestas < self.iTotalVertices-1 :
			self.bConexo = False
			return

		if self.dVisited:
			self.dVisited.clear()

		self.busca_profundidade(self.lVertices[0])

		t=len(self.dVisited)

		print(self.dVisited)
		print("Total:", self.iTotalVertices)
		print("tamanho: ", t)

		if t != self.iTotalVertices:
			self.bConexo = False
		else:
			self.bConexo = True



class Vertice(object):
	"""docstring for Vertice"""

	def __init__(self, Grafo, Rect):
		super(Vertice, self).__init__()
		self.Rect = Rect
		self.iID = int( Grafo.iVid ) +1
		Grafo.iVid += 1
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

