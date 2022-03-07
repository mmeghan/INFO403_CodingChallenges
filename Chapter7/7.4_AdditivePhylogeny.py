'''
Goal: Implement Additive Phylogeny to solve the Distace-Bases Phylogeny Problem
Input: An integer n followed by a space separated nxn distance matrix
Output: A weighted adjacenty list for the simple tree fitting this matrix 

AdditivePhylogeny(D)
    n ← number of rows in D
    if n = 2
        return the tree consisting of a single edge of length D1,2
    limbLength ← Limb(D, n)
    for j ← 1 to n - 1
        Dj,n ← Dj,n - limbLength
        Dn,j ← Dj,n
    (i, k) ← two leaves such that Di,k = Di,n + Dn,k
    x ← Di,n
    D ← D with row n and column n removed
    T ← AdditivePhylogeny(D)
    v ← the (potentially new) node in T at distance x from i on the path between i and k
    add leaf n back to T by creating a limb (v, n) of length limbLength
    return T

*Formatting Note: The adjacency list must have consecutive integer node labels starting from 0. 
The n leaves must be labeled 0,1,...,n-1 in order of their appearance in the distacne matrix. 
Labels for internal nodes may be labeled in any order by must start from n and increase consecutively.

./testcases/AdditivePhylogenySample.txt
'''

def ReadFile():
    with open('./datasets/dataset_609178_6.txt', 'r') as f:
        n = int(f.readline().strip())
        distanceMatrix = [list(map(int, line.strip().split()))for line in f.readlines()]
    return n , distanceMatrix

def LimbLength(dist, target):
	n = len(dist)
	lim_length = float("inf")
	#for every element in n as long as it is not i or j calculate the distance
	#if it is smaller than the previous distance calculated set that as new smallest distance
	for i in range(n):
		for j in range(n):
			if i != target and j != target:
				tem = (dist[i][target]+dist[j][target]-dist[i][j])/2
				if tem < lim_length:
					lim_length = tem
	return int(lim_length) 

def additive_phylogeny(dist,n):
	#function to find a path between two given nodes 
	def find_path(i,j):
		visited = [None] * (max(adj.keys())+1)
		#depth first search algorithm function used to traverse the tree
		def dfs(path):
			for (v,w) in adj[path[-1][0]]:
				if visited[v] == True:
					continue
				visited[v] = True
				pathlen = path[-1][1] + w
				npath = path[:]
				npath.append((v,pathlen))
				if (v == j):
					# found the node that ends path.
					return npath
				result = dfs(npath)
				if result is not None:
					return result
			return
		return dfs([(i,0)])
	#function to calcuate the distance between two nodes with a third node between the two 
	def find_condition(dist, l):
		for i in range(l):
			for j in range(i+1,l):
				if dist[i][j] == dist[i][l]+dist[j][l]:
					return (i,j)
		assert 0
		return


	# add a new leaf to the tree with distance x between i and k
	def add_leaf(leaf,i,j,x,w):
		path = find_path(i,j)
		parent = None
		for k in range(len(path)-1):
			if path[k][1] == x:
				parent = path[k][0]
				break
			if path[k][1] < x and x< path[k+1][1]:
				u = path[k][0]
				v = path[k+1][0]
				w0 = path[k+1][1] - path[k][1]
				w1 = x - path[k][1]
				w2 = path[k+1][1] - x
				parent = max(list(adj.keys())+[n-1]) + 1
				adj[u].remove((v,w0))
				adj[v].remove((u,w0))
				adj[parent] = []
				adj[u].append((parent,w1))
				adj[parent].append((u,w1))

				adj[v].append((parent,w2))
				adj[parent].append((v,w2))
				break
		adj.setdefault(leaf,[]).append((parent,w))
		adj[parent].append((leaf,w))

		return adj


	def recursive(n):
		#return the tree consisting of a single edge of length D1,2
		if n == 2:
			return
		limb = LimbLength(dist[:n][:n],n-1)
		for i in range(n-1):
			dist[i][n-1] -= limb
			dist[n-1][i] -= limb
		#find two leaves such that Di,k = Di,n + Dn,k
		(i,k) = find_condition(dist[:n][:n], n-1)
		x = dist[i][n-1]
		recursive(n-1)
		#add leaf to tree with limblength 
		adj = add_leaf(n-1,i,k,x,limb)
		return adj
	adj = {0: [(1,dist[0][1])],1: [(0,dist[1][0])]}
	recursive(n)
	return adj



n, distanceMatrix = ReadFile()

adj = additive_phylogeny(distanceMatrix,n)
sortedAdj = sorted(adj.items(),key=lambda d:d[0])
with open('AdditivePhylogenySolution.txt', 'w') as output:
    for node in sortedAdj:
        for edge in node[1]:
            #print('%d->%d:%d' %(node[0],edge[0],edge[1]))
            output.write('%d->%d:%d \n' %(node[0],edge[0],edge[1]))