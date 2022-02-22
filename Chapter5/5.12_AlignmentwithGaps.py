'''
Goal-  Solve the Alignment with Affine Gap Penalties Problem
input - Two amino acid strings v and w (each of length at most 100)
output - the maximum alignment score between v and w followed by an alignment of v and w
         achiving this maximum score. Use BLOSUM62 scoring matrix, a gap opening penalty of 11
         and gap extension penalty of 1

./datasets/dataset_609148_8.txt
testcases/10_AffineGapPenalties/inputs/sample
'''
from ScoringMatrices import BLOSUM62
import math 

def ReadFile():
    with open ('./testcases/10_AffineGapPenalties/inputs/sample.txt', 'r') as f:
        data = f.readlines()
        str1 = data[0].strip()
        str2 = data[1].strip()

    return (str1, str2)

def indelInsert(string, i):
    return string[:i] + '-' + string[i:]


def AffineGap(str1, str2, blosum):
    m = len(str1)
    n = len(str2)
    gap_open = 11
    gap_extension = 1

    s = [[[0 for i in range(n+1)] for j in range(m+1)] for k in range(3)]
    backtrack = [[[0 for i in range(n+1)] for j in range(m+1)] for k in range(3)]
    
    for i in range(m+1):
        s[0][i][0] = float('-inf') if i ==0 else -gap_open-(gap_extension*i-1) #lower
        s[1][i][0] = 0 if i == 0 else -gap_open-(gap_extension*i-1) #middle
        s[2][i][0] = 0 if i ==0 else float('-inf') #upper
    for j in range(n+1):
        s[0][0][j] = float('-inf') if i ==0 else -gap_open-(gap_extension*i-1) #lower
        s[1][0][j] = 0 if i == 0 else -gap_open - (gap_extension*j-1) #middle
        s[0][0][j] = float('-inf') if i ==0 else -gap_open - (gap_extension*j-1) #upper

    print('lower:', s[0])
    print('---------')
    print('middle:', s[1])
    print('--------')
    print('upper:', s[2])
    for i in range (1,m+1):
        for j in range(1, n+1):
                        # lower + extension pentalty     #middle + opening pentaly
            s_lower = [s[0][i-1][j] -gap_extension, s[1][i-1][j] -gap_open]
            s[0][i][j] = max(s_lower)
            backtrack[0][i][j] = s_lower.index(s[0][i][j])

                       #upper + gap extension         #middle + gap open
            s_upper = [s[2][i][j-1]-gap_extension, s[1][i][j-1]-gap_open]
            s[2][i][j] = max(s_upper)
            backtrack[2][i][j] = s_upper.index(s[2][i][j])

            keys = [str1[i-1], str2[j-1]]
                        #lower     #middle + match score                            #upper      
            s_middle = [s[0][i][j], s[1][i-1][j-1] + blosum[(keys[0],keys[1])], s[2][i][j]]
            s[1][i][j] = max(s_middle)
            backtrack[1][i][j] = s_middle.index(s[2][i][j])


    align1 = str1
    align2 = str2
    i = m
    j = n

    final_scores = [s[0][i][j], s[1][i][j], s[2][i][j]]
    print('final scores:', final_scores)
    max_score = max(final_scores)
    backtrack_score= final_scores.index(max_score)
    

    while (i*j != 0):
        #start on lower matrix 
        if backtrack_score == 0:
            #if best move is move to middle set to work on middle matrix 
            #and shift second string over 1 and add '-'
            if backtrack[0][i][j] == 1:
                backtrack_score = 1
            align2 = indelInsert(align2, j)
            i = i -1
        #else we are on the middle matrix     
        elif backtrack_score == 1:
            #if the best move is to move to lower matrix, move down 
            if backtrack[1][i][j] == 0:
                backtrack_score = 0
            #else if the best move is to the upper matrix, then move up 
            elif backtrack[1][i][j] == 2:
                backtrack_score = 2
            else:
                #if the best move is to stay on the middle matrix decrese i and j
                i = i-1
                j = j-1
        #we are on the upper matrix
        else:
            
            #if the best move is to move to middle matrix, move there
            #and shift first string over one and insert '-' and decrease j by one 
            if backtrack[2][i][j] == 1:
                backtrack_score=1
            align1 = indelInsert(align1, i)
            j = j-1
    
    for k in range(i):
        align2 = indelInsert(align2, 0)
    for k in range(j):
        align1 = indelInsert(align1, 0)
    
    return max_score, align1, align2
'''
inputs = ReadFile()
str1= inputs[0]
print(str1)
str2 = inputs[1]
print(str2)
'''
str1 = 'PRTEINS'
str2 = 'PRTWPSEIN'
blosum = BLOSUM62()


max_score, align1, align2 = AffineGap(str1, str2, blosum)
print(str(max_score))
print(align1)
print(align2)
