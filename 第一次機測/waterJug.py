# 學號: 10720111 / 10720107
# 姓名: 陳少暉 / 陳丕中

class Bucket:
    def __init__( self, maxVolume, name ):
        self.maxVolume = maxVolume
        self.name = name
        self.curVolume = 0

    def Fill(self):
        print( 'Fill ' + self.name )
        self.curVolume = self.maxVolume

    def Empty(self):
        print( 'Empty ' + self.name )
        self.curVolume = 0

    def PourTo(self, b):
        print( 'Pour ' + self.name + ' ' + b.name )
        bVolumeLeft = b.maxVolume - b.curVolume
        if self.curVolume <= bVolumeLeft:
            # b can accept all water from a
            b.curVolume = b.curVolume + self.curVolume
            self.curVolume = 0
        else:
            b.curVolume = b.maxVolume
            self.curVolume = self.curVolume - bVolumeLeft


    def IsEmpty(self):
        return self.curVolume == 0

    def IsFull(self):
        return self.curVolume == self.maxVolume


content = input('input: ')

while content != '0 0 0':
    content = content.split()
    content = list(map(int, content))

    bucketA = Bucket( content[0], 'A' )
    bucketB = Bucket( content[1], 'B' )
    target = content[2]

    while bucketA.curVolume != target and bucketB.curVolume != target:
        if bucketA.IsEmpty():
            bucketA.Fill()

        if bucketA.curVolume != target:
            if bucketB.IsFull():
                bucketB.Empty()

            bucketA.PourTo(bucketB)


    print( 'Success' )

    content = input('\ninput: ')
