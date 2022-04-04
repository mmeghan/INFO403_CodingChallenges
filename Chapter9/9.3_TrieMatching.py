'''
Goal: Implement Trie Matching to solve the Multiple Pattern Matching Pattern 
Input: A string text and a space separated collection of strings Patterns 
Output: All starting positions in Text where a string from Patterns appears as a substring 
Sample Output: 
    ATCG: 1 11
    GGGT: 4 15
'''


def ReadFile():
    with open('./testcases/TrieMatching_Sample.txt', 'r') as f:
        Text = f.readline().strip()
        Patterns = f.readline().strip()
        Patterns = Patterns.split()
    return Text, Patterns 

class Node: 
	def __init__(self, children, number, symbol, parent, pattern):
		self.children = children 
		self.number = number 
		self.symbol = symbol 
		self.parent = parent
		self.pattern = pattern 

	def addChildren(self, childToAdd): 
		self.children.append(childToAdd)

	def getChildren(self):
		return self.children 

	def getNumber(self): 
		return self.number 

	def getSymbol(self): 
		return self.symbol

	def getParent(self):
		return self.parent

	def getPattern(self):
		return self.pattern



def TrieConstruction(patterns):
	root = Node([], 0, '', None, '')
	Trie = [root] 
	number = 0
    #main for loop going through every pattern given and strored in Patterns 
	for pattern in patterns: 
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
			currentPattern = currentNode.getPattern() 
            #else the child is not listed so a new node is created off the parent and that child is listed under its parent  
			if isChild == False: 
				number += 1
				newPattern = currentPattern + currentSymbol
				newNode = Node([], number, currentSymbol, currentNode, newPattern)
				Trie.append(newNode)
				currentNode.addChildren(newNode)
				currentNode = newNode

	return Trie

def prefixTrieMatching(text, trie):
	counter = 0
	symbol = text[counter]
	v = trie[0]
	while True: 
		if v.getChildren() == []: 
			return v.getPattern() 
		else:
			isChild = False 
			for child in v.getChildren(): 
				if child.getSymbol() == symbol: 
					counter += 1
					if counter < len(text):
						symbol = text[counter]
					v = child 
					isChild = True 
					break
			if isChild == False:
				return ''

def TrieMatching(text, trie):
	positions = [] 
	i = 0
	while len(text) > 0: 
		if prefixTrieMatching(text, trie) != '':
			positions.append(i)
		i += 1
		text = text[1:]
	return positions 


Text, Patterns = ReadFile()
Trie = TrieConstruction(Patterns)
Positions = TrieMatching(Text, Trie)
# need to format output correctly. Getting the right numbers though
for position in Positions:
    print(position)