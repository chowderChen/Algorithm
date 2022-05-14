# 學號: 10720111
# 姓名: 陳少暉
# 0-1 Knapsack

class Item:
    def __init__(self, weight, value):
        self.weight = int(weight)
        self.value = int(value)

def DP_0_1_Knapsack(value, weight, n, W):
    # n: total n item
    # W:knapsack limit
    c = [[0 for w in range(W + 1)] for i in range(n + 1)]

    for w in range(W + 1):
        c[0][w] = 0

    for i in range(n + 1):
        if i == 0:
            for w in range( W+1 ):
                c[0][w] = 0
        else:
            c[i][0] = 0
            for w in range(1, W + 1):
                if (weight[i - 1] <= w):
                    if (value[i - 1] + c[i - 1][w - weight[i - 1]] > c[i - 1][w]):
                        c[i][w] = value[i - 1] + c[i - 1][w - weight[i - 1]]
                    else:
                        c[i][w] = c[i - 1][w]
                else:
                    c[i][w] = c[i - 1][w]

    # for j in range(n+1):
    #     for k in range(W+1):
    #         print(c[j][k], end = ' ')
    #     print()

    return c

if __name__ == '__main__':
    knapsackLimit = input("knapsack limit:")
    itemNum = input( "number of item: " )
    knapsackLimit = int(knapsackLimit)
    itemNum = int( itemNum )
    valueList = []
    weightList = []
    for i in range( itemNum ):
        itemInf = input()
        itemInf = itemInf.split()
        # item = Item(itemInf[0], itemInf[1])
        weightList.append(int(itemInf[0]))
        valueList.append(int(itemInf[1]))

    resultMatrix = DP_0_1_Knapsack(valueList, weightList, itemNum, knapsackLimit)

    itemList = []
    index = itemNum
    weightLeft = knapsackLimit
    while index > 0:
        if resultMatrix[index][weightLeft] != resultMatrix[index - 1][weightLeft]:
            itemList.append(index)  # actually item[index-1], but for user it's index
            weightLeft = weightLeft - weightList[index - 1]
        index = index - 1

    print( 'Total Value = ' + str(resultMatrix[itemNum][knapsackLimit]) )
    print( 'Items ', end = '')
    itemList.reverse()
    isFirst = True
    for i in itemList:
        if not isFirst:
            print(', ', end = '' )
        else:
            isFirst = False
        print( i, end = '' )
