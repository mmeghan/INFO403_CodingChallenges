'''
Goal: Solve the 2-Break Distance Problem.
Input: Genomes P and Q.
Output: The 2-break distance d(P, Q)

*Do Charging Station Problems to help solve this 
 2-break transformation of genome P into Q
2-Break Distance = Blocks(P,Q) - Cycles(P,Q)

'''
def ChromosomeToCycle(Chromosome): 
    Nodes=[]
    #loop through every chromosome adding to Nodes list transforming linear chromosome to cyclic sequence
    #head of synteny block as 2i and tail of synteny block as 2i-1
    for j in range(0,len(Chromosome)):
        i=Chromosome[j]
        if i > 0:
            Nodes.append(2*i-1)
            Nodes.append(2*i)
        else:
            Nodes.append(-2*i) 
            Nodes.append(-2*i-1)
    return Nodes


def ColoredEdges(P):
    Edges = []
    #loop through every chromosome in the genome and get the cyclic sequence for that sequence 
    for chromosome in P:
        Nodes = ChromosomeToCycle(chromosome)
        #loop though chromosome and add to edges the black undirected edges for (2n-1, 2n)
        for j in range(len(chromosome)):
            Edges.append([Nodes[2*j+1],Nodes[(2*j+2)%len(Nodes)]])
    return Edges


def Blocks(P):
    EdgesP = ColoredEdges(P)
    blocks = len(EdgesP)
    return blocks

def Cycles(P,Q):
    #get all P edges
    EdgesP = ColoredEdges(P)
    #get all Q edges
    EdgesQ = ColoredEdges(Q)
    #combined list of all edges between P and Q
    TotalEdges = EdgesP + EdgesQ
    count = 0
    #while there is an edge left in TotalEdges
    while TotalEdges != []: 
        #and while the first and last nodes in the first pair of edges are not the same
        while TotalEdges[0][0] != TotalEdges[0][-1]:
            #go though the rest of the TotalEdges starting at the next pair
            for i in range(1,len(TotalEdges)):
                #if the fist and last element in the edge pair are the same
                # to the first pair of edges add the scond node in the edge pair
                #remove the current pair of edges from TotalEdges
                if TotalEdges[i][0] == TotalEdges[0][-1]:
                    TotalEdges[0].append(TotalEdges[i][1])
                    TotalEdges.remove(TotalEdges[i])
                    break
                #else if the second and last nodes in the edge paire are the same
                #to the first pair of edges add the first node of the current edge pair
                #remove the current pair of edges from TotalEdges
                elif TotalEdges[i][1] == TotalEdges[0][-1]:
                    TotalEdges[0].append(TotalEdges[i][0])
                    TotalEdges.remove(TotalEdges[i])
                    break
        TotalEdges.remove(TotalEdges[0])
        count += 1
    return count 

with open('./datasets/dataset_609165_4.txt','r') as f:
    data = f.readlines()
f.close()

inputChromosomeP = data[0]
inputChromosomeP = inputChromosomeP.strip()
inputChromosomeP = inputChromosomeP[1:-1].split(")(")
n = len(inputChromosomeP)
P = []
for i in range(n):
    P.append([int(x) for x in inputChromosomeP[i].split()])

inputChromosomeQ = data[1]
inputChromosomeQ = inputChromosomeQ.strip()
inputChromosomeQ = inputChromosomeQ[1:-1].split(")(")
n= len(inputChromosomeQ)
Q=[]
for i in range(n):
    Q.append([int(x) for x in inputChromosomeQ[i].split()])

twoBreakDistance = Blocks(P) - Cycles(P,Q)
print(twoBreakDistance)