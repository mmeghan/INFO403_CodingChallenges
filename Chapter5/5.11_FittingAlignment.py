'''
Goal - Solve the Fitting Alignment Problem
input - two nucleotide strings v and w, where v has length at most 1000 and w has length at most 100
output - A highest-scoring fitting alignment between v and w. Use the simple scoring method in which 
         matches count +1 and both the mismatch and indel penalties are 1.

'''
def ReadFile():
    with open('./datasets/dataset_609147_5.txt') as f:
        string1 = f.readline().strip()
        string2 = f.readline().strip()

    return (string1, string2)

def indelInserted(string, i):
    return string[:i] + '-' + string[i:]

def FittingAlignment(string1, string2):
    #find a substring sub of string1 that maximizes the global alignment score between 
    # sub and string2 among all substrings of string1
    #match = +1
    #mismatches/indels = -1
    m = len(string1)
    n = len(string2)

    scoreMatrix = [[0 for i in range(n+1)] for j in range(m+1)]
    backtrack = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
                    #mismatch                 #mismatch                 #match 
            score = [scoreMatrix[i-1][j]-1, scoreMatrix[i][j-1] -1, scoreMatrix[i-1][j-1] + [-1,1][string1[i-1]==string2[j-1]]]
            #find change that increases the similarity 
            scoreMatrix[i][j] = max(score)
            #get the loaction of that score and put in backtrack 
            backtrack[i][j] = score.index(scoreMatrix[i][j])
    
    #enumerate() method adds a counter to an iterable and returns it in a form of enumerating object. 
    #This enumerating obkject can then be used directly for loops or convered into a list 
    #lambda is a small anonymous function that cna take any number of arguments but can only have one expression

    #find the max value from the list of scores from the scoring matrix or the key and then add the first elemnet and n 
                        #index                                    #item
    i = max(enumerate([scoreMatrix[k][j] for k in range(n,m)]), key = lambda x: x[1]) [0] + n
    j = n
    align1 = string1[:i]
    align2 =string2[:j]

    max_score = scoreMatrix[i][j]

    #create the adjusted strings 
    while (i*j != 0): #so while either i or j is not 0
        if backtrack[i][j] == 0:
            i -=1
            align2 = indelInserted(align2, j)
        elif backtrack[i][j] == 1:
            j -= 1
            align1 = indelInserted(align1, i)
        else:
            i -=1 
            j -= 1
    align1 = align1[i:]
    return max_score, align1, align2


#string1 = 'GTAGGCTTAAGGTTA'
#string2 = 'TAGATA'
inputs = ReadFile()
string1 = str(inputs[0])
string2 = str(inputs[1])
max_score , align1, align2 = FittingAlignment(string1,string2)
print(max_score)
print(align1)
print(align2)