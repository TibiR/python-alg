# Solution 1: Checking Off

def isAnagramChecking(str1, str2):
	run = True
	pos1 = 0
	obj = {}
	while(pos1 < len(str1)):
		pos2 = 0
		found = False
		while(pos2 < len(str2)):
			if( str1[pos1] == str2[pos2] ):
				found = True
			pos2 = pos2 + 1;

		if found:
			obj[str1[pos1]] = True
		else:
			obj[str1[pos1]] = None

		pos1 = pos1 + 1
		pos2 = 0

	print(obj)

isAnagramChecking('abcd','dcba')

# Solution 2: Sort and Compare
def isAnagramSort(str1, str2):
	listA = list(str1)
	listB = list(str2)
	listA.sort()
	listB.sort()
	pos = 0
	match = True
	while pos < len(listA) and match:
		if listA[pos] == listB[pos]:
			pos = pos + 1
		else:
			match = False

	return match


print('response B', isAnagramSort('abcd','dcba'))

