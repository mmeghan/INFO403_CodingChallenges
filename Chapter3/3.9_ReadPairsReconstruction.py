'''
Goal: Solve The String Reconstruction from Read-Pairs 
Input: integers k, and d, followed by a collection of paired k-mers Paired Reads
Output: a string text with(k,d)-mer composition equal to Paired Reads

*Notes: d = the fixed distance which the pairs of reads are separated in the genome 
./testcases/PairedStringReconstruction/inputs/textbookExample.txt

./datasets/dataset_609102_16.txt
'''
from copy import deepcopy
import random
import sys
sys.setrecursionlimit(10**6)

def ReadFile():
    with open('./testcases/PairedStringReconstruction/inputs/sample.txt', 'r') as f:
        values = f.readline().strip()
        k =  50 #int(values[0])
        d = 200 #int(values[2])
        data = f.readlines()
        kdmers = {}
        for i in data:
            kdmer1, kdmer2 = i.strip().split('|')
            key = (kdmer1[:-1], kdmer2[:-1])
            val = (kdmer1[1:], kdmer2[1:])
            kdmers.setdefault(key,[]).append(val)
    return k, d, kdmers 

def Start(adj_list):
    degrees = {}
    for k,vn in adj_list.items():
        if k not in degrees: degrees[k] = 0
        degrees[k] += len(vn)
        for v in vn:
            if v not in degrees: degrees[v] = 0
            degrees[v] -= 1
    s = 0
    t = 0
    for k , v in degrees.items():
        if v > 0:
            s += 1
            curr = k
        if v < 0:
            t += 1
    return curr

def deBruijn(kdmers):
    graph = {}
    for kdmer in kdmers:
        prefix = (kdmer[0][:-1], kdmer[1][:-1])
        suffix = (kdmer[0][1:], kdmer[1][1:])
        if prefix not in graph.keys():
            graph[prefix] = []
            graph[prefix].append(suffix)
        else:
            graph[prefix].append(suffix)
    return graph 

def EulerianPath(adj_list, curr, circut, stack):
    while True:
        if adj_list[curr]:
            stack.append(curr)
            step = adj_list[curr].pop(0)
            curr = step
        else:
            circut.append(curr)
            curr = stack.pop()
        if all([a == [] for a in adj_list.values()]):
            break
    circut.append(curr)
    while stack:
        circut.append(stack.pop())
    circut.reverse()
    return circut


def GenomeConstruction(path, k,d):
    prefix , suffix = path[0][0], path[0][1]
    for pair in path[1:]:
        prefix += pair[0][-1]
        suffix += pair[1][-1]
    print('prefix', prefix)
    print('suffix', suffix)
    seq = prefix + suffix[-(k+d):]
    return seq

k , d, kdmers = ReadFile()
adj_list = deBruijn(kdmers)
startNode  = Start(adj_list)
circut = []
stack = []
path = EulerianPath(adj_list, startNode, circut, stack)
print(path)
sequence = GenomeConstruction(path, k, d)
print('sequence:', sequence)