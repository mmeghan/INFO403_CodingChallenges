'''
Code Challenge: Solve the Eulerian Path Problem.

Input: The adjacency list of a directed graph that has an Eulerian path.
Output: An Eulerian path in this graph.


A nearly balanced graph has an Eulerian path if and only if adding an edge between 
its unbalanced nodes makes the graph balanced and strongly connected.
Eulerian Path is a path in graph that visits every edge exactly once. Eulerian Circuit
is an Eulerian Path which starts and ends on the same vertex. 
'''
from ntpath import join


adj_list = {}
vertices = set()
indegree = {}
outdegree = {}


def FindEulerianPath(adj_list, verticies):
    #sun in-degree and out-degree
    indegree = dict.fromkeys(vertices, 0)
    outdegree = dict.fromkeys(vertices, 0)
    for vertex in vertices:
        if vertex in adj_list:
            outdegree[vertex] = len(adj_list[vertex])
            for edge in adj_list[vertex]:
                indegree[edge] += 1
    print('indegree',indegree)
    print('outdegree', outdegree)
    #determin start and end point 
    start = -1
    end = -1
    for vertex in vertices:
        if indegree[vertex] < outdegree[vertex]:
            start = vertex
        elif indegree[vertex] > outdegree[vertex]:
            end = vertex
    
    #begin path 
    current_path , circuit, v = [start], [], start
    while len(current_path) > 0:
        if outdegree[v]:
            current_path.append(v)
            nextv = adj_list[v].pop()
            outdegree[v] -= 1
            v = nextv
        else:
            circuit.append(v)
            v = current_path.pop()
    circuit.reverse()
    return circuit
    '''    finalPath = start = '->'
    for vertex in circuit[1::]:
        finalPath += (vertex + '->')
    return finalPath.strip('->')
    '''



with open('./datasets/dataset_609101_6.txt', 'r') as f:
    for line in f:
        nodes = line[:-1].split(' -> ')
        u = int(nodes[0])
        vs = [int(n) for n in nodes[1].split(',')]

        vertices.add(u)
        vertices = vertices  | set(vs)
        adj_list[u] = vs

result = FindEulerianPath(adj_list, list(vertices))
#print(result)
finalPath = ' '
for node in result:
    finalPath += (str(node) + '->')


with open ('EulerianPathSolution.txt', 'w') as solution:
    solution.write(finalPath.strip('->'))

    


