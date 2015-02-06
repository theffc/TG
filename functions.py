from gui import lCores
import copy


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

	print("Número de cores usadas =", len(setCoresUsadas))


def colorirPrimeiroMenor(grafo):
	verticesRemovidos=[]
	copia = copy.deepcopy(grafo)
	for x in range(len(copia.lVertices)):
		copia.lVertices.sort(key= lambda v: len(v.lAdjs))
		print(copia.lVertices)
		verticesRemovidos.append(copia.lVertices[0].iID)
		copia.removeV(copia.lVertices[0])

	print(verticesRemovidos)
	verticesRemovidos.reverse()
	print(verticesRemovidos)
	listaVertices=[]
	for i in verticesRemovidos:
		for v in grafo.lVertices:
			if v.iID == i:
				listaVertices.append(v)
				break

	print(listaVertices)
	colorirVertices(listaVertices)
	grafo.lVertices=listaVertices



