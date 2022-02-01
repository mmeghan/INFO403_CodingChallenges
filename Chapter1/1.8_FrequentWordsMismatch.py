#input- a string text as well as integers k and d
#output- all most frequent k-mers with up to d mismatches in text 

def readFile (file):
    with open(file, 'r') as f:
        lines = f.readlines()
        genome = lines[0].strip()
        nums = lines[1].strip()
        parameters = nums.split(' ',1)
        k = int(parameters[0])
        d = int(parameters[1])
        print(parameters)
    return (genome, k, d)

def HammingDistance (substring, pattern):
    mismatches = 0
    for i in range (0, len(substring)):
        if substring[i] != pattern[i]:
            mismatches += 1
    return mismatches



def Neighbors(pattern, d):
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return ['A', 'C', 'G', 'T']
    neighborhood = []
    sufneigh = Neighbors(pattern[1:],d)
    for x in sufneigh:
        if HammingDistance(pattern[1:],x) < d:
            for y in ['A', 'C', 'G', 'T']:
                neighborhood.append(y + x)
        else:
            neighborhood.append(pattern[0] + x)
            
    return neighborhood

def FrequentWordsWithMismatches (file):
    inputs = readFile(file)
    genome = inputs[0]
    k = inputs[1]
    d= inputs[2]
    Patterns = []
    FreqMap = {}

    for i in range (0,(len(genome))):
        pattern = genome[i: (i+k)]
        if len(pattern) != k:
            continue
        Neighborhood = Neighbors(pattern, d)
        for neighbor in Neighborhood:
            if neighbor in FreqMap:
                FreqMap[neighbor] += 1 
            else:
                FreqMap[neighbor] = 1
    print(FreqMap)
    all_values = FreqMap.values()
    m = max(all_values)
    print(m)
    for  pattern in FreqMap.keys():
        if FreqMap[pattern] == m:
            Patterns.append(pattern)
    return Patterns 
                
#print(FrequentWordsWithMismatches('dataset_609067_9.txt'))
print(FrequentWordsWithMismatches('../FrequentWordsMismatches/inputs/input_1.txt'))
