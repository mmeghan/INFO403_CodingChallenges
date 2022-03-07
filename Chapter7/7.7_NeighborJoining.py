'''
Goal: Implement NeighborJoining 
Input: an integer n followed by an n x n distance matrix
Output: An adjacency list for the tree resulting from applying the neighbor-joining algorithm. 
        Edge-weights should be accurate to two decimal places 
        (they are provided to three decimal places in the sample output below).

* Formating Note: The adjacency list must have consecutive integer node labels starting from 0. 
  The n leaves must be labeled 0, 1, ..., n - 1 in order of their appearance in the distance matrix. 
  Labels for internal nodes may be labeled in any order but must start from n and increase consecutively.

NeighborJoining(D)
    n ← number of rows in D
    if n = 2
        T ← tree consisting of a single edge of length D1,2
        return T
    D* ← neighbor-joining matrix constructed from the distance matrix D
    find elements i and j such that D*i,j is a minimum non-diagonal element of D*
    Δ ← (TotalDistanceD(i) - TotalDistanceD(j)) /(n - 2)
    limbLengthi ← (1/2)(Di,j + Δ)
    limbLengthj ← (1/2)(Di,j - Δ)
    add a new row/column m to D so that Dk,m = Dm,k = (1/2)(Dk,i + Dk,j - Di,j) for any k
    D ← D with rows i and j removed
    D ← D with columns i and j removed
    T ← NeighborJoining(D)
    add two new limbs (connecting node m with leaves i and j) to the tree T
    assign length limbLengthi to Limb(i)
    assign length limbLengthj to Limb(j)
    return T

./testcases/NeighborJoiningSample.txt
dataset_609181_7
'''

def ReadFile():
    with open('./datasets/dataset_609181_7.txt', 'r') as f:
        n = int(f.readline().strip())
        distanceMatrix = []
        for i in range(n):
            distanceMatrix.append([int(t) for t in f.readline().split()])

    return n, distanceMatrix

def NeighborJoinMat(n, matrix):
    matrix2 = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                newDistance = (n-2)*matrix[i][j] - sum(matrix[i]) - sum(matrix[j])
                matrix2[i][j] = newDistance

    return matrix2

def FindMinElement(n, matrix):
    minValue = matrix[0][0]
    for i in range(n):
        for j in range(i,n):
            if matrix[i][j] < minValue:
                minValue = matrix[i][j]
                position = [i,j]
    return position

def NeighborJoin(D, n, nodeList = None, dict = None):
    if dict == None:
        dict= {}
    if nodeList == None:
        nodeList = list(range(n))

    if n == 2:
        if nodeList[0] not in dict.keys():
            dict[nodeList[0]]={}
        if nodeList[1] not in dict.keys():
            dict[nodeList[1]]={}
        dict[nodeList[0]][nodeList[1]]=D[0][1]
        dict[nodeList[1]][nodeList[0]]=D[0][1]
         
        return dict

    D2 = NeighborJoinMat(n, D)
    minElement = FindMinElement(n, D2)
    i = minElement[0]
    j = minElement[1]
    diff = (sum(D[i]) - sum(D[j]))/(n-2)
    limbI = (D[i][j] + diff)/2
    limbI = "{:.2f}".format(limbI)
    limbJ = (D[i][j] - diff)/2
    limbJ = "{:.2f}".format(limbJ)

    add_row = [(D[k][i] + D[k][j] - D[i][j])/2 for k in range(n)] + [0]
    D.append(add_row)

    for l in range(n):
        D[l].append(add_row[l])

    #keep track of the node--column
    m = nodeList[-1] +1
    nodeList.append(m)
        
    # remove i, j col
    [ab.pop(max(i,j)) for ab in D]
    [ab.pop(min(i,j)) for ab in D]
    # remove i, j row
    D.remove(D[max(i,j)])
    D.remove(D[min(i,j)])
        

    node_i = nodeList[i]
    node_j = nodeList[j]
    nodeList.remove(node_i)
    nodeList.remove(node_j)

    if node_i not in dict.keys():
        dict[node_i]={}
        if node_j not in dict.keys():
            dict[node_j]={}
        if m not in dict.keys():
            dict[m]={}
        dict[node_i][m]=limbI
        dict[node_j][m]=limbJ
        dict[m][node_i]=limbI
        dict[m][node_j]=limbJ

        NeighborJoin(D, n-1, nodeList, dict )
        return dict


n, distanceMatrix = ReadFile()
tree = NeighborJoin(distanceMatrix, n)
with open('./NeighborJoinSolution.txt', 'w') as output:
    for key in tree:
        for node in tree[key]:
            output.write(str(key)+"->" + str(node)+":" +str(tree[key][node]) +'\n')