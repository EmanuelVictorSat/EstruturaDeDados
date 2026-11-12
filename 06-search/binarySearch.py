def sequentialSearch(searchedKey, table):
    for i in range(len(table)):
        if table[i] == searchedKey:
            return i
    return -1

def searchAndInsert(searchedKey, table):
    for i in range(len(table)):
        if table[i] == searchedKey:
            return i 
    table.append(searchedKey)
    return f"Actual Length: {len(table)}"

answer1 = "100 needed"
answer2 = "Only 1 needed"
answer3 = "Because the binary search only works to sorted lists"

def binarySearch(searchedKey, table):
    start = 0
    stop = len(table) - 1
    while start <= stop:
        middle = (start + stop) // 2
        if table[middle] == searchedKey:
            return middle
        if searchedKey > table[middle]:
            start = middle + 1
            #stop = configured stop
        if searchedKey < table[middle]:
            stop = middle - 1
    return -1

# Teóricas 
# No que diz respeito ao trecho em que o código do while só roda se o limiteInf for superior ao limiteSup, existe um erro na configuração do algorítmo. Isso ocorre porque, se tivermos um caso em que há apenas um elemento, o limiteInf será igual ao limiteSup e o código não roda, então não temos resultado correto para quado a busca precisa ser feita até o último elemento 
# Só passar while limiteInf <= limiteSup

def DecrescentBinarySearch(searchedKey, table):
    start = 0
    stop = len(table) - 1
    while start <= stop:
        middle = (start + stop) // 2
        if table[middle] == searchedKey:
            return middle
        if searchedKey > table[middle]:
            stop = middle - 1
            #stop = configured stop
        if searchedKey < table[middle]:
            start = middle + 1
    return -1

def recursive_binary_search(searched_key, table, start = 0, stop = None):
    if stop == None:
        stop = len(table) - 1
    if start <= stop:
        middle = (start + stop) // 2
        if searched_key == table[middle]:
            return middle
        if searched_key > table[middle]:
            return recursive_binary_search( searched_key, table, middle + 1, stop)
        if searched_key < table[middle]:
            return recursive_binary_search(searched_key, table, start, middle - 1)
    return -1

matriculas = [
    1020, 1045, 1080, 1102, 1140,
    1200, 1250, 1300, 1350, 1400,
    1450, 1500, 1550, 1600, 1650
]
# receives the register
# Show it's position
# Search with binary search algorithm
# Show not existent case
# Count comparisons
def lookForRegister(lookFor, table):
    start = 0
    stop = len(table) - 1
    loops = 0
    while start <= stop:
        middle = (start + stop) // 2
        if table[middle] == lookFor:
            return f"Position: {middle}; loops needed: {loops}"
        if lookFor > table[middle]:
            start = middle + 1
        if lookFor < table[middle]:
            stop = middle - 1
        loops += 1
    return f"Loops: {loops}; -1"

print(lookForRegister(1650, matriculas))