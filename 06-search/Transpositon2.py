tabela = [1,2,3,4,5,6,7,20]
def transpositionSearch(key, table):
    for i in range(len(table)):
        if table[i] == key:
            if i > 0:
                hold = table[i - 1]
                table[i - 1] = table[i]
                table[i] = hold 
            else:
                return table
    return table
print(transpositionSearch(20, tabela))
print(transpositionSearch(7, tabela))
print(transpositionSearch(7, tabela))
print(transpositionSearch(7, tabela))
print(transpositionSearch(7, tabela))
print(transpositionSearch(2, tabela))
print(transpositionSearch(2, tabela))
print(transpositionSearch(5, tabela))
print(transpositionSearch(5, tabela))
