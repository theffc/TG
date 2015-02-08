#	Colecao de Funcoes Uteis para manipulacao de Grafos

from gui import lCores, COR_ARESTA, COR_VERTICE, COR_ARVORE, LIGHTGRAY
import copy
import random

def verificarClique(grafo, ponto):
	for vertice in grafo.lVertices:
		if vertice.Rect.collidepoint(ponto):
			grafo.selectedV = vertice
			grafo.selectedA = None
			return vertice
	
	lcopia = grafo.lArestas[:]		
	if grafo.selectedV :
		for i, aresta in enumerate(lcopia):
			if aresta.t[0].iID == grafo.selectedV.iID or aresta.t[1].iID == grafo.selectedV.iID:
				if aresta.Rect.collidepoint(ponto):
					if grafo.selectedA == aresta:
						del grafo.lArestas[i]
						grafo.lArestas.append(aresta)
						continue
					grafo.selectedA = aresta
					return aresta
		lcopia = grafo.lArestas[:]

	for i, aresta in enumerate(lcopia):
		if aresta.Rect.collidepoint(ponto):
			if grafo.selectedA == aresta:
				del grafo.lArestas[i]
				grafo.lArestas.append(aresta)
				continue
			grafo.selectedA = aresta
			grafo.selectedV = None
			return aresta
	return None
	#end verificarClique


def verificarDisclique(grafo, ponto ,id):
	for vertice in grafo.lVertices:
		if vertice.Rect.collidepoint(ponto) and not vertice.iID == id:
			grafo.selectedV = vertice
			return vertice
	return None
	#end verificarDisclique


def colorirVertices(lVertices):
	for v in lVertices:
		v.cor=None

	setCores = set(range(len(lCores)))
	setCores.discard(0)
	setCoresUsadas=set()
	for v in lVertices:
		coresAdjs = set()
		for v2 in v.lAdjs:
			if v2.cor:
				coresAdjs.add(v2.cor)
		possiveisCores = setCoresUsadas - coresAdjs
		if not possiveisCores:
			v.cor = setCores.pop()
			setCoresUsadas.add(v.cor)
		else:
			v.cor = possiveisCores.pop()

	iCores=len(setCoresUsadas)
	print("Número de cores usadas =", iCores)
	return iCores
	#end colorirVertices


def colorirPrimeiroMenor(grafo):
	verticesRemovidos=[]
	copia = copy.deepcopy(grafo)
	for x in range(len(copia.lVertices)):
		copia.lVertices.sort(key= lambda v: len(v.lAdjs))
		#print(copia.lVertices)
		verticesRemovidos.append(copia.lVertices[0].iID)
		copia.removeV(copia.lVertices[0])

	#print(verticesRemovidos)
	verticesRemovidos.reverse()
	#print(verticesRemovidos)
	listaVertices=[]
	for i in verticesRemovidos:
		for v in grafo.lVertices:
			if v.iID == i:
				listaVertices.append(v)
				break

	#print(listaVertices)
	grafo.iCores= colorirVertices(listaVertices)
	grafo.lVertices=listaVertices

	#end colorirPrimeiroMenor


def ehConexo(grafo):
	if grafo.iTotalArestas==0 or grafo.iTotalVertices==0:
		grafo.iConexo = False
		return
	if grafo.iTotalArestas < grafo.iTotalVertices-1 :
		grafo.iConexo = False
		return
	if grafo.iTotalArestas == (grafo.iTotalVertices*(grafo.iTotalVertices-1)/2):
		grafo.iConexo = grafo.iTotalVertices
		return

	grafo.setVisited= set()
	grafo.busca_profundidade(grafo.lVertices[0])
	t=len(grafo.setVisited)
	if t != grafo.iTotalVertices:
		grafo.iConexo = False
	else:
		grafo.iConexo= True


def gerarArvore(grafo):
	if grafo.iTotalVertices==1:
		grafo.iConexo=1
		return
	grafo.esconderArestas()
	ehConexo(grafo)
	if not grafo.iConexo:
		grafo.esconderArestas()
		return

	contador = 1
	copia = random.sample(grafo.lArestas, len(grafo.lArestas))
	lArestasRemovidas = []
	for a in copia:
		grafo.removeA(a)
		ehConexo(grafo)
		if not grafo.iConexo:
			x=grafo.newA(a.t[0], a.t[1])
			x.cor=COR_ARVORE
		else:
			lArestasRemovidas.append(a)

	for a in lArestasRemovidas:
		grafo.newA(a.t[0], a.t[1], esconder=True)
		contador += 1

	grauMinimo = grafo.getMenorGrau()

	if contador < grauMinimo:
		grafo.iConexo = contador
	else:
		grafo.iConexo = grauMinimo
