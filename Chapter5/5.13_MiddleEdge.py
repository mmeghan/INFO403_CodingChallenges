'''
Goal: Solve the Middle Edge in Linear Space Problem 
input: two amino acid strings 
output: the middle edge in the alignment grapn in the form "(i,j)(k,l)" where (i,j)
        connects to (k,l).
To compute score use BLOSUM62 scoring matrix and a linear indel pentaly of 5

middle edge =  an edge in an potimal alignment path starting at the middle node 
middle node = the node where the longest path crosses the middle column

Classify a path from the source to the sink ad in i-path if it passes through the middle column at row i 

./testcases/11_MiddleEdge/inputs/sample.txt
'''
from ScoringMatrices import BLOSUM62
import math

def ReadFile():
    with open ('./datasets/dataset_609149_12.txt', 'r') as f:
        data = f.readlines()
        str1 = data[0].strip()
        str2 = data[1].strip()

    return (str1, str2)

def MiddleEdge(str1, str2, blosum, indel_pentalty):

    m = len(str1)
    n = len(str2)
    #indel_pentalty = 5

    s_start = [[0 for j in range(n+1)] for i in range(m+1)]
    s_end = [[0 for j in range(n+1)] for i in range(m+1)]
    s_sum = [[0 for j in range(n+1)] for i in range(m+1)]

    for i in range(m+1):
        s_start[i][0] = -i * indel_pentalty
        s_end[m-1][n] = -i * indel_pentalty
    for j in range(n+1):
        s_start[0][j] = -j * indel_pentalty
        s_end[m][n-1] = -j * indel_pentalty
    

    for i in range(1, m+1):
        for j in range(1, n+1):
            match = blosum[(str1[i-1] , str2[j-1])]
            s_start[i][j] = max(s_start[i-1][j]-indel_pentalty, s_start[i][j-1]-indel_pentalty, s_start[i-1][j-1]+match)

    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            match = blosum[(str1[i],str2[j])]
            s_end[i][j] = max(s_end[i+1][j]-indel_pentalty, s_end[i][j+1]-indel_pentalty, s_end[i+1][j+1]+match)
   
    middleColumn = math.floor(n/2)
    row=0 #initilization with zero
    adj_col=0
    adj_row= 0

    #finding the middle node, node in the middle column with the highest score
    for i in range (m+1):
        for j in range(n+1):
            s_sum[i][j] = s_start[i][j] + s_end[i][j]
            if s_sum[row][middleColumn] < s_sum[i][middleColumn]:
                row = i 
                middleColumn = middleColumn
    #finding the adjaceny for the middle node, which is a node which has the same score as the middle node 
    # Find where (i,j) connects       
    if m + 1 > row + 1:
        if s_sum[row][middleColumn] == s_sum[row+1][middleColumn+1]:
            adj_row, adj_col = row +1, middleColumn +1 
        elif s_sum[row][middleColumn] == s_sum[row+1][middleColumn]:
            adj_row = row+1
            adj_col = middleColumn
        else:
            adj_row = row
            adj_col = middleColumn+1

    middleNode = row, middleColumn
    connected = adj_row, adj_col

    return middleNode, connected

inputs = ReadFile()
str1 = inputs[0]
str2 = inputs[1]

blosum = BLOSUM62()
indel_pentalty = 5

print(MiddleEdge(str1, str2, blosum, indel_pentalty))
