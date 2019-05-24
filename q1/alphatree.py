
class AlphaTreeNode:
	def __init__(self, key, cost, parent):
		self.keys = []
		self.keys.append(key)
		self.key = key
		self.cost = cost
		self.parent= parent
		self.size = 1
		#self.index = index
		self.left = None
		self.right = None

	#public AlphaTreeNode(AlphaTreeNode node):
	#	self.setCost(node.getCost())
	#	self.setKeys(node.getKeys())
	#

	def increaseSize(self):
		self.size+=1

	def decreaseSize(self):
		self.size-=1

	def getSizeRight(self):
		if (self.getRight() == None):
			return 0
		else:
			return self.getRight().size

	def getSizeLeft(self):
		if (self.getLeft() == None):
			return 0
		else:
			return self.getLeft().size

	def insertKey(self,key):
		self.keys.append(key)

	def getKeys(self):
		return self.keys

	def setKeys(self,keys):
		self.keys = keys

	def getCost(self):
		return self.cost

	def setCost(self, cost):
		self.cost = cost

	def getParent(self):
		return self.parent

	def setParent(self,parent):
		self.parent = parent

	def getLeft(self):
		return self.left

	def setLeft(self,left):
		self.left = left

	def getRight(self):
		return self.right

	def setRight(self,right):
		self.right = right

	def getSize(self):
		return self.size

	def setSize(self,size):
		self.size = size

class AlphaTree:

	def __init__(self):
		self.alpha = 0.7
		self.setRoot(None)

	def insert(self,key,cost):
		if (self.root == None):
			self.root = AlphaTreeNode(key, cost, None)
		else:
			nodeRoot = self.root
			while(True):
				if (nodeRoot.getCost() == cost):
					nodeRoot.insertKey(key)
					return

				parent = nodeRoot

				goLeft = nodeRoot.getCost() > cost
				if(goLeft):
					nodeRoot = nodeRoot.getLeft()
				else:
					nodeRoot = nodeRoot.getRight()
				#nodeRoot = goLeft ? nodeRoot.getLeft(): nodeRoot.getRight()

				if (nodeRoot == None):
					nodeAdd = AlphaTreeNode(key, cost, parent)
					if (goLeft):
						parent.setLeft(nodeAdd)
					else: 
						parent.setRight(nodeAdd)
					self.updateSizesInsert(nodeAdd)
					break

	def updateSizesInsert(self,nodeAdd):
		nodeNotBalance = None
		node = nodeAdd.getParent()
		while (node is not None):
			node.increaseSize()
			cond1 = node.getSizeLeft() <= (self.alpha*node.getSize())
			cond2 = node.getSizeRight() <= (self.alpha*node.getSize())

			if(cond1 and cond2 == False ):
				nodeNotBalance = node
			node = node.getParent()
		self.rebuidTree(nodeNotBalance)

	def updateSizesDelete(self,nodeDel):
		nodeNotBalance = None
		node = nodeDel.getParent()
		while (node is not None):
			node.decreaseSize()

			cond1 = node.getSizeLeft() <= (self.alpha*node.getSize())
			cond2 = node.getSizeRight() <= (self.alpha*node.getSize())

			if(cond1 and cond2 == False ):
				nodeNotBalance = node
			node = node.getParent()
		self.rebuidTree(nodeNotBalance)

	def rebuidTree(self,nodeRoot):
		if (nodeRoot is not None):

			array = None

			leftChild = False
			isRoot = False

			nodeParent = None

			if (nodeRoot.getParent() == None):
				isRoot = True
			elif ((nodeRoot.getParent().getRight() is not None ) and (nodeRoot.getParent().getRight() == nodeRoot) ):
				leftChild = False
				nodeParent = nodeRoot.getParent()
			else:
				leftChild = True
				nodeParent = nodeRoot.getParent()
			

			if (nodeRoot is not None):
				l = []
				l = self.extractValues(nodeRoot,l)

				#array = AlphaTreeNode(len(l))
				array = []
				for i in range(0,len(l)):
					node = l[i]
					print(node)
					array.append( AlphaTreeNode(node.cost,node.key,node.parent) )
				

				node = self.rebuildTree(array, 0, len(array) - 1)

				if (isRoot==False):
					if (leftChild):
						node.setParent(nodeParent)
						nodeParent.setLeft(node)
					else:
						node.setParent(nodeParent)
						nodeParent.setRight(node)
					
				else:
					self.root = node

	def rebuildTree(self,array,start,end):
		print(start,end)

		if (start > end):
			return None
		else:
			indexRoot = (start + end) // 2
			size = end - start + 1

			node = array[indexRoot]
			node.setSize(size)

			left = self.rebuildTree(array, start, indexRoot - 1)
			right = self.rebuildTree(array, indexRoot + 1, end)

			if (left is not None):
				left.setParent(node)
			
			if (right is not None):
				right.setParent(node)
			
			node.setLeft(left)
			node.setRight(right)

			return node

	def extractValues(self,node,result):
		
		if (node.getLeft() is not None):
			self.extractValues(node.getLeft(),result)
		result.append(node)
		if (node.getRight() is not None):
			self.extractValues(node.getRight(),result)
		return result
	
	def delete(self,node):
		if (node.getLeft() == None and node.getRight() == None):
			if (node.getParent() == None):
				self.root = None
			else:
				parent = node.getParent()
				if (parent.getLeft() == node):
					parent.setLeft(None)
				else:
					parent.setRight(None)
			return
		
		if (node.getLeft() is not None):
			child = node.getLeft()
			child.decreaseSize()
			while (child.getRight() is not None):
				child = child.getRight()
			node.setCost(child.getCost())
			node.setKeys(child.getKeys())
			node.decreaseSize()
			self.delete(child)
		else:
			child = node.getRight()
			child.decreaseSize()
			while (child.getLeft() is not None):
				child = child.getLeft()
			node.setCost(child.getCost())
			node.setKeys(child.getKeys())
			node.decreaseSize()
			self.delete(child)
		
	def deleteCost(self,delCost):
		if (self.root == None):
			return
		node = self.root
		child = self.root

		while (child is not None):
			node = child
			if(delCost >= node.getCost()):
				child = node.getRight()
			else:
				child = node.getLeft()
			#child = delCost >= node.getCost(): node.getRight(): node.getLeft()
			if (delCost == node.getCost()):
				self.delete(node)
				self.updateSizesDelete(node)
				return

	def getMin(self):
		if (self.root == None):
			#return -1
			raise IndexError
		else:			
			node = self.root
			while (True):
				if (node.getLeft() == None):
					keys = node.getKeys()
					print('keys',keys)
					menor = keys[0]
					del keys[0]
					#node.getKeys().remove(0)

					if (len(node.getKeys()) == 0):
						self.deleteCost(node.getCost())
					return menor
				else:
					node = node.getLeft()
				
	def findKey(self,key):
		if (self.root == None):
			return -1
		else:
			node = self.root
			while(True):
				if(node == None):
					return -1
				if(node.getCost() > key):
					node = node.getLeft()
				elif (node.getCost() < key):
					node = node.getRight()
				else:
					return node.getKeys()[0]
				
	def findKeyAndUpdate(self,key, cost):
		if (self.root == None):
			return
		else:
			node = self.root
			while (True):
				if (node == None):
					return
				if (node.getCost() > key):
					node = node.getLeft()
				elif (node.getCost() < key):
					node = node.getRight()
				else:
					keys = node.getKeys() 
					del keys[0]
					keys.append(cost)
					return

	def getRoot(self):
		return self.root

	def setRoot(self,root):
		self.root = root
	"""
	public void printCost():
		printCost(self.root)
		System.out.println()
	

	private void printCost(AlphaTreeNode node):
		if (node is not None):
			printCost(node.getLeft())
			System.out.printf("%s ", node.getCost())
			printCost(node.getRight())
		
	

	public void printSize():
		printSize(self.root)
		System.out.println()
	

	private void printSize(AlphaTreeNode node):
		if (node is not None):
			printSize(node.getLeft())
			System.out.printf("%s ", node.getSize())
			printSize(node.getRight())
		
	
	"""