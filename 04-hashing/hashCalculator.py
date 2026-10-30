# Chat exercises
def hash_code(key, listSize):
    hash = key % listSize
    return hash
def registrationHashCalculator(registration, size):
    n = str(registration)
    d = int(n[-2])
    u = int(n[-1])
    
    key = d + u
    return key % size
