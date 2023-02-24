# Twin towers
# longest sub sequence or sth

def LCS(X, Y):
    UPPERLEFT = 1
    UP = 2
    LEFT = 3

    m = len(X)
    n = len(Y)

    c = [[0 for j in range(0, n + 1)] for i in range(0, m + 1)]
    b = [[0 for j in range(0, n + 1)] for i in range(0, m + 1)]

    for i in range(1, m + 1):
        c[i][0] = 0

    for j in range(1, n + 1):
        c[0][j] = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = UPPERLEFT
            else:
                if c[i - 1][j] >= c[i][j - 1]:
                    c[i][j] = c[i - 1][j]
                    b[i][j] = UP
                else:
                    c[i][j] = c[i][j - 1]
                    b[i][j] = LEFT

    i = m
    j = n
    result = []
    while i != 0 and j != 0:
        if b[i][j] == UPPERLEFT:
            result.append(X[i - 1])
            i -= 1
            j -= 1
        elif b[i][j] == UP:
            i -= 1
        else:
            j -= 1

    return result

if __name__ == '__main__':
    run = True
    counter = 1
    while run :
        heights = input("兩塔高度:")
        heights = list( map( int, heights.split() ) )
        if heights[0] == 0 and heights[1] == 0:
            run = False
        else:
            tower1 = input("tower1: ")
            tower2 = input("tower2: ")
            tower1 = list( map( int, tower1.split()))
            tower2 = list( map( int, tower2.split()))
            print( "Twin Towers #" + str(counter) )
            counter = counter + 1
            print( "Number of Tiles: " + str(len( LCS(tower1, tower2) ) ) )
