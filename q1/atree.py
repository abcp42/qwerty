
class Node:
	def __init__(self):
		self.min = None
		self.min_index = -1
		self.index = 0
		self.v = None
	
class AlphaTreeNode:
	def __init__(self):
		self.pivot = 0
		self.vertices = []
		self.count = 0 
		self.size = 1
		self.index = 0
		self.left = None
		self.right = None
		self.size+=1

class AlphaTree:
	def __init__(self):
		self.root = None
		self.is_empty = False
		self.alpha = 0.8

	def get_min_node(self,verts,nodeit = None,index = 0):
		if(nodeit == None):
			nodeit = Node()
			nodeit.min=99999999999999999
			nodeit.min_index=-1
			nodeit.v = None
		for v in verts:
			if(v is not None):
				if(v.visited == False and v.dist<nodeit.min):
					nodeit.min = v.dist
					nodeit.min_index = v.id
					nodeit.v = v
		return nodeit

	def alpha_balance_node(self,node):
		print('alpha_balance_node')
		if(node.left is not None):
			if(node.left.size > self.alpha*node.size):
				#balance_count++
				self.alpha_balance_node(node.left) 
				nodeit = self.get_min_node(node.left.vertices)
				if(nodeit.v is not None):
					#node.left.vertices = g_slist_remove(node.left.vertices, nodeit.v)
					print("REMOVING FROM LEFT:",nodeit.v.id,", ",nodeit.v)
					node.left.vertices.remove(nodeit.v)
					node.left.count-=1
					#node.vertices = g_slist_append(node.vertices, nodeit.v) 
					print("APPEND: ",nodeit.v.id, ", ",nodeit.v)
					node.vertices.append(nodeit.v)
					node.count+=1
				else:
					node.left=None  
		if(node.right is not None):
			if(node.right.size > self.alpha*node.size):
				self.alpha_balance_node(node.right) 
				nodeit = self.get_min_node(node.right.vertices)
				if(nodeit.v is not None):
					print("REMOVING FROM RIGHT:",nodeit.v.id,", ",nodeit.v)
					node.right.vertices.remove(nodeit.v)
					node.right.count-=1
					print("APPEND: ",nodeit.v.id, ", ",nodeit.v)
					node.vertices.append(nodeit.v)
					node.count+=1
				else:
					node.right=None 
		
	def alpha_update_nodes_size(self,node, height):
		if(node.left is None and node.right is None):
			node.size=1

		size =1
		if(node.left is not None):
			self.alpha_update_nodes_size(node.left,height+1)
			size += node.left.size

		if(node.right is not None):
			self.alpha_update_nodes_size(node.right,height+1)
			size += node.right.size
		node.size=size 

		if(height > self.cur_height):
			self.cur_height = height


	def alpha_balance(self):
		self.alpha_balance_node(self.root)
		self.alpha_update_nodes_size(self.root,1)

	def alpha_node_add(self,node, v,index):
		if(node is None):
			return
		node.pivot+= v.dist//2
		print("APPEND: ",v.id, ", ",v)
		node.vertices.append(v)
		print("Vertices: ",node.vertices)
		node.count+=1 
		node.index = index

	def calcule_min_node(self,node, nodeit):
		print('calcule_min_node')
		nodeit = self.get_min_node(node.vertices,nodeit)		
		if(node.left is not None):
			node,nodeit = self.calcule_min_node(node.left, nodeit)
		if(node.right is not None):
			node,nodeit = self.calcule_min_node(node.right, nodeit)
		print(nodeit.min)
		print(nodeit.min_index)
		print(nodeit.v.id)
		print('**',node.vertices)
		#a = 2/0
		return node,nodeit

	def get_min_node_alpha(self):
		print('get_min_node_alpha')
		target = self.root

		nodeit = Node()
		nodeit.min=99999999999
		nodeit.min_index=-1
		nodeit.v= None
		target,nodeit = self.calcule_min_node(target, nodeit)
		
		#a = 2/0
		if(nodeit.min_index <0):
			self.is_empty=True
			print('Tree Empty!!')
		print('To remove:')
		print(nodeit.min)
		print(nodeit.min_index)
		print(nodeit.v.id)
		print('nodeit v: ',nodeit.v)
		print([v.id for v in target.vertices])
		if(nodeit.v is not None):
			print("REMOVING")

			print(target.vertices)
			target.vertices.remove(nodeit.v)
		return nodeit

	def alpha_insert(self,v,index):
		print('alpha_insert')
		#target=None  
		#last=None 

		if(self.root  is  None):
			self.root = AlphaTreeNode()
			target = self.root  	
		else:
			target = self.root

			while(target is not None):

				if( v.dist < target.pivot ):
					if(target.count < target.size):
						break
					else:
						last = target  
						target = target.left
						if(target is None):
							target = AlphaTreeNode()
							last.left = target
							break

				else:
					if(target.count < target.size):
						break
					else:
						last = target 
						target = target.right
						if(target is None):
							target = AlphaTreeNode()
							last.right = target
							break
		self.alpha_node_add(target,v,index)	
		self.cur_height=0
		self.alpha_update_nodes_size(self.root,1)
		self.alpha_balance()
		
		print(target.count)
		print(target.size)
		print(target.pivot)
		print(target.left)
		print(target.right)
		print(target.index)
		print(target.vertices)

		print("****",self.root.vertices)




