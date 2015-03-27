SOMA = 0
def somar(n):
    global SOMA
    SOMA += n
def checkio(data):
    global SOMA
    SOMA = 0
    map(somar,data)
    return SOMA
