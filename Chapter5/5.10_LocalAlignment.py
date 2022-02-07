'''
Goal -  Solve the Local Alignment Problem
inputs - two protein strings in the single-letter amino acid alphabet.
outputs - The maximum score of a local alignment of the strings, followed 
by a local alignment of these strings achieving the maximum score. 
Use the PAM250 scoring matrix for matches and mismatches as well as the indel penalty σ = 5.

'''
import numpy as np

def LocalAlignment (string1, string2, pam250, matrix):
    m = np.zeros((len(string2) + 1, len(string1) + 1))
    for i in range(len(string1)):
        m[0][i+1] = m[0][i] - 5
    for i in range(len(string2)):
        m[i+1][0] = m[i][0] - 5
    for i in range(len(string2)):
        for j in range(len(string1)):
            m[i+1][j+1] = max(0, m[i][j+1] - 5, m[i+1][j] - 5,
                                      m[i][j] + pam250[matrix.index(string2[i])][matrix.index(string1[j])])
    score = 0
    for k in range(len(string2) + 1):
        for t in range(len(string1) + 1):
            if score < m[k][t]:
                score = m[k][t]
                i = k - 1
                j = t - 1
    x = []
    y = []

    while i != -1 or j != -1:
        max_ = m[i+1][j+1] - pam250[matrix.index(string2[i])][matrix.index(string1[j])]
        if max_ == m[i][j]:
            x = [string1[j]] + x
            y = [string2[i]] + y
            i -= 1
            j -= 1
        else:
            max_ = max(m[i+1][j], m[i][j+1])
            if max_ == m[i+1][j]:
                x = [string1[j]] + x
                y = ['-'] + y
                j -= 1
            else:
                x = ['-'] + x
                y = [string2[i]] + y
                i -= 1
        if max_ == 0:
            break
    print(int(score))
    print(''.join(x))
    print(''.join(y))
    
    return score, x, y



with open('./datasets/dataset_609146_10.txt', 'r') as f:
    string1 = f.readline().rstrip()
    string2 = f.readline().rstrip()


with open('PAM250.txt', 'r') as file:
        matrix = file.readline().rstrip().split()
        pam250 = []
        for x in range(len(matrix)):
            line = file.readline().rstrip().split()
            pam250.append([int(line[i]) for i in range(1, len(line))])
LocalAlignment(string1, string2, pam250, matrix)

