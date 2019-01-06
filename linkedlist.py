class Node:
	def __init__(self, initdata):
		self.data = initdata
		self.nextNode = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.nextNode

	def setData(self, newData):
		self.data = newData

	def setNext(self, nextData):
		self.nextNode = nextData

class UnorderLinkedList:
	def __init__(self):
		self.head = None

	def addNode(self, data):
		if self.head is None:
			self.head = Node(data)
		else:
			temp = Node(data)
			temp.setNext(self.head)
			self.head = temp

	def readData(self):
		current = self.head
		while current is not None:
			print(current.data)
			current = current.getNext()

	def searchItem(self, item):
		current = self.head
		found = False
		while current is not None and not found:
			if current.getData() == item:
				found = True
				print(item, ' -> ', current.data)
			else:
				current = current.getNext()

		if found is False:
			print('Element doesn t exit')

	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()

		if previous is None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())

mylist = UnorderLinkedList()
mylist.addNode(5)
mylist.addNode(6)
mylist.addNode(7)
mylist.readData()
mylist.searchItem(5)
mylist.remove(6)
print('after delete')
mylist.readData()


