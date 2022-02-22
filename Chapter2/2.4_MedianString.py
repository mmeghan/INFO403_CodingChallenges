def ReadFile(file):
    with open(file, 'r') as f:
        data = f.readlines()
        k = int(data[0].strip())
        dnas = data[1].strip()
        dna = dnas.split(' ')
    return (dna, k)

def hammingDistance(p, q):
	ham = 0
	for x, y in zip(p, q):
		if x != y:
			ham += 1
	return ham

def distanceBetweenPatternAndString(pattern, dna):
	k = len(pattern)
	distance = 0
	for x in dna:
		hamming = k+1
		for i in range(len(x) - k + 1):
			z = hammingDistance(pattern, x[i:i+k])
			if hamming > z:
				hamming = z
		distance += hamming
	return distance

def numberToPattern(x, k):
	if k == 1:
		return numberToSymbol(x)
	return numberToPattern(x // 4, k-1) + numberToSymbol(x % 4)

def numberToSymbol(x):
	if x == 0:
		return "A"
	if x == 1:
		return "C"
	if x == 2:
		return "G"
	if x == 3:
		return "T"

def medianString(file):
    inputs = ReadFile(file)
    dna = inputs[0]
    k = inputs[1]
    distance = (k+1) * len(dna)
    median = ""
	#for each k-mer Pattern from AA..AA to TT..TT
    for i in range(4**k):
        pattern = numberToPattern(i, k)
        z = distanceBetweenPatternAndString(pattern, dna)
        if distance > z:
            distance = z
            median = pattern
    return median


print(medianString('./datasets/dataset_609080_9.txt'))