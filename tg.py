from __future__ import print_function		

class Grafo(object):
	"""docstring for Grafo"""

	lVertices=[]
	lArestas=[]
	iTotalVertices=0
	iTotalArestas=0
	selecionado=None
		
	@staticmethod
	def newV(Rect):
		v= Vertice(Rect)
		Grafo.lVertices.append(v)
		Grafo.iTotalVertices+=1

	@staticmethod
	def mostrarV():
		print('[')	
		for x in Grafo.lVertices:
			x.mostrar()
		print(']')

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
				return vertice

		for aresta in Grafo.lArestas:
			if aresta.Rect.collidepoint(ponto):
				return aresta

		return None


	@staticmethod
	def newA(v1, v2):
		if v1.iID in v2.setAdjs or v2.iID in v1.setAdjs
			return False

		Rect = v1.Rect.union(v2.Rect)
		aresta = (Rect, v1, v2)
		lArestas.append(aresta)
		Grafo.iTotalArestas+=1
		v1.setAdjs.add(v2.iID)
		v2.setAdjs.add(v1.iID)
		return True


class Vertice(object):

	iVid=1

	"""docstring for Vertice"""
	def __init__(self, Rect):
		super(Vertice, self).__init__()
		self.Rect = Rect
		self.tCenter = Rect.center
		self.iID = Vertice.iVid
		Vertice.iVid += 1
		self.setAdjs=set().add(Vertice.iVid)

	def mostrar(self):
		#print ( str(self.iID)+ ' - ' + str(self.Rect) , ',', '')
		print(self.iID, self.tCenter, sep=' - ')
		
		

class Aresta(object):

	"""docstring for Aresta"""
	def __init__(self, lVertices):
		super(Aresta, self).__init__()
		
		

