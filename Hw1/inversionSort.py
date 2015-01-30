#merge sort

#inputList = []
#file = open('filename.txt', 'r')
#inputList.append(file.readline())

test = [6,5,4,3,2,1]

def splitList(inputList):
        length = len(inputList)
        result = []
	#base case of 1 element
        if length <= 1:
                return inputList

        leftList = [inputList[i] for i in range(0,length/2)]
        rightList = [inputList[j] for j in range(length/2,length)]
        splitList(leftList)
        print "Left list is {}\n".format(leftList)
        splitList(rightList)
        print "Right list is{}\n".format(rightList)
        
        #merge
        if (len(leftList) and len(rightList)) == 1:
                if leftList[0] < rightList[0]:
                        result.append(leftList[0])
                        result.append(rightList[0])
                else:
                        #HERE BE INVERSIONS
                        result.append(rightList[0])
                        result.append(leftList[0])
#        elif len(leftList) != len(rightList):
        else:
                for i in leftList:
                        if leftList[i] < rightList[i]:
                                result.append(leftList[i])
                                result.append(rightList[i])
                        else:
                                #HERE BE INVERSIONS
                                result.append(rightList[i])
                                result.append(leftList[i])
        print "Merged list {}\n".format(result)

splitList(test)
