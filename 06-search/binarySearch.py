def binarySearch(myList, item, begin, end):
    if begin <= end:
        middle = (begin + end) // 2
    if myList[middle] == item:
        return myList[middle]
    if item > myList[middle]:
        return binarySearch(myList, item, middle + 1,end)
    if item < myList[middle]:
        return binarySearch(myList, item, begin, myList[middle] - 1)
    return "Não está na lista"
