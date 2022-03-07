'''
Class Example for 7.2 

'''

import re


adj_list = '''0->4:11
1->4:2
2->5:6
3->5:7
4->0:11
4->1:2
4->5:4
5->4:4
5->3:7
5->2:6'''.split('\n')
# pulled from ch 5 part 1
def ParseEdges(Graph):

    edges= {}
    edge_weight = {}
    for pair in [edge.strip().split('->') for edge in Graph]:
        if int(pair[0]) not in edges:
            edges[int(pair[0])] = [int(pair[1].split(':')[0])]
        else:
            edges[int(pair[0])].append(int(pair[1].split(':')[0]))

        edge_weight[int(pair[0]), int(pair[1].split(':')[0])] = int(pair[1].split(':')[1])

    return edges, edge_weight


def DistanceToOtherLeafs(adj_list, source):
    # gets the distance to every other leaf from a source leaf
    edges, edge_weight = ParseEdges(adj_list)
    scores = {}
    scores[source] = 0
    checked_nodes = []
    nodes = [source]
    # While there are unchecked nodes
    while nodes:
        i = nodes.pop(0)
        # keep track of what you've checked
        checked_nodes.append(i)
        for end in edges[i]:
            weight = edge_weight[(i,end)]
            # if you haven't checked this node before
            if end not in checked_nodes:
                nodes.append(end)
                # if this is a longer path, or you don't have a path for this end node yet
                if (end in scores and scores[end] < scores[i]+weight) or end not in scores:
                    scores[end] = scores[i]+weight
    return scores

def ReversedParseEdges(adj):
    return 


def DistanceBetweenLeafs():
    #reverse ParesedEdges to get list of of nodes and who it goes to 
    reveresEdges = ReversedParseEdges(adj_list)
    #find all the leaves
    leaves = []
    #go though every node and reverse edges and find ones of list lenght 1
    for startNode in reveresEdges:
        #leaves only have one edge
        if len(reveresEdges[startNode]) == 1:
            leaves.append(startNode)
    leaves.sort()
    out = []
    for leaf in leaves:
        #get the distances for each leaf to every other node
        scores = DistanceToOtherLeafs(adj_list, leaf)
        inner_out = []
        for leaf in leaves:
            #remember just the distances to other leaves
            inner_out.append(scores[leaf])
        #add inner list to outer list
        out.append(inner_out)

    return out


