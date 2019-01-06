# Sequntial searh

# 1
def sequential(list, item):
	found = False
	pos = 0
	while pos < len(list) and not found:
		if list[pos] == item:
			found = True
			print (list[pos])
		else:
			pos = pos + 1

sequential([3,4,6,12,66,16,7,100], 66)

# 2 in order list

def sequentialOrder(list, item):
	found = False
	stop = False
	pos = 0

	while pos < len(list) and not found and not stop:
		if list[pos] == item:
			found = True
			print(list[pos])
		else:
			if list[pos] > item:
				stop = True
				print('Not found')
			else:
				pos = pos + 1

sequentialOrder([1,2,3,4,5,6,7,8,10,11], 9)


# BinarySearch 

# 1
def binarySearch(list, item):
	first = 0
	last = len(list) - 1
	found = False

	while first <= last and not found:
		middle = (first + last) // 2
		if(list[middle] == item):
			found = True
			print(list[middle])
		else:
			if item < list[middle]:
				last = middle - 1
			else:
				first = middle + 1

	return found

binarySearch([1,2,3,4,5,6,7,8,9,10], 3)

# 2 binary search with divide and conquer

def binaryConquer(alist, item):
	if len(alist) == 0:
		return False
	else:
		middle = len(alist)//2
		if alist[middle] == item:
			print(alist[middle])
			return True
		else:
			if item < alist[middle]:
				return binaryConquer(alist[:middle], item)
			else:
				return binaryConquer(alist[middle+1:], item)

binaryConquer([1,2,3,4,5,6,7,8,9,10], 8)
