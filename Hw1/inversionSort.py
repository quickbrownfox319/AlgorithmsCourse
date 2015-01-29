#merge sort

inputList = []
file = open('filename.txt', 'r')
inputList.append(file.readline())

def splitList(inputList):
	#base case of 1 element
	if len(inputList) == 1:
		return inputList

	#even list case
	if len(inputList) % 2 == 0:
		leftList[i for i in inputList[:len(inputList)/2]