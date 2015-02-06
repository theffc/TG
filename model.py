import random
from pygame import display	


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
		self.pertenceArvore=False
		self.cor = 
		
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
		self.iConexo = 0 # inteiro que representa a K-conectividade do grafo
		self.sNome = False # Path do arquivo em que o grafo esta salvo
		self.iVid=0 # inteiro usado para diferenciar vertices
		self.setVisited=set() # conjunto de ids de vertices usado na busca em profundidade

	def newV(self, Rect):
		v= Vertice(self, Rect)
		self.lVertices.append(v)
		self.iTotalVertices+=1
		self.selectedV = v
		
		if self.iTotalVertices == 1:
			self.iConexo = 1
		else:
			self.iConexo = 0

		for a in self.lArestas:
			a.pertenceArvore=False
		return v

	def removeArestasDoV(self, v):
		lcopia=self.lArestas[:]
		for a in lcopia:
			if a.t[0].iID == v.iID or a.t[1].iID == v.iID:
				self.removeA(a, verificar=False)


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
		self.gerarArvore()

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

	def newA(self, v1, v2, verificar=True):

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
		
		if self.iConexo:
			self.iConexo = self.getMenorGrau()
		elif verificar:
			self.gerarArvore()

		return aresta

	def removeA(self, a, verificar=True):
		a.t[0].lAdjs.remove(a.t[1])
		a.t[1].lAdjs.remove(a.t[0])
		self.lArestas.remove(a)
		self.iTotalArestas -= 1
		self.selectedA = None
		if verificar and a.pertenceArvore:
			self.gerarArvore()
		else:
			self.iConexo = self.getMenorGrau()

	def mostrar(self):
		self.mostrarV()
		self.mostrarA()


	def busca_profundidade(self, v):
		
		self.setVisited.add(v.iID)

		for x in v.lAdjs:
			if not x.iID in self.setVisited:
				self.busca_profundidade(x)


	def ehConexo(self):
		
		if self.iTotalVertices==1:
			self.iConexo=1
			return

		if self.iTotalArestas==0 or self.iTotalVertices==0:
			self.iConexo = 0
			return

		if self.iTotalArestas < self.iTotalVertices-1 :
			self.iConexo = 0
			return

		if self.iTotalArestas == (self.iTotalVertices*(self.iTotalVertices-1)/2):
			self.iConexo = self.iTotalVertices
			return

		self.setVisited= set()

		self.busca_profundidade(self.lVertices[0])

		t=len(self.setVisited)

		# print(self.setVisited)
		# print("Vertices:", self.iTotalVertices)
		# print("tamanho: ", t)

		if t != self.iTotalVertices:
			self.iConexo = 0
		else:
			self.iConexo = -1


	def gerarArvore(self):

		self.ehConexo()
		
		if not self.iConexo:
			for a in self.lArestas:
				a.pertenceArvore=False
			return

		contador = 1

		copia = random.sample(self.lArestas, len(self.lArestas))
		lArestasRemovidas = []

		for a in copia:
			self.removeA(a, verificar=False)
			self.ehConexo()
			if not self.iConexo:
				x=self.newA(a.t[0], a.t[1], verificar=False)
				x.pertenceArvore=True
			else:
				lArestasRemovidas.append(a)

		for a in lArestasRemovidas:
			self.newA(a.t[0], a.t[1], verificar=False)
			contador += 1

		grauMinimo = self.getMenorGrau()

		if contador < grauMinimo:
			self.iConexo = contador
		else:
			self.iConexo = grauMinimo

	def getMenorGrau(self):
		iGrauMinimo = len(self.lVertices[0].lAdjs)
		for v in self.lVertices:
			grau = len(v.lAdjs)
			if grau < iGrauMinimo:
				iGrauMinimo = grau

		return iGrauMinimo


	def completar(self):
		if(self.iTotalVertices * (self.iTotalVertices-1)/2) == self.iTotalArestas: #grafo completo
			self.gerarArvore()
			return

		for v1 in self.lVertices:
			for v2 in self.lVertices:
				self.newA(v1, v2, verificar=False)

		self.gerarArvore()

	def prepareToSave(self):
		contador=0
		for v in self.lVertices:
			contador+=1
			v.iID = contador		
		self.iVid = contador

	def reset(self):
		for v in self.lVertices:
			v.cor= 0
		for a in self.lArestas:
			a.cor= 