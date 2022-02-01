#Input: strings pattern and tezt along with an integer d 
#Output: all starting positions where pattern appears as a substring of Text with at most d mismatches
#Goal: Find all approximate occurences of a pattern in a text 


def readFile(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        pattern = lines[0].strip()
        genome = lines[1].strip()
        d = int(lines[2].strip())
    return (pattern, genome, d)

def MisMatches (substring, pattern, d):
    if len(substring) != len(pattern):
        result = False
        return result
    mismatches = 0
    for i in range(0,len(substring)):
        if substring[i] != pattern[i]:
            mismatches += 1
    if mismatches > d:
        result =  False
    elif mismatches <= d:
        result = True
        #print(substring)
    return (result)

def HammingDistance (file):
    inputs = readFile(file)
    #print(inputs)
    pattern = inputs[0]
    genome = inputs[1]
    d = inputs[2]
    n = len(pattern)
    match_starts = " "
    ##print("missing one")
    ##print(genome[137:(137+n)])
    ##print(len(genome))
    ##print('\n')
    for i in range(0,(len(genome))):
        match = MisMatches(genome[i:(i+n)], pattern, d)
        if match == True:
            match_starts += str(i) + ' '

    print(match_starts)
    print('\n')
    print(len(match_starts))



HammingDistance('dataset_609067_6.txt')
#HammingDistance('./ApproximatePatternMatching/inputs/input_4.txt')