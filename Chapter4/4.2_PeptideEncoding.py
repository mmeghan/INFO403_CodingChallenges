'''
Goal: Peptide Encoding Problem - find substringd of a genome encoding given amino acid sequence
Input: A DNA string, an amino acid string peptide and the array GeneticCode
Output: all substrings of text encoding Peptide (if any such substrings exist)

*Note: the solution may contain repeated strings, if the same string occurs more than once as a substring of Text and encodes Peptide.
'''
codonTable= {}
def ReadFile():
    with open('./datasets/.txt', 'r') as file:
        DNA = file.readline().strip()
        Peptide = file.readline().strip()
    with open('RNA_codon_table_1.txt', 'r') as file:
        for line in file.readlines():
            items = line.strip().split()
            if len(items) == 2:
                codonTable[items[0]] = items[1]
            else:
                codonTable[items[0]] = 'STOP'
    return (DNA, Peptide, codonTable)

def ReverseCompliment(string):
    reverse = ''
    for i in reversed(range(len(string))):
        if i == 'A':
            reverse += 'T'
        elif i == 'T':
            reverse += 'A'
        elif i == 'C':
            reverse += 'G'
        else:
            reverse += 'C'
    return reverse

def PeptideEncoding (DNA, Peptide):
    forward_substrings = []
    for i in range(0,len(DNA), 3):
        codon = DNA[i:i+3]
        if codonTable[codon] in Peptide:
           n = len(forward_substrings)
           if codonTable[codon] == Peptide[n]:
               forward_substrings.append(codonTable[codon])
    reverse_substrings = []
    
    


