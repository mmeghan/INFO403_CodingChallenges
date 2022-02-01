#input- Integers k and d followed by a space separated collection of strings
#output- All (k,d)-motifs in Dna

def ReadFile(file):
    with open(file, 'r') as f:
        data = f.readlines()
        nums = data[0].strip()
        dnas = data[1].strip()
        dna = dnas.split(' ')
        parameters = nums.split(' ',1)
        k = int(parameters[0])
        d= int(parameters[1])
    return(dna, k, d)

def HammingDistance(substring, pattern):
    mismatches = 0
    for i in range (0, len(substring)):
        if substring[i] != pattern[i]:
            mismatches += 1
    return mismatches
'''
def Neighbor(pattern, d):
    if d ==0:
        return[pattern]
    if len(pattern) == 1:
        return ['A', 'C', 'G', 'T']
    neighborhood = []
    suffix_neighbor =  Neighbor(pattern[1:],d)
    for x in suffix_neighbor:
        if HammingDistance(pattern[1:],x) < d:
            for y in ['A', 'C', 'G', 'T']:
              neighborhood.append(y + x)
        else:
            neighborhood.append(pattern[0] + x)
        return neighborhood

'''
def neighbour(pattern, mismatch, kmerspattern ):
    if mismatch == 0:
        kmerspattern.add(pattern)
    else:
        bases = ['A', 'T', 'C', 'G']
        for i in range(len(pattern)):
            for j in range(len(bases)):
                new_pattern = pattern[:i] + bases[j] + pattern[i+1:]
                if mismatch <= 1:
                    kmerspattern.add(new_pattern)
                else:
                    neighbour(new_pattern, mismatch-1, kmerspattern)

def MotifEnumeration(file):
    inputs = ReadFile(file) 
    dna = inputs[0]
    print(dna)
    k = inputs[1]
    print(k)
    d=inputs[2]
    print(d)

    patterns = []
    for string in dna:
        #a non-repeating list of patterns per string of dna
        pattern = set()
        for i in range((len(string)) - k + 1):
            #non repeating list of neighborhoods of patterns in that string on dna
            kmerspattern = set()
            neighbour(string[i:i + k], d, kmerspattern)
            #adding all the kmers to a non-repeating list 
            for words in kmerspattern:
                pattern.add(words)
        #adding all the patterns per each string into one big list
        for j in pattern:
            patterns.append(j)
    motifpattern = []
    for element in patterns:
        #if there are as many patters in each of the strings of DNA means that it is found in every string 
        if patterns.count(element) == len(dna):
            motifpattern.append(element)
    #get rid of duplicates 
    motifpattern = list(set(motifpattern))
    return motifpattern


#print(MotifEnumeration('dataset_609078_8.txt'))
print(MotifEnumeration('./MotifEnumeration/inputs/input_1.txt'))