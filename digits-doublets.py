def filhos(numbers, atual):
    return (x for x in numbers if (sum(1 for i in range(len(atual)) if atual[i] != x[i]) == 1))


def checkio(numbers):
    numbers = [str(x) for x in numbers]
    fronteira = [numbers[0]]
    caminhos, visitados = dict(), set()
    while fronteira:
        atual = fronteira.pop(0)
        if atual == numbers[-1]:
            break
        visitados.add(atual)
        for filho in filhos(numbers, atual):
            if filho not in visitados and filho not in fronteira:
                caminhos[filho] = atual
                fronteira.append(filho)

    ultimo = numbers[-1]
    resposta = [ultimo]
    while ultimo != numbers[0]:
        ultimo = caminhos[ultimo]
        resposta.append(ultimo)
    resposta.reverse()
    print(resposta)
    return [int(i) for i in resposta]

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    #print list(filhos((str(x) for x in [123, 991, 323, 321, 329, 121, 921, 125, 999]), "123"))
    assert checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [123, 121, 921, 991, 999], "First"
    assert checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [111, 121, 127, 727, 777], "Second"
    assert checkio([456, 455, 454, 356, 656, 654]) == [456, 454, 654], "Third, [456, 656, 654] is correct too"


