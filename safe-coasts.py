from pprint import pprint


def finish_map(regional_map):
    regional_map = [list(linha) for linha in regional_map]
    visinhos = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]
    # encontra locais safe proximos a costa
    for i in range(len(regional_map)):
        for j in range(len(regional_map[i])):
            if regional_map[i][j] == "X":
                for vx, vy in visinhos:
                    if 0 <= i + vx < len(regional_map) and 0 <= j + vy < len(regional_map[i]) and regional_map[i + vx][
                                j + vy] == ".":
                        regional_map[i + vx][j + vy] = "S"

    # expande locais perigosos
    for x, y in ((x, y) for x in range(len(regional_map)) for y in range(len(regional_map[x])) if
                 regional_map[x][y] == "D"):
        fronteira = {(x, y)}

        while fronteira:
            atualx, atualy = fronteira.pop()
            regional_map[atualx][atualy] = "D"
            fronteira |= set((atualx + i, j + atualy) for (i, j) in [(0,1),(0,-1),(-1,0),(1,0)] if
                             0 <= i + atualx < len(regional_map) and 0 <= j + atualy < len(regional_map[i]) and
                             regional_map[atualx + i][j + atualy] == ".")

    #define o restante como safe
    regional_map = ["".join([ponto if ponto != "." else "S" for ponto in linha]) for linha in regional_map]
    pprint(regional_map)
    return regional_map


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(finish_map(("D..", "...", "...")), (list, tuple)), "List or tuple"
    assert list(finish_map(("D..XX.....",
                            "...X......",
                            ".......X..",
                            ".......X..",
                            "...X...X..",
                            "...XXXXX..",
                            "X.........",
                            "..X.......",
                            "..........",
                            "D...X....D"))) == ["DDSXXSDDDD",
                                                "DDSXSSSSSD",
                                                "DDSSSSSXSD",
                                                "DDSSSSSXSD",
                                                "DDSXSSSXSD",
                                                "SSSXXXXXSD",
                                                "XSSSSSSSSD",
                                                "SSXSDDDDDD",
                                                "DSSSSSDDDD",
                                                "DDDSXSDDDD"], "Example"
    assert list(finish_map(("........",
                            "........",
                            "X.X..X.X",
                            "........",
                            "...D....",
                            "........",
                            "X.X..X.X",
                            "........",
                            "........",))) == ["SSSSSSSS",
                                               "SSSSSSSS",
                                               "XSXSSXSX",
                                               "SSSSSSSS",
                                               "DDDDDDDD",
                                               "SSSSSSSS",
                                               'XSXSSXSX',
                                               "SSSSSSSS",
                                               "SSSSSSSS"], "Walls"
    assert finish_map(("..........", ".D.......X", "..........", "..........", "......X...", "..........", "..........",
                       "...X......", "..........", "..........", "X.........")) == ["DDDDDDDDSS", "DDDDDDDDSX",
                                                                                   "DDDDDDDDSS", "DDDDDSSSSS",
                                                                                   "DDDDDSXSSS", "DDDDDSSSSS",
                                                                                   "DDSSSSSSSS", "DDSXSSSSSS",
                                                                                   "DDSSSSSSSS", "SSSSSSSSSS",
                                                                                   "XSSSSSSSSS"], "last"