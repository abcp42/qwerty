from dll import DoublyLinkedList
class Bucket:
  def __init__(self,maxPath):
    self.size = maxPath;
    self.count = 0;
    self.lastPos =0;
    self.buckets = []
    for i in range(maxPath):
      self.buckets.append([None,i]) #list and node index

  def add(self,v):
    if(self.buckets[v[0]][0] == None):
        self.buckets[v[0]][0] = DoublyLinkedList()
    dist_dll = self.buckets[v[0]][0]
    dist_dll.push(v)
    self.count+=1

  def isEmpty(self):
    if(self.count <= 0):
      return True
    return False;

  def remove_min(self):
    n_op = 0
    for i in range(self.lastPos, self.size):
        #print('i:',i)
        #print('self.lastPos:',self.lastPos)
        #print('self.size:',self.size)
        if(self.buckets[i][0] != None):
          #print('getlast')
          node = self.buckets[i][0].getLast()# O(n)?
          #print(node.data)
          min_vert = node.data
          if(min_vert!= None): 
            #print('min_vert != none')   
            #print(node.next)        
            self.buckets[i][0].remove(node)
            if(self.buckets[i][0].head==None):
              self.buckets[i][0] = None
            self.count-=1
            #self.lastPos = i+1#gambiarra
            self.lastPos = i
          else:
             self.buckets[i][0]=None
          return min_vert
    return None