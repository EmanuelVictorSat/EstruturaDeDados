def transpositionSearch(searchedKey, firstNode):
    a = firstNode
    b = None
    bb = None
    while a != None and a.register().key() != searchedKey:
        bb = b
        b = a
        a = a.next()
    if a == None:
        return None
    if b == None: #Searched key is the first element of the list
        return a.register().key()
    b.next(a.next())
    a.next(b)
    if bb == None: #It also do not need the beforeBefore pointer to hold the list existing
        return a.register().key()
    else:
        bb.next(a)
