#input - A collection of Patterns of k-mers
#output - the overlap graph Overlap(Patterns), in the form of an adjacency list
    #may return nodes and their edges in any order

def ReadFile(file):
    strings = []
    with open(file, 'r') as f:
        data = f.readlines()
        for i in data:
            strings.append(i.strip())
    return (strings)

def suffix(pattern):
    return pattern[1:]
def prefix(pattern):
    return pattern[0:(len(pattern)-1)]

def GraphPrint(adj_list):
    with open('OverlapGraphSolution.txt', 'w') as solution:
        for key in adj_list.keys():
            if len(adj_list[key]) > 0:
                solution.write(key+ '-> ')
                if len(adj_list[key]) > 1:
                    for element in adj_list[key]:
                        solution.write(element + ', ')
                else:
                    for element in adj_list[key]:
                        solution.write(element )
                solution.write('\n')
                

def ConstructGraph(file):
    strings = ReadFile(file)

    adj_list= dict()
    for pattern in strings:
        adj_list[pattern] = []
    for pattern in strings:
        for pattern2 in strings:
            if suffix(pattern) == prefix(pattern2):
                adj_list[pattern].append(pattern2)
    
    GraphPrint(adj_list)

    return adj_list

'''
solution = open('OverlapGraphSolution.txt', 'w')
result = ConstructGraph('./OverlapGraph/inputs/test5.txt')
for e in result:
    print(e +" - > "+ result[e][0])
    solution.writelines(e +" -> "+ result[e][0] +"\n")
'''
#ConstructGraph('./OverlapGraph/inputs/sample.txt')

ConstructGraph('dataset_609096_10.txt')