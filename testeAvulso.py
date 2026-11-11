tabela = [65, 83, 59, 28, 72, 90, 2]
def insertionSort(table):
    for i in range(len(table)): #i = 2
        pointer = table[i] #59
        b4 = table[i - 1] #83
        counter = i
        if (i - 1) >= 0: 
            if b4 > pointer: #Só checa os valores
                for x in range(i, 0, -1):
                    if b4 > table[x]:
                        sucessor = table[x]
                        antecessor = table[x - 1]
                        b4 = sucessor
                        table[x] = antecessor
    return table
print(insertionSort(tabela))
