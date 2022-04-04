'''
Goal: Solve the Trie Construction Problem 
Input: A space separated collection of strings Pattens 
Output: The adjacency list corresponding to Trie(Patterns)
    Format: if Trie(Patterns) has n nodes, first label the root with 0 and then
    label the remaining nodes with integers 1 through n-1 in any order, Each edge 
    of the adjacency list of Trie(Pattersn) will be encoded by a triplet: the first two 
    members of the triple must be the integers labeling the inital and terminal nodes of the edge,
    resprectively; the third member of the triple must be the symbol labeling the edge 

Sample Output: 
0 1 A
1 2 T
2 3 A
3 4 G
4 5 A
2 6 C
0 7 G
7 8 A
8 9 T


./testcases/TrieConstruction_Sample.txt

'''
class Node:
    def __init__(self, children, number, symbol, parent):
        self.children = children
        self.number = number 
        self.symbol = symbol
        self.parent = parent 
    def addChildren(self, child):
        self.children.append(child)
    def getChildren(self):
        return self.children
    def getNumber(self):
        return self.number
    def getSymbol(self):
        return self.symbol
    def getParent(self):
        return self.parent 

def ReadFile():
    with open ('./datasets/dataset_609217_4.txt', 'r') as f:
        data = f.read()
        Patterns = data.strip().split()
    return Patterns




def TrieConstruction(Patterns):
    root = Node([],0,'',None)
    Trie = [root]
    number = 0
    #main for loop going through every pattern given and strored in Patterns 
    for pattern in Patterns:
        currentNode = root 
        #looping through each letter in the pattern
        for i in range(len(pattern)):
            currentSymbol = pattern[i]
            isChild = False
            #look through the current children listed for the node
            for child in currentNode.getChildren():
                #check to see if the child is listed and if so move to that node
                if child.getSymbol() == currentSymbol:
                    currentNode = child
                    isChild = True
            #else the child is not listed so a new node is created off the parent and that child is listed under its parent  
            if isChild == False:
                number += 1 
                newNode = Node([], number, currentSymbol, currentNode)
                Trie.append(newNode)
                currentNode.addChildren(newNode)
                currentNode = newNode
    TrieNodes = {}
    #looping though every node of the Trie to get its number, letter, and parent 
    for node in Trie:
        if node.symbol != '':
            number = node.getNumber()
            symbol = node.getSymbol()
            parent = node.getParent()
            parentNumber = parent.getNumber()
            TrieNodes[(parentNumber, number)] = symbol
    return TrieNodes


        
Patterns = ReadFile()
trie = TrieConstruction(Patterns)
with open('./solutions/TrieConstruction_Solution.txt', 'w') as solution:
    for KeyPair in trie.keys():
        data = str(KeyPair[0]) + ' ' + str(KeyPair[1]) + ' ' + str(trie[KeyPair])
        solution.write(data + '\n')

