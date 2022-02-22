import numpy as np
from ScoringMatrices import BLOSUM62

def ReadFile():
    with open ('./testcases/10_AffineGapPenalties/inputs/sample.txt', 'r') as f:
        data = f.readlines()
        str1 = data[0].strip()
        str2 = data[1].strip()

    return (str1, str2)

def GapAligment (str1, str2, blousm):
    n = len(str1)
    m = len(str2)
    sigma = 11
    epsilon = 1
    middle = np.zeros(shape = (n+1,m+1), dtype = np.float)
    upper = np.zeros(shape = (n+1,m+1), dtype = np.float)
    lower = np.zeros(shape = (n+1,m+1), dtype = np.float)
    for i in range(n+1):
        lower[i, 0] = -epsilon*i
        middle[i, 0] = -sigma*i
    for j in range(m+1):
        middle[0, j] = -sigma*j
        lower[0, j] = -epsilon*j
    # backtrack matrix has 3 level : level 0 is lower '|', level 1 is middle '\', level 2 is upper '-'
    # backtrack in level 0 is a vertical gap e.g insertion of '-' for W-alignement
    # backtrack in level 2 is an horizontal gap e.g insertion of '-' for V-alignement
    backtrack = np.chararray(shape = (n,m,3))
    for i in range(n):
        for j in range(m):
            keys = [str1[i], str2[j]]
            lower[i+1, j+1] = max(lower[i, j+1] - epsilon, middle[i, j+1] - sigma)
            upper[i+1, j+1] = max(upper[i+1, j] - epsilon, middle[i+1, j] - sigma)
            middle[i+1, j+1] = max(lower[i+1, j+1], upper[i+1, j+1],  middle[i, j] + blosum[(keys[0],keys[1])])
            
            if lower[i+1, j+1] == lower[i, j+1] - epsilon:
                # continuing vertical gap
                backtrack[i, j, 0] = '|'
            else:
                #opening vertical gap
                backtrack[i, j, 0] = '+'
    
            if upper[i+1, j+1] == lower[i+1, j] - epsilon:
                # continuing horizontal gap
                backtrack[i, j, 2] = '-'
            else:
                #opening vertical gap
                backtrack[i, j, 2] = '+'
                            
            if middle[i+1, j+1] == lower[i+1, j+1]:
                # vertical gap closing
                backtrack[i, j, 1] = '|'
            elif middle[i+1, j+1] == upper[i+1, j+1]:
                # horizontal gap closing
                backtrack[i, j, 1] = '-'
            elif middle[i+1, j+1] == middle[i, j] + blosum[(keys[0],keys[1])]:
                backtrack[i, j, 1] = '/' if str1[i] == str2[j] else '*'
    align1 = []
    align2 = []
    i=n
    j=m

    smax = middle[i,j]
    i -= 1
    j -= 1
    level = 1

    while (i*j != 0):
        if (level == 1):
            if backtrack[i, j, level] == '|':
                level = 0
            elif backtrack[i, j, level] == '-':
                level = 2
            else:
                align2.append(str2[j])
                align1.append(str1[i])
                i -=1
                j -=1
        elif (level == 0):
            # back tracking a vertical gap
            align2.append('-')
            align2.append(str1[i])
            if (backtrack[i, j, level] == '+'):
                # back tracking a gap opening
                level = 1
            i -=1
        elif (level == 2):
            # back tracking an horizontal gap
            align2.append(str2[j])
            align1.append('-')
            if (backtrack[i, j, level] == '+'):
                # back tracking a gap opening
                level = 1
            j -=1
    align1.reverse()
    align2.reverse()
    align1 = ''.join(align1)
    align2 = ''.join(align2)
    return (smax,align1,align2)

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
max_score, align1, align2 = GapAligment(str1, str2, blosum)
print(str(max_score))
print(align1)
print(align2)