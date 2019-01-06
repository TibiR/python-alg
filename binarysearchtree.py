class Node(object):
	def __init__(self, data):
		self.data = data;
		self.leftChild = None;
		self.rightChild = None;

	def insert(self, data):
		if data < self.data:
			if not self.leftChild:
				self.leftChild = Node(data)
			else:
				self.leftChild.insert(data)
		else:
			if not self.rightChild:
				self.rightChild = Node(data)
			else:
				self.rightChild.insert(data)

	def getMin(self):
		if self.leftChild is None:
			print(self.data)
			return self.data
		else:
			return self.leftChild.getMin()

	def getMax(self):
		if self.rightChild is None:
			print(self.data)
			return self.data
		else:
			return self.rightChild.getMax()

	# 1 - go left
	# 2 - print
	# 3 - go right
	def traverseInOrder(self):
		if self.leftChild is not None:
			self.leftChild.traverseInOrder();

		print(self.data);

		if self.rightChild is not None:
			self.rightChild.traverseInOrder()

node = Node(20)
node.insert(15)
node.insert(16)
node.insert(14)
node.insert(21)
node.traverseInOrder()
# node.getMin()
# node.getMax()


