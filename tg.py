from __future__ import print_function		

class Grafo(object):
	"""docstring for Grafo"""

	vertices=[]
	arestas=[]
	totalVertices=0
	totalArestas=0
		
	@staticmethod
	def newV(Rect):
		v= Vertice(Rect)
		Grafo.vertices.append(v)
		Grafo.totalVertices+=1

	@staticmethod
	def mostrarV():
		print('[')	
		for x in Grafo.vertices:
			x.mostrar()
		print(']')

	@staticmethod
	def colidiuXY(ponto):
		for vertice in Grafo.vertices:
			if vertice.Rect.collidepoint(ponto):
				return True
		return False

class Vertice(object):

	vid=1

	"""docstring for Vertice"""
	def __init__(self, Rect):
		super(Vertice, self).__init__()
		self.Rect = Rect
		self.center = Rect.center
		self.id = Vertice.vid
		Vertice.vid += 1

	def mostrar(self):
		#print ( str(self.id)+ ' - ' + str(self.Rect) , ',', '')
		print(self.id, self.center, sep=' - ')
		
		

class Aresta(object):

	"""docstring for Aresta"""
	def __init__(self, vertices):
		super(Aresta, self).__init__()
		self.vertices = vertices
		

