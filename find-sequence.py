from itertools import groupby
def check(linha):
    linha = list(linha)
    print linha
    for i,k in groupby(linha):
        grupo = list(k)

        if len(grupo) > 3:
            return True
    return False


def checkio(matrix):
    return any(
        (
            check(matrix[i])
            or check(matrix[x][i] for x in range(len(matrix)))
            or check(matrix[x + i][x] for x in range(len(matrix)) if x + i<len(matrix))
            or check(matrix[x][x + i] for x in range(len(matrix)) if x + i<len(matrix))

            or check(matrix[i-x][x] for x in range(len(matrix)) if 0<=i-x  )
            or check(matrix[len(matrix)-1-x][i+x] for x in range(len(matrix)) if i+x < len(matrix) and len(matrix)-x-1 > 0 )
        )
        for i in range(len(matrix))
    )


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
    assert checkio([
        [1,5,4,4],
        [2,2,4,1],
        [1,4,3,5],
        [4,3,3,2]]) == True