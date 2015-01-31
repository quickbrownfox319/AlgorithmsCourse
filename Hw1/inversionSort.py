#merge sort

class MergeSort:
    #inputList = []
    #file = open('filename.txt', 'r')
    #inputList.append(file.readline())
    def __init__(self):
        self.test = [1,2,4,3,5,6]
        self.count = 0
        splitList(test)
        print "Final Count {} ".format(count)

    def __init__(self,file):
        self.inp = []
        self.count = 0

        self.file = open('IntegerArray.txt', 'r')
        inp.append(file.readline())

        splitList(inp)
        print "Final Count {} ".format(count)

    def splitList(inputList):

        ##Splitting Section##
        print "List to be split {}\n".format(inputList)
        length = len(inputList)

        #Base case of 1 element
        if length <= 1:
            return inputList

        #Divide list into halves
        leftList = [inputList[i] for i in range(0,length/2)]
        rightList = [inputList[j] for j in range(length/2,length)]

        #Recursively split left and right lists
        subLeft = splitList(leftList,count)
        subRight = splitList(rightList,count)

        ##Merge Section##
        #Call merge function using recursively split lists
        mergedList = merge(subLeft, subRight, count)
        print "Merged list is {}\n".format(mergedList)

        #Return merged list for next level of merging
        return mergedList

    def merge(left, right):
        result = []

        print "Left List {}\n".format(left)
        print "Right List {}\n".format(right)

        #store lengths of lists
        lenL = len(left) #left
        lenR = len(right) #right
        lenK = lenL + lenR #result

        #Keeps track of progress thru list
        L = 0 #left
        R = 0 #right
        K = 0 #result

        #Keeps result list from overflowing
        while (K < lenK):

            #Checks to see if left or right lists are completed
            #Useful for if one list is completely smaller than other and
            #for odd number of elements in a list
            if (L >= lenL) or (R >= lenR):
                break

            #Compares left list index value to right list index value
            #Appends to resulting list, then increments markers
            if left[L] <= right[R]:
                result.append(left[L])
                L += 1
                K += 1
            elif left[L] >= right[R]:
                result.append(right[R])
                count += 1

                R += 1
                K += 1

        #In the event that one list is completed, fills result list
        #with remainder list
        if L < R:
            for i in range(L,lenL):
                    result.append(left[i])
        else:
            for j in range(R,lenR):
                    result.append(right[j])
                    count += 1
        print "count: {}\n".format(count)
        return result

obj = MergeSort
obj.splitList()