#input - a sequence path of k-mers Pattern1,...,Patternn such that the last k-1 symbols of Patterni 
  #are equal to the first k-1 symbols of Patterni+1 for 1<= i <= n-1
#output - A string Text of length k+n-1 such that the ith k-mer in text is equal to Patterni (for 1<=i<=n)

from operator import ge
from os import remove


def ReadFile(file):
    strings = []
    with open(file, 'r') as f:
        data = f.readlines()
        for i in data:
            strings.append(i.strip())
    return (strings)



def StringReconstruction(file):
    strings = ReadFile(file)
    path = strings[0]
    for i in strings[1:]:
        path += i[len(i)-1]
    solution = open('StringReconstructionSolution.txt', 'w')
    solution.write(path)
    return(path)
    
    
#StringReconstruction('dataset_609096_3.txt')
StringReconstruction('ClassPRoblem6.txt')