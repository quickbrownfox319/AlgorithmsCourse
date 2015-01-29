#merge sort

#inputList = []
#file = open('filename.txt', 'r')
#inputList.append(file.readline())

inputList = [1,2,3,4]

def splitList(inputList):
	#base case of 1 element
	if len(inputList) == 1:
		return inputList

	#even list case
	if len(inputList) % 2 == 0:
		leftList = [inputList[i] for i in range(0,len(inputList)/2)]
		rightList = [inputList[j] for j in range(len(inputList)/2,len(inputList))]
		print leftList
		print rightList