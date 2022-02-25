'''
Code Challenge: Solve the k-Universal Circular String Problem.

Input: An integer k.
Output: A k-universal circular string.


NOTE: Could not solve becuase kept getting weird error "UnboundLocalError: local variable 'start_node' referenced before assignment" 
	   not sure why this is happening 
'''

from copy import deepcopy
import random


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

def deBrujin(patterns):
    graph = {}
    for pattern in patterns:
        if pattern[:-1] not in graph:
            graph[pattern[:-1]] = []
            graph[pattern[:-1]].append(pattern[1:])
        else:
            graph[pattern[:-1]].append(pattern[1:])
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
    genome = path[0]
    for element in path[1:]:
        genome += element[-1]
    return genome

def kUniversal(n):
	text = ''
	kmers = []
	for i in range (2**n):
		kmer = format(i,'b')
		if len(kmer) < n:
			diff = n - len(kmer)
			kmer = ('0' *diff) + kmer
		kmers.append(kmer)
	dB = deBrujin(kmers)
	path = EulerianPath(dB)
	edges = []
	for i in range (len(path)-1):
		edge = path[i] + path[i+1][-1:]
		edges.append(edge)
	text = GenomeConstruction(edges)
	text = text[:-(n-1)]
	return text

print(kUniversal(4))
