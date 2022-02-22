import math

def MiddleEdge(str1, str2, blosum, indel_pentalty):

    m = len(str1)
    n = len(str2)

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