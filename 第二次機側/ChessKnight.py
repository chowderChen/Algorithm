# Chess knight

import queue

def translateIndex(char):
    # 將輸入座標英文部分轉為數字
    if char == 'a':
        return 1
    elif char == 'b':
        return 2
    elif char == 'c':
        return 3
    elif char == 'd':
        return 4
    elif char == 'e':
        return 5
    elif char == 'f':
        return 6
    elif char == 'g':
        return 7
    elif char == 'h':
        return 8

def BFS( startLoc, endLoc):
    q = queue.Queue()
    tmpQ = queue.Queue()
    visited = [ [ False for i in range(9)] for j in range(9)]  # 避免重複走訪
    q.put(startLoc)
    moveCount = 0

    while not q.empty() :
        loc = q.get()
        if loc[0] == endLoc[0] and loc[1] == endLoc[1]:
            return moveCount

        visited[ loc[0] ][ loc[1] ] = True

        # 如果loc和目標座標不符，則將loc所有可能的下一步加入queue
        if loc[0] + 1 <= 8:
            if loc[1] + 2 <= 8 and not visited[ loc[0] + 1 ][ loc[1] + 2 ]:
                tmpQ.put( [loc[0] + 1, loc[1] + 2 ])
            if loc[1] - 2 >= 0 and not visited[ loc[0] + 1 ][ loc[1] - 2 ]:
                tmpQ.put( [loc[0] + 1, loc[1] - 2])

        if loc[0] - 1 >= 1:
            if loc[1] + 2 <= 8 and not visited[ loc[0] - 1 ][ loc[1] + 2 ]:
                tmpQ.put( [loc[0] - 1, loc[1] + 2])
            if loc[1] - 2 >= 0 and not visited[ loc[0] - 1 ][ loc[1] - 2 ]:
                tmpQ.put( [loc[0] - 1, loc[1] - 2])

        if loc[1] + 1 <= 8:
            if loc[0] + 2 <= 8 and not visited[ loc[0] + 2 ][ loc[1] + 1 ]:
                tmpQ.put( [loc[1] + 1, loc[0] + 2])
            if loc[0] - 2 >= 0 and not visited[ loc[0] - 2 ][ loc[1] + 1 ]:
                tmpQ.put( [loc[1] + 1, loc[0] - 2])

        if loc[1] - 1 >= 1:
            if loc[0] + 2 <= 8 and not visited[ loc[0] + 2 ][ loc[1] - 1 ]:
                tmpQ.put( [loc[1] - 1, loc[0] + 2])
            if loc[0] - 2 >= 0 and not visited[ loc[0] - 2 ][ loc[1] - 1 ]:
                tmpQ.put( [loc[1] - 1, loc[0] - 2])

        # 如果q空了且tmpQ有東西，代表要找到目標座標，必須至少再走一步
        # 所以moveCount加一
        if q.empty() and not tmpQ.empty():
            q = tmpQ
            tmpQ = queue.Queue()
            moveCount += 1



if __name__ == '__main__':
    run = True
    while run:
        startAndEnd = input()
        if startAndEnd == "0 0":
            run = False
        else:
            startAndEnd = startAndEnd.split()
            start = [int(startAndEnd[0][1]), translateIndex( startAndEnd[0][0] ) ]
            end = [int(startAndEnd[1][1]), translateIndex( startAndEnd[1][0] ) ]

            print('From', startAndEnd[0], 'to', startAndEnd[1], ', Knight Moves =', BFS(start, end))
