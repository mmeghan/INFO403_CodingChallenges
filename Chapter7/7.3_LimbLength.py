'''
Goal: For each j, we can compute LimbLength(j) by finding the minimum value of (D_{i,j} + D_{j,k} - D_{i,k})/2(D i,j +D j,k - D i,k)/2 over all pairs of leaves i and k.
Inputs: An integer n, followed by an integer j between 0 and n - 1, followed by a space-separated additive distance matrix D (whose elements are integers).
Output: The limb length of the leaf in Tree(D) corresponding to row j of this distance matrix (use 0-based indexing).
./testcases/LimbLengthSample.txt

./datasets/dataset_609177_11.txt

'''

def ReadFile():
    with open('./testcases/LimbLengthClassEx.txt', 'r') as f:
        n = int(f.readline().strip())
        j = int(f.readline().strip())
        distanceMatrix = [list(map(int, line.strip().split()))for line in f.readlines()]
    return n, j , distanceMatrix


def LimbLength(distanceMatrix, j, n):
    i = 0
    min_val = float('inf')
    #compute the number of j's in n 
    while i < n and i ==j:
        i += 1
    #for every element in n compute the minimum value over all pairs of leaves i and k 
    for k in range(n):
        if k == j or k == i:
            continue
        print('Dij:',distanceMatrix[i][j] )
        print('Djk:',distanceMatrix[k][j])
        print('Dik:', distanceMatrix[i][k] )
        min_val = min(min_val, (distanceMatrix[i][j] + distanceMatrix[k][j] - distanceMatrix[i][k])//2)
    return min_val

n, j, distanceMatrix = ReadFile()
distance = LimbLength(distanceMatrix, j, n)
print(distance)
