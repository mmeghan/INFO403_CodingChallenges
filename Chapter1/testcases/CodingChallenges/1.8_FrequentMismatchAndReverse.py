#input - a DNA string text as well as integers k and d
#output- all k-mers Pattern maximizing the sum Countd(Text, Pattern) + Countd(Text,Pattennrc) over all possible k-mers

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

def ReversePattern(pattern):
    reverseComp = ""
    i = (len(pattern)-1)
    while i >= 0:
        if pattern[i] == "A":
            reverseComp+= "T"
        elif pattern[i] =="T":
            reverseComp+= "A"
        elif pattern[i] == "C":
            reverseComp+= "G"
        elif pattern[i] == "G":
            reverseComp+= "C"
        i = i-1
    return(reverseComp)

def Neighbors(pattern, d):
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return ['A', 'C', 'G', 'T']
    neighborhood = []
    suffixneigh = Neighbors(pattern[1:],d)
    for x in suffixneigh:
        if HammingDistance(pattern[1:],x) < d:
            for y in ['A', 'C', 'G', 'T']:
                neighborhood.append(y + x)
        else:
            neighborhood.append(pattern[0] + x)
            
    return neighborhood

def FrequentPattern(file):
    inputs = readFile(file)
    genome = inputs[0]
    k = inputs[1]
    d= inputs[2]
    Patterns = set()
    FreqMap = {}

    for i in range (0, (len(genome))):
        pattern = genome[i: (i+k)]
        if len(pattern) != k:
            continue
        Neighborhood = Neighbors(pattern, d)
        for neighbor in Neighborhood:
            if neighbor in FreqMap:
                FreqMap[neighbor] += 1 
            else:
                FreqMap[neighbor] = 1
    
    reverse_genome = ReversePattern(genome)
    print(genome)
    print(reverse_genome)
    for i in range (0, len(reverse_genome)):
        pattern = reverse_genome[i:(i+k)]
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
            Patterns.add(pattern)
    return Patterns 

print(FrequentPattern('../dataset_609067_10.txt'))