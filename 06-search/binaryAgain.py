import random
def binarySearch(key, table):
    start = 0
    end = len(table) - 1
    comparisons = 0
    while start <= end: #So we can not repeat searches forever!
        mid = (start + end) // 2
        if table[mid] == key:
            comparisons += 1
            return f"{table}\nKey: {key} found on {mid} position.\nComparisons needed: {comparisons}"
        elif table[mid] > key:
            end = mid - 1
            comparisons += 1
        elif table[mid] < key:
            start = mid + 1
            comparisons += 1

    return f"{table}; {key} Key not found!"    

array1 = sorted([random.randint(1,100) for i in range(15)])
array2 = sorted([random.randint(1,100) for i in range(32)])
array3 = sorted([random.randint(1,100) for i in range(50)])

'''print(binarySearch(17, array1))
print(binarySearch(6, array1))
print(binarySearch(25, array1))
print(binarySearch(43, array2))
print(binarySearch(45, array2))
print(binarySearch(98, array2))
print(binarySearch(18, array3))
print(binarySearch(11, array3))
print(binarySearch(16, array3))'''

def bynariComparing(k, t):
    start = 0
    hi = len(t) - 1
    comp = 0
    while start <= hi:
        mid = (start + hi) // 2
        if t[mid] == k:
            comp += 1
            return f"Key at the {mid} idex\nComparisons needed: {comp}"
        elif t[mid] > k:
            hi = mid - 1
            comp += 1
        else:
            start = mid + 1
            comp += 1
        return f"-1. Comparisons: {comp}"

def recursiveBinary(key, table, start = None, stop = None): #O que acontece se eu não definir start e stop = None? Como eu posso driblar isso?
    if start == None:
        start = 0
    if stop == None:
        stop = len(table) - 1
    if start > stop:
        return f"{table} Not found!"
    mid = (start + stop) // 2
    if table[mid] == key:
        return mid
    elif table[mid] > key:
        return recursiveBinary(key, table, start, mid - 1)
    else:
        return recursiveBinary(key, table, mid + 1, stop)
    
print(recursiveBinary(17, array1))

def findRegister(key, keys, registers):
    start = 0
    stop = len(keys) - 1
    while start <= stop:
        mid = (start + stop) // 2
        if keys[mid] == key:
            return registers[mid]
        elif keys[mid] > key:
            stop = mid - 1
        else: # if keys[mid] < key:
            start = mid + 1
    return -1

keys = [10, 20, 30, 40, 50, 60, 70]

records = [
    "Ana", "Bruno", "Carlos", "Daniel",
    "Eduarda", "Felipe", "Gabriela"
]
print(findRegister(70, keys, records))