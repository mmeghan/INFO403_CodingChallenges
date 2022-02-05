'''
the String Reconstruction Problem reduces to finding an Eulerian path in the de Bruijn graph generated from reads.
We can therefore summarize this solution using the following pseudocode,
which relies on three problems that we have already solved:

The de Bruijn Graph Construction Problem;
The Eulerian Path Problem;
The String Spelled by a Genome Path Problem.

StringReconstruction(Patterns)
    dB ← DeBruijn(Patterns)
    path ← EulerianPath(dB)
    Text ← PathToGenome(path)
    return Text

Code Challenge: Solve the String Reconstruction Problem.

Input: An integer k followed by a list of k-mers Patterns.
Output: A string Text with k-mer composition equal to Patterns. (If multiple answers exist, you may return any one.)

'''

def ReadFile(file):
    with open (file, 'r') as f:
        data = f.readlines()
        k = int(data[0].strip())
        patterns = []
        for sequence in data[1::]:
            patterns.append(sequence.strip())
    return (k, patterns)

def suffix(pattern):
    return pattern[1:]
def prefix(pattern):
    return pattern[0:(len(pattern)-1)]

def deBrujin(k, patterns):
    graph = {}
    for pattern in patterns:
        if prefix(pattern) not in graph.keys():
            graph[prefix(pattern)] = suffix(pattern)
        else:
            graph[prefix(pattern)] += ','+suffix(pattern)
    print(graph)
    return graph

def FindEulerianPath(adj_list, vertices, indegree, outdegree):
    #sun in-degree and out-degree
    indegree = dict.fromkeys(vertices, 0)
    outdegree = dict.fromkeys(vertices, 0)
    for vertex in vertices:
        if vertex in adj_list:
            outdegree[vertex] = len(adj_list[vertex])
            print(vertex, outdegree[vertex])
            print(adj_list[vertex])
            
            for edge in adj_list[vertex]:
                print('edge', edge)
                indegree[edge] += 1
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

def StringReconstruction():
    fileinputs = ReadFile('./StringReconstruction/inputs/sample.txt')
    k= fileinputs[0]
    print('k: ',  k)
    patterns = fileinputs[1]
    print('patterns: ', patterns)

    db = deBrujin(k , patterns)
    print('drBrijn: ', db)

    adj_list = {}
    vertices = set()
    indegree = {}
    outdegree = {}
    for vertex, edge in db.items():
        vertices.add(vertex)
        edge = [n for n in edge.split(',')]
        vertices = vertices | set(edge)
        adj_list[vertex] = edge
    print('adj_list:', adj_list)
    path = FindEulerianPath(db, list(vertices), indegree, outdegree)
    print(path)

#ReadFile('./StringReconstruction/inputs/sample.txt')
StringReconstruction()

