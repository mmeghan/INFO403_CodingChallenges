'''
Goal: Solve the Multiple Longest Common Subsequence Problem 
input- three DNA strings of length at most 10
output - the length of the longest common subsequence of these three strings, followed by a multiple
         alignment of the three strings corresponding to such an alignment 

the score of a column of the alignment matrix is equal to 1 if all the column's symbols are identical
and 0 if even one symbol disagrees

./testcases/13_MultipleAlignment/inputs/sample.txt

'''

def ReadFile():
    with open ('./datasets/dataset_609150_5.txt', 'r') as f:
        data = f.readlines()
        str1 = data[0].strip()
        str2 = data[1].strip()
        str3 = data[2].strip()

    return (str1, str2, str3)

def indelInsertion(string, i):
    return string[:i] + '-' + string[i:]

def MultipleAlignments(str1, str2, str3):
    m = len(str1)
    n = len(str2)
    p = len(str3)
    s =[[[0 for k in range(p+1)] for j in range (n+1)] for i in range(m+1)]
    backtrack = [[[0 for k in range(p+1)] for j in range (n+1)] for i in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            for k in range(1, p+1):
                if str1[i-1] == str2[j-1] == str3[k-1]:
                    s[i][j][k]=max(s[i - 1][j - 1][k - 1] + 1, s[i - 1][j][k], s[i][j - 1][k], s[i][j][k - 1], s[i - 1][j - 1][k], s[i - 1][j][k - 1], s[i][j - 1][k - 1])
                    if s[i][j][k]==s[i - 1][j][k]:
                        backtrack[i][j][k] = 1
                    elif s[i][j][k]==s[i][j - 1][k]:
                        backtrack[i][j][k] = 2
                    elif s[i][j][k]==s[i][j][k - 1]:
                        backtrack[i][j][k] = 3
                    elif s[i][j][k]==s[i - 1][j-1][k]:
                        backtrack[i][j][k] = 4
                    elif s[i][j][k]==s[i-1][j][k - 1]:
                        backtrack[i][j][k] = 5
                    elif s[i][j][k]==s[i][j - 1][k - 1]:
                        backtrack[i][j][k] = 6        
                else:
                    s[i][j][k] = max(s[i - 1][j - 1][k - 1], s[i - 1][j][k], s[i][j - 1][k], s[i][j][k - 1], s[i - 1][j - 1][k], s[i - 1][j][k - 1], s[i][j - 1][k - 1])
                    if s[i][j][k]==s[i - 1][j][k]:
                        backtrack[i][j][k] = 1
                    elif s[i][j][k]==s[i][j - 1][k]:
                        backtrack[i][j][k] = 2
                    elif s[i][j][k]==s[i][j][k - 1]:
                        backtrack[i][j][k] = 3
                    elif s[i][j][k]==s[i - 1][j-1][k]:
                        backtrack[i][j][k] = 4
                    elif s[i][j][k]==s[i-1][j][k - 1]:
                        backtrack[i][j][k] = 5
                    elif s[i][j][k]==s[i][j - 1][k - 1]:
                        backtrack[i][j][k] = 6   
    correctedSTR1 = str1
    correctedSTR2 = str2
    correctedSTR3 = str3
    correctedSTR1, correctedSTR2, correctedSTR3 = AlignReconstruction(backtrack, correctedSTR1, correctedSTR2, correctedSTR3 )

    return str(s[m][n][p]), correctedSTR1, correctedSTR2, correctedSTR3

def AlignReconstruction (backtrack, string1, string2, string3):
    i,j,k = len(backtrack)-1, len(backtrack[0])-1, len(backtrack[0][0])-1
    while(i*j*k != 0):
        if backtrack[i][j][k] == 1:
            i -= 1
            string2 = indelInsertion(string2, j)
            string3 = indelInsertion(string3,k)
        elif backtrack[i][j][k] == 2:
            j -= 1
            string1 = indelInsertion(string1, i)
            string3 = indelInsertion(string3,k)
        elif backtrack[i][j][k] == 3:
            k -= 1
            string1 = indelInsertion(string1, i)
            string2 = indelInsertion(string2, j)
        elif backtrack[i][j][k] == 4:
            i-= 1
            j-=1
            string3 = indelInsertion(string3,k)
        elif backtrack[i][j][k] == 5:
            i -=1
            k -=1
            string2 = indelInsertion(string2,j)
        elif backtrack[i][j][k] == 6:
            j -= 1
            k -= 1
            string1 = indelInsertion(string1, i)
        else:
            i -= 1
            j -= 1
            k -= 1
    while len(string1) != max(len(string1), len(string2), len(string3)):
        string1 = '-' + string1
    while len(string2) != max(len(string1), len(string2), len(string3)):
        string2 = '-' + string2
    while len(string3) != max(len(string1), len(string2), len(string3)):
        string3 = '-' + string3
    return string1, string2, string3
   
inputs = ReadFile()
str1 = inputs[0]
str2 = inputs[1]
str3 = inputs[2]
for result in MultipleAlignments(str1, str2, str3):
    print(result)