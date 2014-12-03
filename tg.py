from __future__ import print_function		

class Grafo(object):
	"""docstring for Grafo"""

	lVertices=[]
	lArestas=[]
	iTotalVertices=0
	iTotalArestas=0
	selectedV=None
	selectedA=None
		
	@staticmethod
	def newV(Rect):
		v= Vertice(Rect)
		Grafo.lVertices.append(v)
		Grafo.iTotalVertices+=1

	@staticmethod
	def mostrarV():
		print('[ VERTICES')	
		for x in Grafo.lVertices:
			x.mostrar()
		print('VERTICES ]')


	@staticmethod
	def verticeClique(ponto):
		for vertice in Grafo.lVertices:
			if vertice.Rect.collidepoint(ponto):
				return True
		return False

	@staticmethod
	def verificarClique(ponto):

		for vertice in Grafo.lVertices:
			if vertice.Rect.collidepoint(ponto):
				Grafo.selectedV = vertice
				return vertice

		for aresta in Grafo.lArestas:
			
			# um dos vertices foi deslocado -> criar novo rect pra aresta
			if aresta.t[0].iMudouPos or aresta.t[1].iMudouPos:
				aresta.Rect = aresta.t[0].Rect.union(aresta.t[1].Rect)
				if not aresta.t[0]:
					aresta.t[0].iMudouPos -= 1
				else:
					aresta.t[1].iMudouPos -= 1
			
			if aresta.Rect.collidepoint(ponto):
				Grafo.selectedA=aresta
				return aresta

		Grafo.selectedA = None
		Grafo.selectedV = None
		return None


	@staticmethod
	def newA(v1, v2):

		# ja existe essa aresta
		if v1.iID in v2.setAdjs:
			return None

		Grafo.lArestas.append(aresta)
		Grafo.iTotalArestas+=1
		v1.setAdjs.add(v2.iID)
		v2.setAdjs.add(v1.iID)
		return aresta

	@staticmethod
	def desenhar(Surf):

		if Grafo.selectedV:
			Grafo.selectedV.Rect = pygame.draw.circle(Surf,BLUE,Grafo.selectedV.Rect.center,RECT_SIZE, LINE)
			Grafo.selectedV.bMudouPos = False

		if Grafo.selectedA:
			Grafo.selectedA.Rect = pygame.draw.line(Surf,BLUE,Grafo.selectedA.Rect.center,RECT_SIZE, LINE)
			Grafo.selectedA.bMudouPos=False

		for v in Grafo.lVertices:
			if v.bMudouPos:
				v.Rect = pygame.draw.circle(Surf,BLUE,v.Rect.center,RECT_SIZE, LINE)
				v.bMudouPos = False

		for a in Grafo.lArestas:
			if a.bMudouPos:
				a.Rect = pygame.draw.line(Surf, PINK, a.t[0].Rect.center, a.t[1].center, LINE)
				a.bMudouPos = False

class Vertice(object):
	"""docstring for Vertice"""

	iVid=0

		def __init__(self, Rect):
		super(Vertice, self).__init__()
		self.Rect = Rect
		self.iID = int( Vertice.iVid +1 )
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
		
		

