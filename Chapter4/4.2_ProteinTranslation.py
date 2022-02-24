'''
Goal: Protein Translation Problem-  translate an RNA string into an amino acid string 
Input: An RNA String pattern and the array GeneticCode
Output: the translation of Pattern into an animo acid string peptide

*Note: the stop codon should not be translates
'''
from attr import dataclass


def ReadFile():
    with open('./datasets/dataset_609118_4.txt','r') as f:
        data = f.readline()
        RNA = data.strip()

    codonTable = {}
    with open('RNA_codon_table_1.txt', 'r') as file:
        for line in file.readlines():
            items = line.strip().split()
            if len(items) == 2:
                codonTable[items[0]] = items[1]
            else:
                codonTable[items[0]] = 'STOP'

    return (RNA, codonTable)

def ProteinTranslation(string, codonTable):
    ProteinString = ''
    for i in range(0,len(string),3):
        codon = string[i:i+3]
        print(codon)
        protein = codonTable[codon]
        if protein == 'STOP':
            return ProteinString
        else:
            ProteinString += protein
        
    return ProteinString

inputs = ReadFile()
RNA = inputs[0]
codonTable = inputs[1]

print(ProteinTranslation(RNA, codonTable))