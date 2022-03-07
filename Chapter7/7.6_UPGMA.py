'''
Goal: Implement 
Input: An integer n followed by a space sparated n x n distance matrix
Output: An adjacency list for the ultrametric tree returned by UPGMA. 
        Edge weights should be accurate to two decimal places 
        (answers in the sample dataset below are provided to three decimal places).

* Formating Note: The adjacency list must have consecutive integer node labels starting from 0. 
  The n leaves must be labeled 0, 1, ..., n - 1 in order of their appearance in the distance matrix. 
  Labels for internal nodes may be labeled in any order but must start from n and increase consecutively.

UPGMA(D, n) 
    Clusters ← n single-element clusters labeled 1, ... , n
    construct a graph T with n isolated nodes labeled by single elements 1, ... , n
    for every node v in T 
         Age(v) ← 0
    while there is more than one cluster
        find the two closest clusters Ci and Cj 
        merge Ci and Cj into a new cluster Cnew with |Ci| + |Cj| elements
        add a new node labeled by cluster Cnew to T
        connect node Cnew to Ci and Cj by directed edges 
        Age(Cnew) ← DCi, Cj / 2
        remove the rows and columns of D corresponding to Ci and Cj
        remove Ci and Cj from Clusters
        add a row/column to D for Cnew by computing D(Cnew, C) for each C in Clusters
        add Cnew to Clusters
    root ← the node in T corresponding to the remaining cluster
    for each edge (v, w) in T
        length of (v, w) ← Age(v) - Age(w)
    return T

'''
import sys
import numpy as np


def ReadFile():
    with open('./testcases/UPGMASample.txt', 'r') as f:
        n = int(f.readline().strip())
        lines = [line.strip().split() for line in f.readlines()]
        distanceMatrix = np.array(lines, dtype= float)
        np.fill_diagonal(distanceMatrix, np.inf)
        f.close()
        del(lines)
    return n, distanceMatrix

def findClosest(clusters, D):
    min = sys.maxsize
    start = 0 
    end = 0
    for i in range(len(D)):
        for j in range(i):
            if i in clusters and j in clusters:
                distance = distanceClusters(D, i, j, clusters)
                if distance < min:
                    min = distance
                    start = i
                    end = j
    return [start,end]

def distanceClusters(D, i, j, clusters):
    distance = 0
    if i in clusters and j in clusters:
        for ii in clusters[i]:
            for jj in clusters[j]:
                distance += D[ii][jj]

    result = distance / (len(clusters[i]) * len(clusters[j]))

    return result 


def UPGMA(D, n):
    tree = {}
    clusters ={}
    age = {}

    #initally populate clusters, tree and age
    for i in range(n):
        clusters[i] = [i]
    
    for i in range(n):
        tree[i] = []
    
    for i in range(n):
        age[i] = 0

    stack = list(clusters.keys())

    #while there is more than one cluster left 
    while len(stack) > 1:
        #create new cluster 
        Cnew = len(tree)

        #find the closest clusters 1, j and get their distances
        #i , j = findClosest(clusters,D)
        [i, j] = np.unravel_index(np.argmin(D, axis=None), D.shape)
        Ci , Cj  = stack[i], stack[j]

        #Age of Cnew = Distance[i][j] /2 
        age[Cnew] = D[i][j] /2

        #merge Ci and Cj into a Cnew and add Cnew to Clusters
        clusters[Cnew] = clusters[Ci] + clusters[Cj]

        #add Cnew to tree with w direstec edges to Ci and Cj
        tree[Cnew] = [Ci, Cj]

        #compute D(Cnew,C)  for each C in clusters
        sizeCi, sizeCj = len(clusters[Ci]), len(clusters[Cj])
        Dnew = []

        #want to iterate over all columns m in matrix except i and j
        for m in range(len(stack)):
            if m != i and m != j:
                distance = ((D[i][m]*sizeCi) + (D[j][m]*sizeCj)) / (sizeCi + sizeCj)
                Dnew.append(distance)
        
        #remove Ci and Cj from stack 
        stack.remove(Ci)
        stack.remove(Cj)

        #remove the rows and columns of D corresponding to Ci and Cj 
        D = np.delete(D, (i,j), 0)
        D = np.delete(D, (i,j), 1)

        #add a row to D for Cnew
        D = np.append(D, [Dnew], 0)
        #add diagonal for new cluster 
        Dnew.append(float('inf'))
        D = np.append(D, [[d] for d in Dnew], 1)

        #add new cluster to stack
        stack.append(Cnew)

        #create edgelist
        #root = the node in tree corresponding to the remaing cluster 
        #for each edge(v,w) has length = age(v) - age(w)
        edges = []
        for v in tree.keys():
            for w in tree[v]:
                edges.append((v, w, "%.3f" % (abs(age[v] - age[w]))))
                edges.append((w, v, "%.3f" % (abs(age[v] - age[w]))))
    
        return edges


n, distanceMatrix = ReadFile()
edges = UPGMA(distanceMatrix, n)
#not getting all of the answers that is supposed to be returned only some of them
#this is the current output i am getting 
'''
4->2:5.000
2->4:5.000
4->3:5.000
3->4:5.000
'''
for edge in edges:
    print('{0}->{1}:{2}'.format(edge[0],edge[1],edge[2]))