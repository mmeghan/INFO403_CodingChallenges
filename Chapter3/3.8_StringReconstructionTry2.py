'''
*Second attempt for 3.8 string reconstruction problem
Goal: Solve the String Reconstruction Problem 
Inputs: an integer k folloeed vy a list of k-mers Patterns
Output: A string Text with k-mer composition equal to Patterns 
        if multiple answers exist can return anyone 

./datasets/dataset_609101_7.txt

'''
import sys
sys.setrecursionlimit(10**6)

def ReadFile():
     
    return (k, patterns)

def SuffixComposition(k, string, uniq = False):
    kmers = []
    for i in range(len(string)+1-k):
        kmers.append(string[i:i+k-1])
    if uniq:
        return sorted(list(kmers))
    else:
        return sorted(kmers)

def Suffix(string):
    return string[1:]

def Prefix(string):
    return string[0:-1]

def BalancedCount(adj):
    BalancedCount = dict.fromkeys(adj.keys(),0)
    for node in adj.keys():
        for out in adj[node]:
            BalancedCount[node] -= 1
            try:
                BalancedCount[out] += 1
            except:
                BalancedCount[out]=1
    return BalancedCount

def DeBruijn(patterns, k):
    #returns a DeBruijn graph for a set of overlapping patterns 
    kmers = []
    for pattern in patterns:
        kmers = kmers + SuffixComposition(k, pattern, uniq = True)
    kmers = set(kmers)
    dict = {}
    for kmer in kmers:
        dict[kmer] = []
    for kmer in patterns:
        dict[Prefix(kmer)].append(Suffix(kmer))
    return dict, kmers 




def EulerianPath(dict):
    
    stack = []
    balancedCount = BalancedCount(dict)
    print(balancedCount)
    stack.append([k for k, v in balancedCount.items() if v==-1][0])
    path = []
    while stack != []:
        EdgeVertex = stack[-1]
        try:
            weight = dict[EdgeVertex][0]
            stack.append(weight)
            dict[EdgeVertex].remove(weight)
        except:
            path.append(stack.pop())
    return path[::-1]

def GenomePath(kmers, appendLast = True):
    genome = ''
    for kmer in kmers:
        genome += kmer[0]
    if appendLast:
        genome += kmer[1:]
    return genome 


def StringReconstruction():
    inputs = ReadFile()
    k = inputs[0]
    patterns = inputs[1]
    adj_list, verticies = DeBruijn(patterns,k)
    
    eulerianPath = EulerianPath(adj_list, verticies)
    genome = GenomePath(eulerianPath)
    return genome 

print(StringReconstruction())

    
    
