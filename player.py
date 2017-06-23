from temu import *
import sys

#x=np.array([[1,1,0,0,0,0,0,0,0,0,0,0,1,1] for _ in range(20)]+[[1]*14]*2)
x=np.array(
[
    [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
])
#print(x)

bag=genPiece()
bag.extend(genPiece())
bag.extend(genPiece())

piece=1
rot=0
col=0
row=0

bt=pieceFits(x,piece,rot,col,row)
print(bt)
if bt:
    print(boardWithPiece(x,piece,rot,col,row))
#x,linClr=clearFullLine(x)
#print(linClr)
#print(x)
pSent=0
score=0
boards=[]
nextPiece=[]
moveChoice=[]
scoreTable=[]



with open('tet.data','a') as f:
    while(len(bag)>1):
        dat=[]
        piece=bag.pop(0)
        nex=bag[0]
        rot,row,col=0,0,4
        if (pieceFits(x,piece,rot,col,row)) != True:
            print('topped out')
            break
        lastMove=0
        while(1):
            g=boardWithPiece(x,piece,rot,col,row)
            g2=np.array([[i if i>0 else 88 for i in j] for j in g])
            print(g2)
            s=input()
            boards.append(g)
            nextPiece.append(nex)
            if (s==','):#up=rotate cw
                if(rotateCW(x,piece,rot,col,row)):
                    rot=(rot+1)%(rotTable[piece])
                    lastMove=1
                moveChoice.append(0)
            elif (s=='.'):#up=rotate ccw
                if(rotateCCW(x,piece,rot,col,row)):
                    rot=(rot-1)%(rotTable[piece])
                    lastMove=1
                moveChoice.append(1)
            elif(s=='a'):#left
                if(moveLeft(x,piece,rot,col,row)):
                    col-=1
                moveChoice.append(2)
            elif(s=='o'):#down
                if(moveDown(x,piece,rot,col,row)):
                    row+=1
                moveChoice.append(3)
            elif(s=='e'):#right
                if(moveRight(x,piece,rot,col,row)):
                    col+=1
                moveChoice.append(4)
            elif(s==' '):#space
                tSpin=hardDrop(x,piece,rot,col,row)
                moveChoice.append(5)
                break
        pSent+=1
        x,linClr=clearFullLine(x)
        score+=scoreTotal(linClr,tSpin)
        scoreTable.append[score]
        g=boardWithPiece(x,piece,rot,col,row)
        g2=np.array([[i if i>0 else 88 for i in j] for j in g])
        print(g2)
np.savetxt(tet.dat,[boards,nextPiece,moveChoice,scoreTable])



'''
x=np.array(
[
    [1,1,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1],
])
'''
