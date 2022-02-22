'''
Second Attempt at Median String to get a better grasp of problem and make code more coherant 
Goal: Implement Median String 
Input: an integer k, followed by a space-separated collection of strings DNA
Output: A k-mer Pattern that minimizes d(Pattern,DNA) among all possible choices of k-mers 
        (If there are multiple such strings Pattern, can return any one of them)
'''
import math 

def ReadFile():
    with open ('./datasets/dataset_609080_9.txt', 'r') as f:
        data = f.readlines()
        k = int(data[0].strip())
        dnas = data[1].strip()
        dna = dnas.split(' ')
    return (dna, k)

def HammingDistance (substring, pattern):
    mismatches = 0
    if (len(pattern) == len(substring)):
        for i in range (len(substring)):
            if (substring[i] != pattern[i]):
                mismatches +=1
    else:
        mismatches = -1
    return mismatches

def MinHammingDistance (pattern, string):
    k = len(pattern)
    min_distance = len(string)
    for i in range (len(string)+1):
        if (HammingDistance(pattern, string[i:i+k]) < min_distance):
            min_distance = HammingDistance(pattern, string[i:i+k])
    return min_distance

def NumberToPattern(x, k):
	if k == 1:
		return NumberToSymbol(x)
	return NumberToPattern(x // 4, k-1) + NumberToSymbol(x % 4)

def NumberToSymbol(x):
	if x == 0:
		return "A"
	if x == 1:
		return "C"
	if x == 2:
		return "G"
	if x == 3:
		return "T"

def MedianString():
    inputs = ReadFile()
    dna = inputs[0]
    k = inputs[1]

    distance = math.inf
    median = ''
    pattern_list = []

    for i in range (4**k):
        kmer = NumberToPattern(i,k)
        pattern_list.append(kmer)
    
    for pattern in pattern_list:
        score = 0
        for sequence in dna:
            score += MinHammingDistance(pattern, sequence)
        if score < distance:
            distance = score
            median = pattern 
    return median 

print(MedianString())
