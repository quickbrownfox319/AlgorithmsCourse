#merge sort

#inputList = []
#file = open('filename.txt', 'r')
#inputList.append(file.readline())

test = [6,5,4,3]

def splitList(inputList):
        length = len(inputList)
        result = []
	#base case of 1 element
        if length <= 1:
                return inputList

        leftList = [inputList[i] for i in range(0,length/2)]
        rightList = [inputList[j] for j in range(length/2,length)]
        finalLeft = splitList(leftList)
        print "Left list is {}\n".format(finalLeft)
        finalRight = splitList(rightList)
        print "Right list is{}\n".format(finalRight)
        
        #merge
        if (len(finalLeft) and len(finalRight)) == 1:
                if finalLeft[0] < finalRight[0]:
                        result.append(finalLeft[0])
                        result.append(finalRight[0])
                        return result
                else:
                        #HERE BE INVERSIONS
                        result.append(finalRight[0])
                        result.append(finalLeft[0])
                        return result
#        elif len(finalLeft) != len(finalRight):
        else:
                for i in finalLeft:
                        if finalLeft[i] < finalRight[i]:
                                result.append(finalLeft[i])
                                result.append(finalRight[i])
                                return result
                        else:
                                #HERE BE INVERSIONS
                                result.append(finalRight[i])
                                result.append(finalLeft[i])
                                return result
        print "Merged list {}\n".format(result)

splitList(test)
