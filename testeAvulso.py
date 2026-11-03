def hashMAtricula(matricula, size):
    m = str(matricula)
    u = m[-1]
    d = m[-2]
    key = int(d+u)
    return key % size