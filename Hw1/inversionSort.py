#merge sort

#inputList = []
#file = open('filename.txt', 'r')
#inputList.append(file.readline())

test = [3,1,2,6,5]

def splitList(inputList):
        length = len(inputList)
        
	#base case of 1 element
        if length <= 1:
                return inputList

        #if length % 2 == 0:
        leftList = [inputList[i] for i in range(0,length/2)]
        rightList = [inputList[j] for j in range(length/2,length)]
        splitList(leftList)
        print "Left list is {}\n".format(leftList)
        splitList(rightList)
        print "Right list is{}\n".format(rightList)
        mergedList = merge(leftList,rightList)
        print "Merged list {}\n".format(mergedList)

def merge(right,left):
        result = [] #will be merged result

        if (len(left) and len(right)) == 1:
                if left[0] < right[0]:
                        result.append(left[0])
                        result.append(right[0])
                else:
                        result.append(right[0])
                        result.append(left[0])
        elif len(left) != len(right):
                
        
        else:
                for i in left:
                        if left[i] < right[i]:
                                result.append(left[i])
                                result.append(right[i])
                        else:
                                result.append(right[i])
                                result.append(left[i])
        return result

splitList(test)
