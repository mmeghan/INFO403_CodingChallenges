'''
Goal- Fine the length of a longest path in the Manhattan Tourist Problem 
input - integers n and m, followed by an nx(m+1) matrix Down and an (n+1)x m matrix Right. the two matricies are separated by '-'
output - the lenght of a longest path from source (0,0) to sink(n,m) in the rectangular grid whose edges are defines by the matricies Down and Right

Psudocode- (own i, j and righti, j are the respective weights of the vertical and horizontal edges entering node (i, j). 
We denote the matrices holding (downi, j) and (righti, j) as Down and Right, respectively.)

ManhattanTourist(n, m, Down, Right)
    s0, 0 ← 0
    for i ← 1 to n
        si, 0 ← si-1, 0 + downi-1, 0
    for j ← 1 to m
        s0, j ← s0, j-1 + right0, j-1
    for i ← 1 to n
        for j ← 1 to m
            si, j ← max{si - 1, j + downi-1, j, si, j - 1 + righti, j-1}
    return sn, m
./testcases/02_LongestPathGrid/inputs/test3.txt
    dataset_609142_10

'''

def ReadFile():
    with open ('./datasets/dataset_609142_10.txt', 'r') as f:
        n, m = map(int, f.readline().strip().split())
        down = [[int(i) for i in f.readline().strip().split()] for i in range(n)]
        f.readline()
        right = [[int(i) for i in f.readline().strip().split()] for i in range(n+1)]
    print(n,m)
    print(down)
    print(right)
    return(n,m, down, right)

def ManhattenTourism(n,m, down, right):
    '''
    moving south: (i-1,j)
    moving east: (i,j-1)
    for i>0 and j>0, the only way to reach node(i,j) is by moving down from node (i-1,j)
    or by moving right from node (i,j-1). THis Si,j can be computed as the maximum of two values:
    Si-1,j + weight of vertical edge from (i-1,j) to (i,j)
    Si,j-1 + weight of the horizontal edge from (i,j-1) to (i,j)
    '''
    result = [[0]*(m+1) for i in range(n+1)]
    #go down the matrix 
    for i in range(1, n+1):
        result[i][0] = result[i-1][0] + down[i-1][0]
    # go across the matrix
    for j in range(1, m+1):
        result[0][j] = result[0][j-1] + right[0][j-1]
    for i in range(1,n+1):
        for j in range(1, m+1):
            #find if its longer to go down or across for the next step 
            result[i][j] = max(result[i-1][j] + down[i-1][j], result[i][j-1]+right[i][j-1])
    return result[n][m]


inputs = ReadFile()
n = inputs[0]
m = inputs[1]
down = inputs[2]
right = inputs[3]
print(ManhattenTourism(n,m,down, right))







