'''
Goal:  Compute the distances between leaves in a weighted tree.
Input: An integer n followed by the adjacency list of a weighted tree with n leaves
Output: An n x n matrix (di,j), where di,j is the length of the path between leaves i and j.


The tree is given as an adjacency list of a graph whose leaves are integers between 0 and n - 1; 
the notation a->b:c means that node a is connected to node b by an edge of weight c. 
The matrix you return should be space-separated.

./testcases/LeavesDistanceSample.txt
'''
from collections import defaultdict
from queue import Queue
import re

def ReadFile():
    with open('./datasets/dataset_609176_12.txt', 'r') as f:
        adj =  defaultdict(list)
        n = int(f.readline())
        for line in f.readlines():
            src, dst, weight = list(map(int, re.split('->|:', line.strip())))
            adj[src].append((dst, weight))
    return n, adj



def LeavesDistance(adj, root):
    curr = root
    d = [-1] * len(adj)
    d[curr] = 0

    q=  Queue()
    #for the atributes of adj[curr] (so its connecting node and edge weight) add to d and put in queue
    for neighbor, weight in adj[curr]:
        d[neighbor] = weight + d[curr]
        q.put(neighbor)
    #while there is something in the queue get it and calulate distance and put in d
    while not q.empty():
        curr = q.get()
        for neighbor, weight in adj[curr]:
            if d[neighbor] != -1:
                continue
            else:
                d[neighbor] = weight + d[curr]
                q.put(neighbor)
    return d

n, adj = ReadFile()
#print(n)
#print(adj)
with open ('./LeaveDistanceSolution.txt', 'w') as output:
    for leaf in range(n):
        print(' '.join(list(map(str, LeavesDistance(adj, leaf)[:n]))), file = output)
