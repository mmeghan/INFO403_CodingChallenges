'''
Goal: Peptide Encoding Problem - find substringd of a genome encoding given amino acid sequence
Input: A DNA string, an amino acid string peptide and the array GeneticCode
Output: all substrings of text encoding Peptide (if any such substrings exist)

*Note: the solution may contain repeated strings, if the same string occurs more than once as a substring of Text and encodes Peptide.
'''
codonTable= {}
def ReadFile():
    with open('./datasets/dataset_609118_7.txt', 'r') as file:
        DNA = file.readline().strip()
        Peptide = file.readline().strip()

    with open('RNA_codon_table_1.txt', 'r') as file:
        for line in file.readlines():
            items = line.strip().split()
            if len(items) == 2:
                codonTable[items[0]] = items[1]
            else:
                codonTable[items[0]] = 'STOP'
    return DNA, Peptide, codonTable

def kmer(text,i,k):
    return text[i:(i+k)]

def Lwindows(text,L):
    windows=list()
    for i in range(0,len(text)-L+1):
        windows.append(kmer(text,i,L))
    return windows

def DnaToRna(dna):
    rna=[]
    for i in range(0,len(dna)):
        if dna[i]=="T":
            rna.append("U")
        else:
            rna.append(dna[i])
    return "".join(rna)

def RnaToDna(rna):
    dna=[]
    for i in range(0,len(rna)):
        if rna[i]=="U":
            dna.append("T")
        else:
            dna.append(rna[i])
    return "".join(dna)

def reverse_complement(text):
    reverse=""
    for i in range(0,len(text)):
        if text[i]=="A":
            reverse+="U"
        if text[i]=="U":
            reverse+="A"
        if text[i]=="C":
            reverse+="G"
        if text[i]=="G":
            reverse+="C"
    return reverse[::-1]

def translation(rna):
    G= codonTable
    result=[]
    for i in range(0,len(rna),3):
        letter=G[rna[i:(i+3)]]
        if letter=="*":
            break
        result.append(letter)
    return "".join(result)

def PeptideEncoding(dna,peptide):
    result=[]
    p=len(peptide)
    rna=DnaToRna(dna)
    for substring in Lwindows(rna,3*p):
        if translation(substring)==peptide:
            result.append(RnaToDna(substring))
    for substring in Lwindows(rna,3*p):
        if translation(reverse_complement(substring))==peptide:
            result.append(RnaToDna(substring))
    return result
    
DNA, Peptide, codonTable  = ReadFile()
result=PeptideEncoding(DNA,Peptide)
for i in range(0,len(result)):
    print(result[i])


