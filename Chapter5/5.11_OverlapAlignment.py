'''
Goal- Solve the overlap alignment problem
input - two strings v and w each with a length of at most 1000
Output: The score of an optimal overlap alignment of v and w, followed by an 
         alignment of a suffix v' of v and a prefix w' of w achieving this maximum 
         score. 
- Matches +=1 
- Mismatches/indels -=2 

'''

def ReadFile():
    with open('./datasets/dataset_609147_7.txt') as f:
        string1 = f.readline().strip()
        string2 = f.readline().strip()

    return (string1, string2)

def indelInserted(string, i):
    return string[:i] + '-' + string[i:]

def OverlapAlignment(string1, string2):
    m = len(string1)
    n = len(string2)

    scoreMatrix = [[0 for i in range(n+1)] for j in range(m+1)]
    backtrack = [[0 for i in range(n+1)] for j in range(m+1)]


    max_score = -2*(m+n)
    max_i = 0
    max_j = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
                    #mismatch                 #mismatch                 #match 
            score = [scoreMatrix[i-1][j]-2, scoreMatrix[i][j-1] -2, scoreMatrix[i-1][j-1] + [-1,1][string1[i-1]==string2[j-1]]]
            #find change that increases the similarity 
            scoreMatrix[i][j] = max(score)
            #get the loaction of that score and put in backtrack 
            backtrack[i][j] = score.index(scoreMatrix[i][j])

            if i == m or j == n:
                if scoreMatrix[i][j] > max_score:
                    max_score = scoreMatrix[i][j]
                    max_i = i
                    max_j = j
    a = max_i
    b = max_j
    align1 = string1[:a]
    align2 =string2[:b]

    while(a*b != 0): 
        if backtrack[a][b] == 0:
            align2 = indelInserted(align2, b)
            a = a-1
        elif backtrack[a][b] == 1:
            align1 = indelInserted(align1, a)
            b = b-1
        else:
            a = a-1
            b = b-1
            
    align1 =  align1[a:]
    align2 =  align2[b:]
    
    return max_score, align1, align2

    

inputs = ReadFile()
#string1 = str(inputs[0])
#string2 = str(inputs[1])
string1 = 'PAWHEAE'
string2 = 'HEAGAWGHEE'
max_score , align1, align2 = OverlapAlignment(string1,string2)
print(max_score)
print(align1)
print(align2)