
class Vertice():
  def __init__(self):
    self.id = 0
    self.dist = 9999999
    self.visited = False
    self.adj_vert_num = 0
    self.weights = []
    self.adjs = []

#cada vertice tem que ter os demais vertices armazenado
def create_node_vertice(i,num_ver):
  v = Vertice()
  v.id =i+1
  for i in range(num_ver):
    v.adjs.append(None)
    v.weights.append(0)
  return v

def reset_node(v):
  v.dist= 99999999
  v.visited =False


def insert_adj_in_node(v,w,p,num_ver):
  for i in range(num_ver):
    if(v.adjs[i]==None):
      v.adjs[i] = w
      v.adj_vert_num+=1
      v.weights[i]=p
      break


def get_min_distance(vertice_list,num_ver):
  minimum = 999999999 
  min_index = 0
  for i in range(num_ver):
    #count_n_operations++;
    if (vertice_list[i].visited == False and vertice_list[i].dist <= minimum):
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
  parent = []
  #marca todos os vertices como nao visitados
  for i in range(num_ver):
    parent.append(-1)
  #vertice inicial tem distancia 0.  Na 1 iteracao todos os demais estao setados com 'infinidade'
  vertice_list[src].dist=0
  
  #tree = GTree((GCompareFunc)cmp_func);
  #g_tree_insert(tree,dv[src], dv[src]);
  from atree import AlphaTree
  tree = AlphaTree()
  tree.alpha_insert(vertice_list[src],src)
  
  a = 0

  #enquanto a arvore tiver uma altura>0
  while(tree.is_empty!=True):
    #pegue a menor distancia(estrutura ja deleta:
    node= tree.get_min_node_alpha()# 1.1
    v_min_index = node.index
    print('node.v.id:',node.v.id)
    #print( 'v_min_index', v_min_index )
    #print(len(vertice_list))
    v_min = vertice_list[v_min_index]
    v_min.visited=True#marque vertice minimo como ja visitado. Desse modo o 1.2 sera feito, pois nao sera mais contado
    #tree.delete(v_min_node.key)
    #para cada vertice adjacente ao vertice minimo
    for i in range(v_min.adj_vert_num):# 1.3
      adj_ver = vertice_list[v_min.adjs[i].id-1]#pega o vertice adjacente 
      #Se a distancia atual do vertice minimo, mais o seu peso, for menor que a distancia do vert adjacente
      if(adj_ver.visited==False and  v_min.dist + v_min.weights[i] < adj_ver.dist ):
        adj_ver.dist = v_min.dist + v_min.weights[i] #a distancia do vertice adjacente tera esse novo valor
        parent[adj_ver.id-1] = v_min.id-1 # a pos que era do vertice adjacente, sera do menor v agora
        tree.alpha_insert(adj_ver,adj_ver.id-1)
  print_solution(vertice_list,vertices,parent,src)    


vertice_list = []

#e = [(1,2),(1,4),(1,6),(2,3),(3,4),(4,5),(5,6),(6,7),(7,2)]
#vertices = 7
#edges = 9

e = [(1,2,7),(1,3,9),(1,6,14),(2,3,10),(2,4,15),(3,4,11),(3,6,2),(4,5,6),(5,6,9)]
vertices = 6
edges = 9


for i in range(vertices):
  #print(i)
  vertice_list.append(create_node_vertice(i,vertices+1)) #crie vertices com suas arestas

for i in range(edges-1):
  #print(i)
  #print(e[i])
  #para cada par de vertices, conecte suas arestas
  insert_adj_in_node(vertice_list[e[i][0]-1],
                    vertice_list[e[i][1]-1],
                    e[i][2],#1 so para o sample
                    vertices)
      
for i in range(vertices):
  print("ver:",vertice_list[i].id+1)
  ver = vertice_list[i]
  for j in range(ver.adj_vert_num):
    print('adjs:',ver.adjs[j].id+1)

print("Dijkstra!!!")
dijkstra(vertice_list, 0, vertices)

"""
for i in range(vertices):
  print("ver:",vertice_list[i].id+1)
  ver = vertice_list[i]
  for j in range(ver.adj_vert_num):
    print('adjs:',ver.adjs[j].id+1)
    print('weight:',ver.weights[j])
"""
