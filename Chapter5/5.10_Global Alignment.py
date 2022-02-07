'''
Goal- Find a highest-scoring alignment of two strings as defined by a scoring matrix
input - Two protein strings written in the single-letter amino acid alphabet.
output - The maximum alignment score of these strings followed by an alignment achieving 
         this maximum score. Use the BLOSUM62 scoring matrix for matches and mismatches as 
         well as the indel penalty σ = 5.
To solve the global alignmnet problem, i musht find a longest path in the alignment graph 
after updating the edge weights to reflect the values in the scoring matrix.
'''
import numpy as np

def GlobalAlignment (str1, str2, blosum, matrix):
    
    m = np.zeros((len(str2) + 1, len(str1) + 1))
    for i in range(len(str1)):
        m[0][i+1] = m[0][i] - 5
    for i in range(len(str2)):
        m[i+1][0] = m[i][0] - 5
    for i in range(len(str2)):
        for j in range(len(str1)):
            m[i+1][j+1] = max(m[i][j+1] - 5, m[i+1][j] - 5,
                                      m[i][j] + blosum[matrix.index(str2[i])][matrix.index(str1[j])])
    x = []
    y = []
    i = len(str2) - 1
    j = len(str1) - 1
    while i != -1 or j != -1:
        max_ = m[i+1][j+1] - blosum[matrix.index(str2[i])][matrix.index(str1[j])]
        if max_ == m[i][j]:
            x = [str1[j]] + x
            y = [str2[i]] + y
            i -= 1
            j -= 1
        else:
            max_ = max(m[i+1][j], m[i][j+1])
            if max_ == m[i+1][j]:
                x = [str1[j]] + x
                y = ['-'] + y
                j -= 1
            else:
                x = ['-'] + x
                y = [str2[i]] + y
                i -= 1

    print(int(m[-1][-1]))
    print(''.join(x))
    print(''.join(y))
    
    return m[-1][-1], x, y

if __name__ == "__main__":
    
    with open('BLOSUM62.txt', 'r') as file:
        matrix = file.readline().rstrip().split()
        blosum = []
        for x in range(len(matrix)):
            line = file.readline().rstrip().split()
            blosum.append([int(line[i]) for i in range(1, len(line))])
            
    with open('./datasets/dataset_609146_3.txt', 'r') as file:
        str1 = file.readline().rstrip()
        str2 = file.readline().rstrip()
    #str1 = 'PLEASANTLY'
    #str2 = 'MEANLY'
    GlobalAlignment(str1, str2, blosum, matrix)
