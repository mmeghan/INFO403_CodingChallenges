'''
*Second attempt for 3.8 string reconstruction problem
Goal: Solve the String Reconstruction Problem 
Inputs: an integer k folloeed vy a list of k-mers Patterns
Output: A string Text with k-mer composition equal to Patterns 
        if multiple answers exist can return anyone 

./datasets/dataset_609101_7.txt


***THIS IS MY CURRENT WORKING VERSION***
'''
from copy import deepcopy
import random

import sys
sys.setrecursionlimit(10**6)

def ReadFile():
    with open('./testcases/StringReconstruction/inputs/sample.txt', 'r')as f:
        k = int(f.readline().strip())
        patterns = [line.strip() for line in f.readlines()]
    return (k, patterns)

def FindStart(adj_list):
    start = {}
    for one in adj_list:
        start.setdefault(one, 0)
        start[one] += len(adj_list[one])
    end = {}
    for one in adj_list:
        for two in adj_list[one]:
            end.setdefault(two, 0)
            end[two] += 1
    for one in end:
        try: 
            if start[one] != end[one]:
                if start[one] > end[one]:
                    start_node = one
                if start[one] < end[one]:
                    end_node = one
        except KeyError:
            end_node = one

    for one in start:
        try:
            if end[one] != start[one]:
                if end[one] < start[one]:
                    start_node = one
                if end[one] > start[one]:
                    end_node = one
        except KeyError:
            start_node = one
    return start_node, end_node


def deBrujin(k,patterns):
    graph = {}
    for pattern in patterns:
        for i in range(len(pattern)-k+1):
            if pattern[i:(i+k-1)] not in graph.keys():
                graph[pattern[i:(i+k-1)]] = []
                graph[pattern[i:(i+k-1)]].append(pattern[i+1:i+k])
            else:
                graph[pattern[i:i+k-1]].append(pattern[i+1:i+k])
    return graph 

def EulerianPath(adj_list):
    circut_max = len(adj_list.values())
    start_node, end_node = FindStart(adj_list)  
    if end_node not in adj_list.keys():
        adj_list.setdefault(end_node, [])
    adj_list[end_node].append(start_node)

    red_adj_list= {}
    red_adj_list = deepcopy(adj_list)

    start = start_node
    print('Start Node:', start)
    curr = start

    stack = []
    circut = []
    while len(circut) != circut_max+1:
        if red_adj_list[curr] != []:
            stack.append(curr)
            step = random.choice(red_adj_list[curr])
            red_adj_list[curr].remove(step)
            curr = step
        else:
            circut.append(curr)
            curr = stack[len(stack)-1]
            stack.pop()
    circut.pop(0)

    path = start + '->'
    for vertex in circut[::-1]:
        path += (vertex + '->')
    return path.strip('->')

def GenomeConstruction(path):
    n = len(path)
    print('n:', n)
    genome = str(path[0])
    for element in path[1:]:
        nucleotide= element[0]
        genome += nucleotide
    last_elem = path[n-1]
    genome += last_elem[1]
    return genome 

def StringReconstruction():
    inputs = ReadFile()
    k = inputs[0]
    patterns = inputs[1]
    print('patterns:',patterns)
    deBruijn = deBrujin(k, patterns)
    print('dbBruijn:',deBruijn)
    path = EulerianPath(deBruijn)
    print(path)
    kmers = path.split('->')
    genome = GenomeConstruction(kmers)
    print(genome)




StringReconstruction()

    
    
