'''
Goal: Solve The String Reconstruction from Read-Pairs 
Input: integers k, and d, followed by a collection of paired k-mers Paired Reads
Output: a string text with(k,d)-mer composition equal to Paired Reads

*Notes: d = the fixed distance which the pairs of reads are separated in the genome 
./testcases/PairedStringReconstruction/inputs/textbookExample.txt

./datasets/dataset_609102_16.txt

def string_reconstruction_from_read_pairs(patterns, d):
    print('Patterns:', patterns)
    dB = debruijn_from_read_pairs(patterns)
    print('dB:', dB)
    path = eulerian_path_problem(dB)
    print('Path:', path)
    sequence = genome_path_problem(path, d)
    print('Sequence:',sequence)


./datasets/dataset_609102_16.txt

'''
from copy import deepcopy
import random
import sys; sys.setrecursionlimit(10**6) 

def DeBruijn_pairs(reads):
    
    Adjacency = {}
    for read in reads:
        prefix = (read[0][:-1], read[1][:-1])
        suffix = (read[0][1:], read[1][1:])
        if prefix not in Adjacency:
            Adjacency[prefix] = [suffix]
        else:
            Adjacency[prefix].append(suffix)
            
    return Adjacency


def get_source(graph):

    deg = {}    
    for v in graph:
        if v not in deg.keys():
            deg[v] = -len(graph[v])
        else:
            deg[v] -= len(graph[v])
        for u in graph[v]:
            if u not in deg.keys():
                deg[u] = 1
            else:
                deg[u] += 1
    for v in deg:
        if deg[v] == -1:
            return v 
    print('graph does not have an eulerian path, no source.')

def dfs(v, graph, eulerian, stack):
    circut_max = len(graph.values())
    red_adj_list= {}
    red_adj_list = deepcopy(graph)
    curr = v 

    while len(eulerian) != circut_max+1:
        if red_adj_list[curr] != []:
            stack.append(curr)
            step = random.choice(red_adj_list[curr])
            red_adj_list[curr].remove(step)
            curr = step
        else:
            eulerian.append(curr)
            curr = stack[len(stack)-1]
            stack.pop()
    eulerian.pop(0)
    return eulerian

def reconstruct(eulerian):
    prefs, suffs = eulerian[0][0], eulerian[0][1]
    
    for pair in eulerian[1:]:
        prefs += pair[0][-1]
        suffs += pair[1][-1]
    
    if prefs[k+d:] == suffs[:-(k+d)]:
        print('aligned pref + suff strings')
    seq = prefs + suffs[-(k+d):]
    
    return seq



f = open('./testcases/PairedStringReconstruction/inputs/sample.txt', 'r')
k, d  = (int(i) for i in f.readline().strip().split(' '))
reads = []
reads = []
reads = list(tuple(i.strip('()').strip().split('|')) for i in f.readlines())
print(reads)

graph = DeBruijn_pairs(reads)
print('graph:',graph)
source = get_source(graph)
print('source:',source)
eulerian = []
stack = []
dfs(source, graph, eulerian, stack)
print('eulerian:',eulerian)
eulerian.reverse()
seq = reconstruct(eulerian)
print(seq)
