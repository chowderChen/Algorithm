class BTree:
    def __init__(self, m):
        # m: max children num
        self.children = []
        self.keys = []
        self.m = m


    def Insert( self, key ):
        # if root is full,create new root to hold key, split original root
        if self.NodeIsFull():
            newRoot = BTree( self.m )
            newRoot.children.append( self )

            self.Split( newRoot )

            if key < newRoot.keys[0]:
                tmpNode = newRoot.children[0]
            else:
                tmpNode = newRoot.children[1]
        else:
            tmpNode = self
            newRoot = self

        while not tmpNode.NodeIsLeaf():
            # search next node to examine
            # split full node & find the correct leaf position
            i = 0
            while i < len( tmpNode.keys ) and key > tmpNode.keys[i]:
                i = i + 1

            next = tmpNode.children[i]
            if next.NodeIsFull():
                next.Split( tmpNode )
            else:
                tmpNode = next

        tmpNode.NodeAddKey( key )

        return newRoot


    def Split( self, parent ):
        newNode = BTree( self.m )
        midIndex = self.NodeSize() // 2  # midIndex == maxSize(3) // 2 == 1

        # self: 0~1, newNode: 2~3
        newNode.children = self.children[ midIndex + 1: ]
        self.children = self.children[ :midIndex + 1 ]

        # keys: self: 0, parent: 1, newNode: 2~3
        parent.NodeAddKey(self.keys[midIndex])
        newNode.keys = self.keys[midIndex+1:]
        self.keys = self.keys[ :midIndex ]

        parent.NodeAddChild( newNode )


    def NodeAddKey(self, key):
        self.keys.append( key )
        self.keys.sort()

    def NodeAddChild(self, child):
        i = 0
        while i < len( self.children ) and child.keys[0] > self.children[i].keys[0] :
            i = i + 1

        self.children = self.children[ 0:i ] + [ child ] + self.children[ i: ]

    def NodeIsFull(self):
        return self.NodeSize() == self.m - 1

    def NodeIsLeaf(self):
        return not self.children

    def NodeSize(self):
        return len( self.keys )

    def PrintPreorder(self):
        print(self.keys, end = '')
        for i in self.children:
            i.PrintPreorder()

    def PrintPostorder(self):
        for i in self.children:
            i.PrintPreorder()
        print(self.keys, end = '')


tree = BTree(4)
content = input('內容: ')
content = content.split()
content = list(map(int, content))
# print(content)
for key in content:
    tree = tree.Insert( key )

print( "2-3-4 Tree (Preorder):" )
tree.PrintPreorder( )
print( "\n2-3-4 Tree (Postorder):" )
tree.PrintPostorder()
