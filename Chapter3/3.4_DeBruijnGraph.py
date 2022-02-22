'''
De Bruijn Graph from a String Problem: Construct the de Brujin graph of a string
input- an integer k and a string Text 
output- Debruijnk(text) in the form of an adjacency list 
'''

def ReadFile(file):
    with open(file, 'r') as f:
        data = f.readlines()
        k = int(data[0].strip())
        genome = data[1].strip()
    return (genome, k)


def DeBruijnGraph(file):
    inputs= ReadFile(file)
    genome = inputs[0]
    k = inputs[1]
    result = {}
    #edges = []
    #nodes = set()
    for i in range(len(genome)-k +1):
        if genome[i:(i+k-1)] not in result.keys():
            result[genome[i:(i+k-1)]] = genome[i+1:i+k]
        else:
            result[genome[i:i+k-1]] += ',' + genome[i+1:i+k]
    
    return result 



r = DeBruijnGraph('dataset_609097_6.txt')
with open ('deBruijnSolution.txt' , 'w') as s:
    for key in sorted(r.keys()):
        s.write(key + '->' + r[key]+ '\n')

        #print(key + '->' + r[key])
#print(VizualizeDeBruijnGraph('./deBruijnGraphString/inputs/sample.txt'))