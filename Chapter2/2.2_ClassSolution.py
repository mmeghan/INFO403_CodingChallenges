
from distutils.command.install_lib import install_lib
from pickle import TRUE


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

def ApproximatePatternCount(genome, pattern, d):
    n = len(pattern)
    count = 0
    for i in range(0, (len(genome))):
        substring = genome[i: (i+n)]
        if HammingDistance(substring, pattern) <= d:
            count += 1 
    return count 

def neighbors(pattern, d):
        if d == 0:
          return [pattern]
        if len(pattern) == 1:
          return ['A', 'C', 'G', 'T']
        neighborhood = []
        sufneigh = neighbors(pattern[1:],d)
        for x in sufneigh:
          if HammingDistance(pattern[1:],x) < d:
            for y in ['A', 'C', 'G', 'T']:
              neighborhood.append(y + x)
          else:
            neighborhood.append(pattern[0] + x)
        return neighborhood


def MotifEnumeration(file):
    inputs = ReadFile(file) 
    dna = inputs[0]
    k = inputs[1]
    d=inputs[2]
    Patterns = []
    for string in dna:
        pattern = set()
        for i in range(0,len(string)-k+1):
            substring = string[i:i+k]
            neiborhood = neighbors(substring,d)
            for neighbor in neiborhood:
                inALL= TRUE
                for string in dna:
                    inString = False
                    for j in range(0,len(string)-k+1):
                        if HammingDistance(neighbor, string[j:j+k]) <= d:
                            inString = True
                        if not inString:
                            inALL = False
                    if inALL:
                       Patterns.append(neighbor)
    finalPattern = []
        
    Patterns = list(set(Patterns))
    return(Patterns)



print(MotifEnumeration('./MotifEnumeration/inputs/input_1.txt'))