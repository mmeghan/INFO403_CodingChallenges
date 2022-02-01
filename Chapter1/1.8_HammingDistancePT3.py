def readFile(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        pattern = lines[0].strip()
        genome = lines[1].strip()
        d = int(lines[2].strip())
    return (pattern, genome, d)

def HammingDistance (substring, pattern):
    mismatches = 0
    for i in range (0, len(substring)):
        if substring[i] != pattern[i]:
            mismatches += 1
    return mismatches

def ApproximatePatternCount(file):
    inputs = readFile(file)
    pattern = inputs[0]
    genome = inputs[1]
    d = inputs[2]
    n = len(pattern)
    count = 0
    for i in range(0, (len(genome))):
        substring = genome[i: (i+n)]
        if len(substring) != n:
            continue
        if HammingDistance(substring, pattern) <= d:
            print(substring)
            count += 1 
    return count 

#print (ApproximatePatternCount('./ApproximatePatternCount/input/input_2.txt'))
print(ApproximatePatternCount('dataset_609067_6.txt'))