'''
Solve the Eulerian Cycle Problem
input - the adjacency list of an Eulerian directed graph 
output - an eulerian cycle in this graph 
'''
'''
EulerianCycle(Graph)
    form a cycle Cycle by randomly walking in Graph (don't visit the same edge twice!)
    while there are unexplored edges in Graph
        select a node newStart in Cycle with still unexplored edges
        form Cycle' by traversing Cycle (starting at newStart) and then randomly walking 
        Cycle ← Cycle'
    return Cycle

This one is tricky and can come down more to efficient data structures than anything else. Here are some hints.

Check out the first and third FAQ item at https://www.bioinformaticsalgorithms.org/faq-chapter-3

You may want to make a convenience function that takes in a multiline string, the adjacently list, and spits out a list of tuples consisting of the edges of the graph.

Here is an approach you may want to try:  Hierholzer’s algorithm (time complexity O(V+E)), where V is number of nodes and E is number of edges.

Choose any vertex v and push it onto a stack. Initially all edges are unmarked.
While the stack is nonempty, look at the top vertex, u, on the stack. If u has an unmarked incident edge, say, to a vertex w, then push w onto the stack and mark the edge uw. On the other hand, if u has no unmarked incident edge, then pop u off the stack and print it.
When the stack is empty, you will have printed a sequence of vertices that correspond to an Eulerian circuit
If you're really stuck, the pictures on the blog post (after the initial big block of text) are helpful. But the C code at the bottom is off limits: http://iampandiyan.blogspot.com/2013/10/c-program-to-find-euler-path-or-euler.html
'''

adjList = {}

def ReadFile(file):
    with open(file, 'r') as file:
        while True:
            line = file.readline().rstrip()
            if line is None or line == '':
                break
            key = int(line.split('->')[0].rstrip())
            values = line.split('->')[1].rstrip().split(',')
            values = [int(value.rstrip()) for value in values]
            adjList[key] = values
    return adjList



def FindEulerianCycles (file):
    adj_list = ReadFile(file)
    #print(adj_list)
    edge_count = dict()

    for i in range(len(adj_list)):
        edge_count[i] = len(adj_list[i])
    if len(adj_list) == 0:
        return #empty graph
    #maintain a stack to keep verticies 
    curr_path = []

    #vector to store final cycle 
    cycle = []

    #start from any vertex
    curr_path.append(0)
    curr_v = 0 #current vertex

    while len(curr_path):
        #if there's remaining edge
        if edge_count[curr_v]:
            #push the vertex
            curr_path.append(curr_v)
            #find the next vertex using an edge
            next_v = adj_list[curr_v][-1]
            #remove that edge 
            edge_count[curr_v] -= 1
            adj_list[curr_v].pop()
            #move to next vertex
            curr_v = next_v
        #backtrack to find remaining cycle
        else:
            cycle.append(curr_v)
            #backtracking 
            curr_v = curr_path[-1]
            curr_path.pop()
    #print cycle in reverse (not quite working )
    with open('EulerianCycleSolution.txt', 'w') as solution:
        for i in range (len(cycle)-1,-1,-1):
            solution.write(cycle[i], end = "")
            #print(cycle[i], end = "")
            if i:
                solution.write("-> ", end = "")
                #print("-> ", end = "")
    

FindEulerianCycles('dataset_609101_2.txt')
#FindEulerianCycles('./EulerianCycle/inputs/sample.txt')
