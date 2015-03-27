def pode_ser_valido(data):
    resultados_esperado = len(data) * (len(data)**2 + 1) / 2


    for i in range(len(data)):
        linha = data[i]
        if 0 not in linha and sum(linha) != resultados_esperado:
            return False
        linha = [data[x][i] for x in range(len(data[i]))]
        if 0 not in linha and sum(linha) != resultados_esperado:
            return False
    linha = [data[x][x] for x in range(len(data))]
    if 0 not in linha and sum(linha) != resultados_esperado:
        return False
    linha = [data[len(data) - x - 1][x] for x in range(len(data))]
    if 0 not in linha and sum(linha) != resultados_esperado:
        return False
    return True

def checkio(data, opcoes=None):
    if opcoes is None:
        opcoes = set(range(1, len(data) ** 2 + 1)) - set(x for linha in data for x in linha)

    if all(x != 0 for linha in data for x in linha):
        return data

    x, y = ((x, y) for x in range(len(data)) for y in range(len(data)) if data[x][y] == 0).next()

    for i in opcoes:
        data[x][y] = i

        if pode_ser_valido(data):
            resultado = checkio(data, opcoes - {i})
            if resultado:
                return resultado

    data[x][y] = 0
    return False


if __name__ == '__main__':
    # This part is using only for self-testing.
    def check_solution(func, in_square):
        SIZE_ERROR = "Wrong size of the answer."
        MS_ERROR = "It's not a magic square."
        NORMAL_MS_ERROR = "It's not a normal magic square."
        NOT_BASED_ERROR = "Hm, this square is not based on given template."
        result = func(in_square)
        #check sizes
        N = len(result)
        if len(result) == N:
            for row in result:
                if len(row) != N:
                    print(SIZE_ERROR)
                    return False
        else:
            print(SIZE_ERROR)
            return False
        #check is it a magic square
        # line_sum = (N * (N ** 2 + 1)) / 2
        line_sum = sum(result[0])
        for row in result:
            if sum(row) != line_sum:
                print(MS_ERROR)
                return False
        for col in zip(*result):
            if sum(col) != line_sum:
                print(MS_ERROR)
                return False
        if sum([result[i][i] for i in range(N)]) != line_sum:
            print(MS_ERROR)
            return False
        if sum([result[i][N - i - 1] for i in range(N)]) != line_sum:
            print(MS_ERROR)
            return False

        #check is it normal ms
        good_set = set(range(1, N ** 2 + 1))
        user_set = set([result[i][j] for i in range(N) for j in range(N)])
        if good_set != user_set:
            print(NORMAL_MS_ERROR)
            return False
        #check it is the square based on input
        for i in range(N):
            for j in range(N):
                if in_square[i][j] and in_square[i][j] != result[i][j]:
                    print(NOT_BASED_ERROR)
                    return False
        return True


    assert check_solution(checkio,
                          [[2, 7, 6],
                           [9, 5, 1],
                           [4, 3, 0]]), "1st example"

    assert check_solution(checkio,
                          [[0, 0, 0],
                           [0, 5, 0],
                           [0, 0, 0]]), "2nd example"

    assert check_solution(checkio,
                          [[1, 15, 14, 4],
                           [12, 0, 0, 9],
                           [8, 0, 0, 5],
                           [13, 3, 2, 16]]), "3rd example"
