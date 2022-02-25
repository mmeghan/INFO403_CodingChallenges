'''
Goal: implement Linear Space Alignment to solve the Global ALignment Problem for a large dataset 
input: two long protein strings written in the single-letter amino acid alphabet 
output: the maximum alignment score of these strings followed by an alignment achieving this maximum score

use Blosum62 scoring matrix and indel penalty of 5 

-During the execution of LinearSpaceAlignment two recursive calls are done, LinearSpaceAlignment(v, w, top=0, bottom=4, right=0, left=4) and LinearSpaceAlignment(v, w, 5, 8, 5, 8) 
-In the case when midEdge is horizontal or diagonal the left blue rectangle is shifted by one column to the right 
as compared to the middle column(the line middle = middle +1)
- In the case when midEdge is vertical or diagonal, the left blue rectagle is shifted by one row to the bottom
as compared to the postion of the middle node (the line midNode = midNode +1)

'''

from ScoringMatrices import BLOSUM62
from MiddleEdge import MiddleEdge
import math

pentalty = 5
blosum = BLOSUM62()

def ReadFile():
    with open ('./testcases/12_LinearSpaceAlignment/inputs/sample.txt', 'r') as f:
        data = f.readlines()
        str1 = data[0].strip()
        str2 = data[1].strip()
    return (str1, str2)

inputs = ReadFile()
str1= inputs[0]
str2 = inputs[1]
top = 0 
bottom = len(str1)
print('bottom:', bottom)
left = 0 
right = len(str2)
print('right:', right)



def MiddleNodeEdge(top, bottom, left, right):
    #returns the coordinate i of the middle node (i,j)
    #returns the direction (right, down, diagonal) depending on weather the middle edge is horizontal, diagonal or vertical
    ((i1,j1),(i2,j2)) = MiddleEdge(str1[top:bottom], str2[left:right], blosum, pentalty)
                #Right          #down           #diagonal
    print(((i1,j1),(i2,j2)))
    direction = 0 if i1==i1 else 1 if j1==j2 else 2
    return j1, direction 

def RecoverAlignment(path):
    align1 = ''
    align2 = ''
    score = 0 
    for i in range(len(path)):
        if path[i] == 1:
            align1 = align1 + str1[0]
            align2 = align2 + '-'
            score -= pentalty
            str1= str1[1:]
        elif path[i] == 0:
            align1= align1 + '-'
            align2 = align2 +str2[0]
            score -= pentalty
            str2 = str2[1:]
        elif path[i] == 2:
            align1 = align1+ str1[0]
            align2 = align2 + str2[0]
            if (str1[0],str2[0]) in blosum:
                score += blosum[(str1[0], str2[0])]
            else:
                score += blosum[(str2[0], str1[0])]
            str1 = str1[1:]
            str2 = str2[1:]
    return score, align1, align2



def LinearSpaceAlignment(top, bottom, left, right):
    if left == right:
        return pentalty*(bottom-top)
    if top ==  bottom:
        return pentalty*(right-left)
    
    middle = math.floor((left+right)/2)
    midNode, midEdge = MiddleNodeEdge(top,bottom, left, right)

    pathLeft = LinearSpaceAlignment(top, midNode, left, middle)
    #output midEdge
    if midEdge == 0 or midEdge == 2:
        middle += 1
    if midEdge == 1 or midEdge == 2:
        midNode +=1 
    pathRight = LinearSpaceAlignment(midNode, bottom, middle, right)
    print(pathLeft + midEdge + pathRight)
    return pathLeft + midEdge + pathRight





path = LinearSpaceAlignment(top,bottom,left,right)
print('path:',path)
for item in RecoverAlignment(path):
    print(item)






