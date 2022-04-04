'''
Goal:Find the longest repeat in a string 
Input: A string Text 
Output: A longest substring of Text that appears in Text more than once 


./testcases/LongestRepeat_Sample.txt
'''
import sys
sys.setrecursionlimit(1500)
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


def ReadFile():
    with open('./datasets/dataset_609219_5.txt', 'r') as f:
        Text = f.readline().strip()
    return Text 

def sort_by_descending_length(edges):
    return [e for _,e in sorted([(len(edge),edge) for edge in edges],reverse=True)]

def FindLongestRepeat(string1,string2=None):        
    tree = SuffixTree()
    string = string1 if string2 == None else string1 + string2
    tree.build(string)
    edges = sort_by_descending_length(tree.collectEdges())
    for edge in edges:
        index1 = string.find(edge,0,-1 if string2==None else len(string1))
        if index1==-1: continue
        index2 = string.find(edge,(index1+1) if string2==None else len(string1))
        if index2==-1: continue
        # try to extend edge -- first to the left
        i = 1
        while string[index1-i]==string[index2-i]:
            i+=1
        i -= 1
        # then to the right
        j  = len(edge)
        while index2+j<len(string) and string[index1+j]==string[index2+j]:
            j+=1

        return string[index1-i:index1+j]

Text = ReadFile()
Result = FindLongestRepeat(Text)
print(Result)