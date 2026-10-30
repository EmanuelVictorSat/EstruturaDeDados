def Palindrome(string):
    palavra = Pilha()
    compare = ''
    comEssa = ''
    for i in string:
        if ord(i) >= 65 and ord(i) <= 90 or ord(i) >= 97 and ord(i) <= 122:
            obj = No(i)
            palavra.empilhar(obj)
            comEssa += i
    top = palavra.top
    while top is not None:
        compare += top.data
        top = top.next
    if compare == comEssa:
        return True
    return False
