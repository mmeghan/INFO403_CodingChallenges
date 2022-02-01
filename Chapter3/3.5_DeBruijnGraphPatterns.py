'''
Construct the de Burijn graph from a set of k-mers
input - a collection of k-mer patterns
output- the adjacency list of the de Burijn graph DeBruijn(Patterns)
'''

def ReadFile(file):
    with open(file, 'r') as f:
        data = f.readlines()
        patterns = []
        for sequence in data:
            patterns.append(sequence.strip())
        
    return patterns

def suffix(pattern):
    return pattern[1:]
def prefix(pattern):
    return pattern[0:(len(pattern)-1)]

def deBrujin(file):
    patterns = ReadFile(file)
    print(patterns)
    k = len(patterns[0])
    graph = {}

    for pattern in patterns:
        if prefix(pattern) not in graph.keys():
            graph[prefix(pattern)] = suffix(pattern)
        else:
            graph[prefix(pattern)] += ','+suffix(pattern)
    return graph 


result = deBrujin('dataset_609098_8.txt')
with open ('deBruijnPatternSolution.txt', 'w') as solution:
    for key in sorted(result.keys()):
        solution.write(key + '->' + result[key]+ '\n')
