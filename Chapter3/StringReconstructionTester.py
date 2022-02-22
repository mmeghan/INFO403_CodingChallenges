import os
import sys

with open('./testcases/StringReconstruction/inputs/test1.txt', 'r') as f:
    k = int(f.readline().strip())
    patterns = f.readlines()
f.close()
print('K: ', k)
print('patterns: ', patterns)
adjDict = {}
degreeDict = {}
stack = []
cycle = []



def preProcessing(kmers):
    #ADJACENCY LIST
    for patt in kmers:
            adjDict.setdefault(patt.strip()[:-1], []).append(patt.strip()[1:])
    print('adj list: ', adjDict)
    #DEGREE LIST
    for k,vn in adjDict.items():
        if k not in degreeDict: 
            degreeDict[k] = 1
        else: 
            degreeDict[k] += 1
        for v in vn:
            if v not in degreeDict:
                degreeDict[v]= -1
            else: 
                degreeDict[v] -= 1
    print('degree dict:', degreeDict)
    #GET START VERTEX
    s  = 0
    t = 0
    for k,v in degreeDict.items():
        if v > 0:
            s += 1
            curr = k
        if v < 0:
            t += 1
    if s != 1 and t != 1: 
        sys.exit("Eulerian path doesn't exist")
    print('s',s)
    print('t',t)
    print('curr:',curr)
    return curr

def eulerianPath(curr):
    while True:
        if adjDict[curr]:
            stack.append(curr)
            neighbor = adjDict[curr].pop(0)
            curr = neighbor
        else:
            cycle.append(curr)
            curr = stack.pop()
        if all([a == [] for a in adjDict.values()]):
            break
    cycle.append(curr)
    while stack:
        cycle.append(stack.pop())
    cycle.reverse()
    return cycle

current = preProcessing(patterns)
path = eulerianPath(current)

solution = str(path[0])
for element in path[1:]:
    solution += str(element[1:])
print(solution)
'''
with open('./solutions/StringReconstructionSolution.txt', 'w') as file:
    file.write(solution)
file.close()
'''