def visinhos(region, ponto):
    x, y = ponto
    NEIGHS = ((-1, 0), (1, 0), (0, 1), (0, -1))
    return [region[x + i][y + j] for (i, j) in NEIGHS if
            0 <= x + i < len(region) and 0 <= y + j < len(region[0]) and region[x + i][y + j] != region[x][y]]


def extrai_grafo(region):
    grafo = dict()
    for i in range(len(region)):
        for j in range(len(region[0])):
            grafo[region[i][j]] = grafo.get(region[i][j], set()) | set(visinhos(region, (i, j)))
    return grafo


def conflitos(grafo, mapa_cores):
    total = 0
    for regiao, visinhos in grafo.items():
        total += len([v for v in visinhos if mapa_cores[regiao] == mapa_cores[v]])
    return total


def conflitos_regiao(grafo, mapa_cores, regiao):
    return sum(1 for v in grafo[regiao] if mapa_cores[regiao] == mapa_cores[v])


def esta_conflitante(grafo, mapa_cores, regiao):
    return any(mapa_cores[regiao] == mapa_cores[visinho] for visinho in grafo[regiao])


def backtrack(grafo, mapa_cores):

    if all(x!=0 for x in mapa_cores):
        return mapa_cores

    for cor in [1, 2, 3, 4]:
        novo_mapa = mapa_cores[:]
        posicao_atual = novo_mapa.index(0)
        novo_mapa[posicao_atual] = cor
        print novo_mapa
        if not esta_conflitante(grafo,novo_mapa, posicao_atual):
            resp = backtrack(grafo,novo_mapa)
            if resp:
                return resp
    return False


def color_map(region):
    CORES = [1, 2, 3, 4]
    grafo = extrai_grafo(region)
    print grafo
    n_regions = len(set(i for linha in region for i in linha))
    mapa_cores = [0] * n_regions

    return backtrack(grafo,mapa_cores)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    NEIGHS = ((-1, 0), (1, 0), (0, 1), (0, -1))
    COLORS = (1, 2, 3, 4)
    ERROR_NOT_FOUND = "Didn't find a color for the country {}"
    ERROR_WRONG_COLOR = "I don't know about the color {}"

    def checker(func, region):
        user_result = func(region)
        if not isinstance(user_result, (tuple, list)):
            print("The result must be a tuple or a list")
            return False
        country_set = set()
        for i, row in enumerate(region):
            for j, cell in enumerate(row):
                country_set.add(cell)
                neighbours = []
                if j < len(row) - 1:
                    neighbours.append(region[i][j + 1])
                if i < len(region) - 1:
                    neighbours.append(region[i + 1][j])
                try:
                    cell_color = user_result[cell]
                except IndexError:
                    print(ERROR_NOT_FOUND.format(cell))
                    return False
                if cell_color not in COLORS:
                    print(ERROR_WRONG_COLOR.format(cell_color))
                    return False
                for n in neighbours:
                    try:
                        n_color = user_result[n]
                    except IndexError:
                        print(ERROR_NOT_FOUND.format(n))
                        return False
                    if cell != n and cell_color == n_color:
                        print("Same color neighbours.", cell, n)
                        return False
        if len(country_set) != len(user_result):
            print("Excess colors in the result")
            return False
        return True

    checker(color_map, (
        (13, 13, 13, 13, 13, 13, 14, 14, 14, 14,), (13, 0, 0, 1, 1, 2, 2, 3, 3, 14,), (13, 4, 5, 5, 6, 6, 7, 7, 8, 14,),
        (13, 9, 9, 10, 10, 11, 11, 12, 12, 14,), (13, 13, 13, 13, 14, 14, 14, 14, 14, 14,),))