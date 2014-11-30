		
class Grafo(object):
	"""docstring for Grafo"""

	vertices=[]
	arestas=[]
	totalVertices=0
	totalArestas=0
		
	def newV(xy):
		v= Vertice(xy)
		Grafo.vertices.append(v)
		Grafo.totalVertices+=1

	def newA():
		pass

class Vertice(object):

	vid=1

	"""docstring for Vertice"""
	def __init__(self, xy):
		super(Vertice, self).__init__()
		self.xy = xy
		
		self.id = self.vid
		self.vid+=1
		
		

class Aresta(object):

	"""docstring for Aresta"""
	def __init__(self, vertices):
		super(Aresta, self).__init__()
		self.vertices = vertices
		


Grafo.newV(2)
