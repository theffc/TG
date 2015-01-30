from gui import lCores


def colorirVertices(lVertices):
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