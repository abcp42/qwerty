from file_reader import readSTP
import pickle
import time

class Vertice():
  def __init__(self):
    self.id = 0
    self.dist = 9999999
    self.visited = 0
    self.adj_vert_num = 0
    self.weights = {}
    self.adjs = {}
    

#cada vertice tem que ter os demais vertices armazenado
def create_node_vertice(i,num_ver):
  v = Vertice()
  v.id =i
  return v

def reset_node(v):
  v.dist= 99999999
  v.visited =0

def insert_adj_in_node(v1,v2,w):
  v1.adjs[v2.id] = v2
  v1.adj_vert_num+=1
  v1.weights[v2.id] = w


def get_min_dist(vertice_list,num_ver):
  minimum = 999999999 
  min_index = 0
  for i in range(num_ver):
    #count_n_operations++;
    if (vertice_list[i].visited == 0 and vertice_list[i].dist <= minimum):
      minimum = vertice_list[i].dist 
      min_index = i
  return vertice_list[min_index];

def print_path(parent,j):
  if (parent[j]==-1):
    return
  print_path(parent, parent[j])
  print(j+1,end = ', ') # sempre ajustando vertices, ja que comeco do 0...

def print_solution(vertice_list,nV,parent,src):
  print("Vertex       Distance        Path")
  print(nV)
  for i in range(nV):
    if(vertice_list[i].dist ==99999999999999):
      print(src+1,"->",i+1,"     INF ")
    else:
      print(src+1,"->",i+1,"       ",vertice_list[i].dist,"            ",src+1,end = ': ')
    #for p in parent:
    #  if(p!=-1):
    #    print(p+1, end = ',')
    #print('')
    print_path(parent, i)
    print('')

def dijkstra(vertice_list,src,num_ver):
  #from min import get_min_distance
  parent = []
  #marca todos os vertices como nao visitados
  for i in range(num_ver):
    parent.append(-1)
  #vertice inicial tem distancia 0.  Na 1 iteracao todos os demais estao setados com 'infinidade'
  vertice_list[src].dist=0

  #pelo numero de vertices, escolha o vertice de menor distancia atualmente no grafo.
  #Na primeira iteracao sera o source. 
  for j in range(num_ver-1):
    #print('getting min distance...')
    #start = time.time()
    v_min = get_min_dist(vertice_list,num_ver)# 1.1 O(n)
    #v_min = get_min_dist(vertice_list,num_ver)
    #end = time. time()
    #print('getmin: ',end - start)
    #print(v_min.id)
    #print('got min distance!')
    print("num of vert left: ",num_ver-j)
    if(v_min==None):
      continue
    v_min.visited=1#marque vertice minimo como ja visitado. Desse modo o 1.2 sera feito, pois nao sera mais contado
    #para cada vertice adjacente ao vertice minimo
    #start = time.time()
    for key in v_min.adjs:# 1.3
      adj_ver = vertice_list[v_min.adjs[key].id]#pega o vertice adjacente 
      #Se a distancia atual do vertice minimo, mais o seu peso, for menor que a distancia do vert adjacente
      if(v_min.dist + v_min.weights[key] < adj_ver.dist ):
        adj_ver.dist = v_min.dist + v_min.weights[key] #a distancia do vertice adjacente tera esse novo valor
        parent[adj_ver.id] = v_min.id # a pos que era do vertice adjacente, sera do menor v agora

    #end = time. time()
    #print('forloop: ',end - start)

    
  print_solution(vertice_list,len(vertice_list),parent,src)    



vertice_list = []
#e = [(1,2,7),(1,3,9),(1,6,14),(2,3,10),(2,4,15),(3,4,11),(3,6,2),(4,5,6),(5,6,9)]
#vertices = [1,2,3,4,5,6]
#e,vertices = readSTP()
vertices,e = pickle.load( open( "vert_arestas2.p", "rb" ) )
for i in range(len(vertices)):
  vertice_list.append(create_node_vertice(i,len(vertices))) #crie vertices cada um com sua lista de vertices
vertices = []
for i in range(len(e)):
  #para cada par de vertices, conecte suas arestas
  #insere v2 no v1, bem como o peso

  insert_adj_in_node(vertice_list[e[i][0]-1],#v1
                    vertice_list[e[i][1]-1],#v2
                    e[i][2])

#pickle.dump( vertice_list, open( "vertice_list.p", "wb" ) )

print("Dijkstra!!!")
dijkstra(vertice_list, 0, len(vertice_list))

"""
for i in range(vertices):
  print("ver:",vertice_list[i].id+1)
  ver = vertice_list[i]
  for j in range(ver.adj_vert_num):
    print('adjs:',ver.adjs[j].id+1)
    print('weight:',ver.weights[j])
"""
