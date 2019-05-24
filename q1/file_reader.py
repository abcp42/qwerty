import pickle

def saveSTP(path = "USA-road-d.NY.gr"):
	f=open(path, "r")
	vertices_dict = {}
	arestas = []
	vertices = []
	f1=f.readlines()
	for x in f1:
		if(x[0]=='a'):
			s = x.split(' ')
			vertices_dict[s[1]] = 1
			vertices_dict[s[2]] = 1
			a = s[3]
			arestas.append((int(s[1]),int(s[2]),int(a)))
	for key in vertices_dict:
		vertices.append(int(key))

	pickle.dump( (vertices,arestas), open( "vert_arestas.p", "wb" ) )
 
def saveSTP2(path = "alue7080.stp"):
	f=open(path, "r")
	vertices_dict = {}
	arestas = []
	vertices = []
	f1=f.readlines()
	for x in f1:
		if(x[:2]=='E '):
			s = x.split(' ')
			#print(s)
			vertices_dict[s[1]] = 1
			vertices_dict[s[2]] = 1
			a = s[3]
			arestas.append((int(s[1]),int(s[2]),int(a)))
	for key in vertices_dict:
		vertices.append(int(key))
	#print(arestas)
	pickle.dump( (vertices,arestas), open( "vert_arestas2.p", "wb" ) )


def readSTP(path = "USA-road-d.NY.gr"):
	f=open(path, "r")
	vertices_dict = {}
	arestas = []
	vertices = []
	f1=f.readlines()
	for x in f1:
		if(x[0]=='a'):
			s = x.split(' ')
			vertices_dict[s[1]] = 1
			vertices_dict[s[2]] = 1
			a = s[3]
			arestas.append((int(s[1]),int(s[2]),int(a)))
	for key in vertices_dict:
		vertices.append(int(key))

	return vertices,arestas

#saveSTP2()


