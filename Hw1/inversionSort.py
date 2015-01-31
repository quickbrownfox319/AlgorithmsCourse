#merge sort

#inputList = []
#file = open('filename.txt', 'r')
#inputList.append(file.readline())

test = [6,5,4,3]

def splitList(inputList):
        length = len(inputList)

	#base case of 1 element
        if length <= 1:
                return inputList

        leftList = [inputList[i] for i in range(0,length/2)]
        rightList = [inputList[j] for j in range(length/2,length)]
        subLeft = splitList(leftList)
        print "Left list is {}\n".format(subLeft)
        subRight = splitList(rightList)
        print "Right list is {}\n".format(subRight)
        mergedList = merge(subLeft, subRight)
        print "Merged list is {}\n".format(mergedList)
        return mergedList


def merge(left, right):
        result = []
        print "LEFT = {}".format(left)
        print "RIGHT = {}".format(right)
        #for base case elements of 1
        if (len(left) and len(right)) == 1:
                if left[0] < right[0]:
                        result.append(left[0])
                        result.append(right[0])
                else:
                        #HERE BE INVERSIONS
                        result.append(right[0])
                        result.append(left[0])
        elif len(left) == len(right):
                for i in range(0,len(left)-1):
                        if left[i] < right[i]:
                                result.append(left[i])
                                result.append(right[i])
                        else:
                                #HERE BE INVERSIONS
                                result.append(right[i])
                                result.append(left[i])
        return result                    



splitList(test)
