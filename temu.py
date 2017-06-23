import numpy as np
import random as r

op= [[[1,1],[1,1]]]

ip=[[[0,0,0,0],[1,1,1,1],[0,0,0,0],[0,0,0,0]],
    [[0,0,1,0],[0,0,1,0],[0,0,1,0],[0,0,1,0]],
    [[0,0,0,0],[0,0,0,0],[1,1,1,1],[0,0,0,0]],
    [[0,1,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0]]]

sp=[[[0,1,1],[1,1,0],[0,0,0]],
    [[0,1,0],[0,1,1],[0,0,1]],
    [[0,0,0],[0,1,1],[1,1,0]],
    [[1,0,0],[1,1,0],[0,1,0]]]

zp=[[[1,1,0],[0,1,1],[0,0,0]],
    [[0,0,1],[0,1,1],[0,1,0]],
    [[0,0,0],[1,1,0],[0,1,1]],
    [[0,1,0],[1,1,0],[1,0,0]]]

tp=[[[0,1,0],[1,1,1],[0,0,0]],
    [[0,1,0],[0,1,1],[0,1,0]],
    [[0,0,0],[1,1,1],[0,1,0]],
    [[0,1,0],[1,1,0],[0,1,0]]]

lp=[[[0,0,1],[1,1,1],[0,0,0]],
    [[0,1,0],[0,1,0],[0,1,1]],
    [[0,0,0],[1,1,1],[1,0,0]],
    [[1,1,0],[0,1,0],[0,1,0]]]

jp=[[[1,0,0],[1,1,1],[0,0,0]],
    [[0,1,1],[0,1,0],[0,1,0]],
    [[0,0,0],[1,1,1],[0,0,1]],
    [[0,1,0],[0,1,0],[1,1,0]]]

pieceList=[op,ip,sp,zp,tp,lp,jp]
hwList=[2,4,3,3,3,3,3]#size of piece table square
rotTable=[1,4,4,4,4,4,4]#number of rotations for each piece ignoring degenerate

def genPiece():#create bag of 7 pieces in random order then bag.pop(0) to get next
    bag=[i for i in range(7)]
    r.shuffle(bag)
    return(bag)#generate number 0-6, for each piece

def clearFullLine(board):
    lineClears=0
    for i in range(19):
        if sum(board[i])>13:
            board=np.delete(board,i,axis=0)
            board=np.insert(board,0,[1,1,0,0,0,0,0,0,0,0,0,0,1,1],axis=0)
            lineClears+=1
    return(board,lineClears)

def pieceFits(board,p,rot,col,row):#verify p rot at col,row doesn't overlap
    piece=pieceList[p][rot]
    hw=hwList[p]
    #check collisions
    merge = np.sum(np.logical_and(board[row:row+hw,col:col+hw],piece))
    if merge:
        return(False)
    return(True)

def moveLeft(board,p,rot,col,row):
    return(pieceFits(board,p,rot,col-1,row))

def moveRight(board,p,rot,col,row):
    return(pieceFits(board,p,rot,col+1,row))

def moveDown(board,p,rot,col,row):#return True if can move down
    return(pieceFits(board,p,rot,col,row+1))


def rotateCW(board,p,rot,col,row):
    rotCW=(rot+1)%(rotTable[p])
    return(pieceFits(board,p,rotCW,col,row))

def rotateCCW(board,p,rot,col,row):
    rotCCW=(rot-1)%(rotTable[p])
    return(pieceFits(board,p,rotCW,col,row))

def hardDrop(board,p,rot,col,row):
    while (1):
        if row>17:
            break
        elif pieceFits(board,p,rot,col,row+1):
            row+=1
        else:
            break
    hw=hwList[p]
    board[row:row+hw,col:col+hw]=np.add(pieceList[p][rot],board[row:row+hw,col:col+hw])
    if (p==4):
        if (rot==2):
            if (board[row,col]+board[row,col+2])>0:
                return(1)
    return(0)

def boardWithPiece(board,p,rot,col,row):#print current board without updating main board
    hw=hwList[p]
    b2=np.copy(board)
    b2[row:row+hw,col:col+hw]=np.add(np.array(pieceList[p][rot])*2,np.array(board[row:row+hw,col:col+hw]))
    return(b2)

def scoreTotal(linClr,tSpin):
    if(tSpin):
        return(12)
    else:
        return(linClr**2)
