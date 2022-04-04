'''
Goal: Solve the Suffic Tree Construction Problem
Input: A string Text 
Output: A space separated list of the edge labels of SuffixTree(Text). Strings may be returned in any order

./testcases/SuffixTreeConstruction_Sample.txt

'''
def ReadFile():
    with open('./datasets/dataset_609219_4.txt', 'r') as f:
        Text =  f.readline().strip()
    return Text 

class SuffixTree:
    next_seq = 0
    class Node:
        def __init__(self):
            self.symbol         = None
            self.edges          = {}
            self.label          = None
            self.seq            = SuffixTree.next_seq
            SuffixTree.next_seq += 1
 
        def hasLabelledEdge(self,symbol):
            return symbol in self.edges
        
        def endEdge(self,symbol):
            return self.edges[symbol] 
        
        def isLeaf(self):
            return len(self.edges)==0
        
        def setLabel(self,j):
            self.label=j

        def print(self,path=[]):
            if len(self.edges)==0:
                print (f"{self.label}, {''.join(path)}" )
            else:
                for symbol,edge in self.edges.items():
                    edge.node.print(path=path+[symbol])
        def create_adj(self,adj={}):
            if len(self.edges)==0:
                adj[self.seq] = {}
            else:
                adj[self.seq] = [edge.node.seq for edge in self.edges.values()]
                for edge in self.edges.values():
                    edge.node.create_adj(adj)
 
        def collectEdges(self,path=[],accumulator=[]):
            if len(self.edges)==0:
                accumulator.append(path+[self.symbol])
            elif len(self.edges)==1:
                for symbol,edge in self.edges.items():
                    edge.node.collectEdges(path+[symbol],accumulator=accumulator)                
            else:
                if len(path)>0:
                    accumulator.append(path+[self.symbol])
                for symbol,edge in self.edges.items():
                    edge.node.collectEdges([symbol],accumulator=accumulator)
            return accumulator
    class Edge:
        def __init__(self,node,position):
            self.node     = node
            self.position = position
    def __init__(self):
        self.root = self.Node()
    
    def build(self,text):
        Leaves   = []
        Internal = []
        Nodes    = {}
        for i in range(len(text)):
            currentNode = self.root
            for j in range(i,len(text)):
                currentSymbol = text[j]
                if currentNode.hasLabelledEdge(currentSymbol):
                    currentNode = currentNode.endEdge(currentSymbol).node
                else:
                    newNode                          = self.Node()
                    Nodes[newNode.seq]               = newNode
                    currentNode.edges[currentSymbol] = self.Edge(newNode,j)
                    currentNode                      = newNode
                    Internal.append(newNode)                    
            if currentNode.isLeaf():
                currentNode.setLabel(i)
                Leaves.append(currentNode)
  
                
        return Leaves,Internal,Nodes
    
    def print(self):
        self.root.print()
        
    def create_adj(self):
        adj = {}
        self.root.create_adj(adj)
        return adj
    
    def collectEdges(self):
        return [ ''.join(run[:-1]) for run in self.root.collectEdges(accumulator=[])]


def check(Edges,Expected):
    print (f'Expected = {len(Expected)} edges, actual={len(Edges)}')
    mismatches = 0
    for a,b in zip(sorted(Edges),sorted(Expected)):
        if a!=b:
            mismatches+=1
            print (f'Expected {b}, was {a}')
    print(f'{0} mismatches')

def compare_edges(Edges,Expected):
    print (f'Expected = {len(Expected)} edges, actual={len(Edges)}')
    expected = iter(sorted(Expected))
    edges    = iter(sorted(Edges))
    exp      = next(expected)
    ed       = next(edges)
    while exp != '-' and ed !='-':
        if exp<ed:
            print('{0},{1}'.format(exp,'-'))
            exp = next(expected,'-')           
        elif ed<exp:
            print('{0},{1}'.format('-',ed))
            ed = next(edges,'-') 
        else:
            exp = next(expected,'-')
            ed = next(edges,'-')

Text = ReadFile()
Tree = SuffixTree()
Tree.build(Text)
Edges = Tree.collectEdges()
with open('./solutions/SuffixTreeConstruction_Solution.txt', 'w') as solution:
    for edge in Edges:
        solution.write(edge + '\n')