def get_min_distance(vertice_list,num_ver):
  cdef int minimum = 999999999 
  cdef int min_index = 0
  cdef i = 0
  for i in range(num_ver):
    #count_n_operations++;
    if (vertice_list[i].visited == 0 and vertice_list[i].dist <= minimum):
      minimum = vertice_list[i].dist 
      min_index = i
  return vertice_list[min_index];

cdef struct Vals:
    int id 
    int dist
    int visited
    int adj_vert_num
    #self.weights = {}
    #self.adjs = {}