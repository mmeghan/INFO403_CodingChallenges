'''
Goal - Sole the Longest Path in a DAG Problem
input -  An integer representing the starting node to consider in a graph, 
         followed by an integer representing the ending node to consider, 
         followed by a list of edges in the graph.
    * The edge notation "0->1:7" indicates that an edge connects node 0 to node 1 
    with weight 7.  You may assume a given topological order corresponding to nodes 
    in increasing order.
output - The length of a longest path in the graph, followed by a longest path.

dataset_609144_7
./testcases/04_LongestPathDAG/inputs/sample.txt
'''

import random
import copy


def ReadFile():
    with open('./datasets/dataset_609144_7.txt') as f:
        adj = {}
        weightMatrix = {}
        start = f.readline()
        start = start.strip()
        end = f.readline()
        end = end.strip()
        data = f.readlines()
        for i in range(len(data)):
            element = data[i].strip()
            element = element.split('->')
            fromNode = int(element[0])
            result = element[1].split(':')
            toNode = int(result[0])
            weight = int(result[1])
            if fromNode not in adj:
                adj[fromNode]= []
                weightMatrix[fromNode]= []
            adj[fromNode].append(toNode)
            weightMatrix[fromNode].append(weight)

    return (start, end, adj, weightMatrix)

def TopologialOrder (adj, nodes, start, end):
    ordered = []
    candidates = []
    values = []
    copyDict = copy.deepcopy(adj)
    edgesList = []
    for vals in adj.values():
        for val in vals:
            values.append(val)
    for node in nodes:
        if node not in values:
            candidates.append(node)
    while candidates:
        node = candidates[random.randint(0,len(candidates)-1)]
        ordered.append(node)
        candidates.remove(node)
        if node in adj.keys():
            outgoingEdges = adj[node]
            for outgoingEdge in outgoingEdges:
                edge = (node, outgoingEdge)
                if edge not in edgesList:
                    edgesList.append(edge)
                    index = copyDict[node].index(outgoingEdge)
                    del copyDict[node][index]

                    valsNewGraph = []
                    for vals in copyDict.values():
                        for val in vals:
                            valsNewGraph.append(val)
                    if outgoingEdge not in valsNewGraph:
                        candidates.append(outgoingEdge)
    return ordered

def predecessor(node, adj):
    predecessor = []
    for key in adj.keys():
        values = adj[key]
        for val in values:
            if node == val:
                predecessor.append(key)
    return predecessor

def LongestPath (start, end, adj, weight):
    nodes = []
    longesPath = {}
    for node in adj.keys():
        if node not in nodes:
            nodes.append(node)
    for vals in adj.values():
        for val in vals:
            nodes.append(val)
    path = {}
    for node in nodes:
        path[node] = -len(adj)
        longesPath[node] = ''

    path[start] = 0 
    longesPath[start] = str(start)
    TopologicalGraph = TopologialOrder(adj, nodes, start, end)
    index = TopologicalGraph.index(start)

    for i in range(index+1, len(TopologicalGraph)):
        node = TopologicalGraph[i]
        predecess = predecessor(node,adj)
        if len(predecess) != 0 :
            options = []
            paths = []
            for pred in predecess:
                if pred in TopologicalGraph:
                    index = adj[pred].index(node)
                    options.append(path[pred] + weight[pred][index])
                    paths.append(longesPath[pred] + " " + str(node))
            path[node] = max(options)
            newIndex = options.index(max(options))
            longesPath[node] = paths[newIndex]
    return path[end], longesPath[end]


inputs = ReadFile()
start = int(inputs[0])
end = int(inputs[1])
adj = inputs[2]
weight = inputs[3]
longestPathLength, longestPath = LongestPath(start, end, adj, weight)
print(longestPathLength)
longestPath = longestPath.split()
txt = str(longestPath[0])
for i in range(1, len(longestPath)):
    txt += '->' + longestPath[i]
print(txt)