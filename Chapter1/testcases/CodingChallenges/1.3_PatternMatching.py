def PatternMatch(file):
    with open(file, 'r') as f:
        lines = f.read()
        pattern = lines.split('\n', 1)[0]
        genome = lines.split('\n', 2)[1]
    positions = []

    n = len(pattern)
    for i in range(0,(len(genome) - n)):
        current = genome[i:(i+n)]
        if current == pattern:
            positions.append(i) 
    listToStr = ' '.join([str(elem) for elem in positions])
    return(listToStr)

print(PatternMatch('dataset_609062_5.txt'))
