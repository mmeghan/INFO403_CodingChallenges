'''
Code Challenge: Solve the k-Universal Circular String Problem.

Input: An integer k.
Output: A k-universal circular string.
'''
def kUniversal(n):
	text = ''
	kmers = []
	for i in range (2**n):
		kmer = format(i,'b')
		if len(kmer) < n:
			diff = n - len(kmer)
			kmer = ('0' *diff) + kmer
		kmers.append(kmer)

	dB = deBruijn(kmers)
	path = EulerianPath(dB)
	edges = []
	for i in range (len(path)-1):
		edge = path[i] + path[i+1][-1:]
		edges.append(edge)
	text = GenomePath(edges)
	text = text[:-(k-1)]
	return text