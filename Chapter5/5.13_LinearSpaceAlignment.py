'''
Goal: implement Linear Space Alignment to solve the Global ALignment Problem for a large dataset 
input: two long protein strings written in the single-letter amino acid alphabet 
output: the maximum alignment score of these strings followed by an alignment achieving this maximum score

use Blosum62 scoring matrix and indel penalty of 5 
'''

#from ScoringMatrices import BLOSUM62
import math
import numpy as np

pentalty = 5


with open ('./testcases/12_LinearSpaceAlignment/inputs/sample.txt', 'r') as f:
    data = f.readlines()
    str1 = data[0].strip()
    str2 = data[1].strip()
with open('BLOSUM62.txt', 'r') as input_data:
    items = [line.strip().split() for line in input_data.readlines()]
    blosum = {(item[0], item[1]):int(item[2]) for item in items}


def twoColumnWeight(str1, str2, middle):
    m = len(str1)
    n = len(str2)

    weightSum = np.zeros((m+1,2))
    for i in range(m+1):
        weightSum[i,0] = -pentalty*i
    if middle == 0:
        weightSum[0:m+1, 1] = weightSum[0:m+1,0]
        return weightSum
    count = 0 
    while True:
        weightSum[0,1] = weightSum[0,0]-pentalty
        for i in range(1, m+1):
            if (str1[i-1],str2[0]) in blosum:
                weightSum[i,1] = max(weightSum[i,0]-pentalty, weightSum[i-1,1]-pentalty, weightSum[i-1,0] + blosum[str1[i-1],str2[0]])
            else:
                weightSum[i,1] = max(weightSum[i,0]-pentalty, weightSum[i-1,1]-pentalty, weightSum[i-1,0]+blosum[(str2[0],str2[i-1])])
        str2 = str2[1:n]
        count += 1
        if count == middle:
            break 
        weightSum[0:m+1,0] = weightSum[0:m+1,1]
    return weightSum



def MiddleNodeEdge(top,bottom,left,right):
    first = str1[top:bottom]
    second = str2[left:right]
    middle = math.floor((left+right)/2) - left
    First = twoColumnWeight(first,second,middle)
    fromStart = First[0:len(first)+1,1]
    #to end
    firstR = first[::-1]
    secondR = second[::-1]
    middler = len(second) - middle
    FirstR  =twoColumnWeight(firstR,secondR,middler)
    toEnd = np.flip(FirstR[0:len(first)+1,1])
    length = fromStart + toEnd
    index = np.argmax(length)
    V = FirstR[len(first)-index-1,1] - pentalty
    H = FirstR[len(first)-index, 0] - pentalty
    if (firstR[len(first)-index-1], secondR[middler-1]) in blosum:
        D = FirstR[len(first)-index-1,0] + blosum[(firstR[len(first)-index-1], secondR[middler-1])] 
    else:
        D = FirstR[len(first)-index-1,0] + blosum[(secondR[middler-1],firstR[len(first)-index-1])]
    if FirstR[len(first) - index,1] == D:
        return (index+top,'D')
    elif FirstR[len(first)-index,1] == H:
        return (index+top, 'H')
    elif FirstR[len(first)-index,1] == V:
        return (index+top, 'V')
    

def LinearSpaceAlignment ( top, bottom, left, right):
        #the case left = right describes the alignment of an empty string agaist the string Str1top+1...Str1bottom
        #which is trivially computed as the score of a gap formed by bottom - top vertical edges 
    if left ==right:
        return 'V'*(bottom-top)
    if top == bottom:
        return 'H'*(right-left)
    middle = math.floor((left+right)/2)
    middleNode = MiddleNodeEdge(top,bottom,left,right)[0]
    middleEdge = MiddleNodeEdge(top,bottom,left,right)[1]
    pathLeft = LinearSpaceAlignment(top,middleNode, left, middle)
    if middleEdge == 'H' or middleEdge == 'D':
        middle += 1
    if middleEdge == 'V' or middleEdge == 'D':
        middleNode += 1
    pathRight = LinearSpaceAlignment(middleNode, bottom, middle, right)
    
    return pathLeft + middleEdge + pathRight 

def getAlignment (path, string1, string2):
    align1 = ''
    align2= ''
    score = 0 
    for i in range(len(path)):
        if path[i] =='V':
            align1 = align1 + string1[0]
            align2 = align2 + '-'
            score = score -  pentalty
            string1 = string1[1:]
        elif path[i] == 'H':
            align1 = align1 + '-'
            align2 = align2 + string2[0]
            score =  score - pentalty
            align2 = align2[1:]
        elif path[i] == 'D':
            align1 = align1 + string1[0]
            align2= align2 + string2[0]
            if (string1[0] , string2[0]) in blosum:
                score =score + blosum[(string1[0],string2[0])]
            string1 = string1[1:]
            string2 = string2[1:]
    return score, align1, align2 

#inputs = ReadFile()
#str1= inputs[0]
#str2 = inputs[1]
top = 0 
bottom = len(str1)
left = 0 
right = len(str2)
path = LinearSpaceAlignment(top,bottom,left,right)
#gets the wrong score but right alignment 
for result in getAlignment(path, str1,str2):
    print (result)





