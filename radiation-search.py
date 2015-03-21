FLAG = -1


def get_filhos(matrix, atual):
    return [(atual[0] + i, atual[1] + j) for i, j in [(0, 1), (1, 0), (-1, 0), (0, -1)] if
            0 <= atual[0] + i < len(matrix) and 0 <= atual[1] + j < len(matrix[0])]


def calcula(matrix, x, y):
    total = 0
    elemento = matrix[x][y]
    fronteira = {(x, y)}
    while fronteira:
        atual = fronteira.pop()
        if matrix[atual[0]][atual[1]] == elemento:
            total += 1
            matrix[atual[0]][ atual[1]] = FLAG
            for filho in get_filhos(matrix, atual):
                fronteira.add(filho)
    return total


def checkio(matrix):
    somas = dict()
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if not matrix[x][y] == FLAG:
                elemento = matrix[x][y]
                somas[elemento] = max(somas.get(elemento, 0), calcula(matrix, x, y))
    return max([[i,k] for k,i in somas.iteritems()])

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [1, 2, 3, 4, 5],
        [1, 1, 1, 2, 3],
        [1, 1, 1, 2, 2],
        [1, 2, 2, 2, 1],
        [1, 1, 1, 1, 1]
    ]) == [14, 1], "14 of 1"

    assert checkio([
        [2, 1, 2, 2, 2, 4],
        [2, 5, 2, 2, 2, 2],
        [2, 5, 4, 2, 2, 2],
        [2, 5, 2, 2, 4, 2],
        [2, 4, 2, 2, 2, 2],
        [2, 2, 4, 4, 2, 2]
    ]) == [19, 2], '19 of 2'