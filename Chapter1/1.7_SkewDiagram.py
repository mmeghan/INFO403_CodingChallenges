## input: genome string 
# output: the skew value for every postion in genome 

def Skew(genome):
    skews = []
    skew = 0 
    skews.append(skew)
    for i in range (0, len(genome)):
        if genome[i] == "C":
            skew -= 1
            print(skew, '\n')
        elif genome[i] == "G":
            skew += 1 
            print(skew, '\n')
        
        skews.append(skew)
    return (skews)

print(Skew('TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'))

