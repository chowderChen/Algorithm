# 學號: 10720111
# 姓名: 陳少暉
# Huffman codes

import heapq

class HuffmanNode:
    def __init__(self):
        self.char = ''
        self.freq = 0
        self.left = None
        self.right = None
        self.code = ""

    def __lt__(self, other):
        return self.freq < other.freq

def Huffman( q ):
    heapq.heapify(q)
    n = len(q)

    for i in range(n - 1):
        hNode = HuffmanNode()
        hNode.left = heapq.heappop(q)
        hNode.right = heapq.heappop(q)
        hNode.freq = hNode.left.freq + hNode.right.freq
        heapq.heappush(q,hNode)

    return heapq.heappop(q)

def HuffmanTraverse(root, s, inList):
    if root:
        if root.char != "":
            for i in inList:
                if root.char == i.char:
                    i.code = s
            # print(root.char + " " + s )

        leftStr = s + "0"
        rightStr = s + "1"
        HuffmanTraverse(root.left, leftStr, inList )
        HuffmanTraverse(root.right, rightStr, inList )

if __name__ == '__main__':
    run = True
    counter = 1
    while run:
        charNum = int( input("輸入: ") )
        if charNum == 0:
            run = False
        else:
            inList = []
            for i in range(charNum):
                tmp = input()
                tmp = tmp.split()
                hNode = HuffmanNode()
                hNode.char = tmp[0]
                hNode.freq = int(tmp[1])
                inList.append(hNode)

            q = inList.copy()
            root = Huffman(q)
            HuffmanTraverse(root, "", inList)
            print("Huffman Codes #" + str(counter))
            counter += 1
            for i in inList:
                print( i.char + " " + i.code )
