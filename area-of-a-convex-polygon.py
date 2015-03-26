def checkio(data):
    data += [data[0]]
    soma1,soma2=0,0
    for i in range(len(data)-1):
        soma1 += data[i][0]*data[i+1][1]
        soma2 += data[i][1]*data[i+1][0]
    resp = abs((abs(soma1)-abs(soma2))/2.)
    print resp
    return resp


if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio([[1, 1], [9, 9], [9, 1]]), 32), "The half of the square"
    assert almost_equal(checkio([[4, 10], [7, 1], [1, 4]]), 22.5), "Triangle"
    assert almost_equal(checkio([[1, 2], [3, 8], [9, 8], [7, 1]]), 40), "Quadrilateral"
    assert almost_equal(checkio([[3, 3], [2, 7], [5, 9], [8, 7], [7, 3]]), 26), "Pentagon"
    assert almost_equal(checkio([[7, 2], [3, 2], [1, 5], [3, 9], [7, 9], [9, 6]]), 42), "Hexagon"
    assert almost_equal(checkio([[4, 1], [3, 4], [3, 7], [4, 8], [7, 9], [9, 6], [7, 1]]), 35.5), "Heptagon"
