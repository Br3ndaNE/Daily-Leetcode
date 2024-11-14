list1 = [1,2,4]
list2 = [1,3,4]

def mergeTwoLists(list1, list2):
    returnList = []
    for i in range(len(list1)):
        if(list1[i] <= list2[i]):
            returnList.append(list1[i])
            returnList.append(list2[i])
        else:
            returnList.append(list2[i])
            returnList.append(list1[i])
    return returnList




print(mergeTwoLists(list1,list2))