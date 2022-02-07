'''
Goal- use OutoutLCS to solve the Longest Common Substring Problem
input - two strings s and t
output - the longest common subsequence of s and t 

dataset_609144_5
./testcases/03_LongestCommonSubsequence/inputs/test1.txt
'''
import sys
sys.setrecursionlimit(5000)

def ReadFile():
    with open('./datasets/dataset_609144_5.txt', 'r') as f:
        data = f.readlines()
        s = data[0].strip()
        t = data[1].strip()
    return (s,t)

def LCSbacktrack(s,t):
    Backtrack = []
    result = []
    for i in range(len(s)+1):
        result.append([0])
    for j in range(len(t)+1):
        result[0].append(0)
    for i in range(0,len(s)):
        Backtrack.append([])

    for i in range (1, len(s)+1):
        for j in range(1, len(t)+1):
            match = 0
            if s[i-1] == t[j-1]:
                match += 1
                result[i].append(max([result[i-1][j],result[i][j-1],result[i-1][j-1]+match]))
            else:
                result[i].append(max([result[i-1][j], result[i][j-1], result[i-1][j-1]]))
            if result[i][j] == result[i-1][j]:
                Backtrack[i-1].append('D')
            elif result[i][j] == result[i][j-1]:
                Backtrack[i-1].append('R')
            elif result[i][j] == result[i-1][j-1] + match:
                Backtrack[i-1].append('Di')
    return Backtrack

def OutputLCS (Backtrack,s, i, j, final):
    if i == -1 or j == -1:
        print(final[::-1])
        return 
    if Backtrack[i][j] == 'D':
        return OutputLCS(Backtrack, s, i-1, j, final)
    elif Backtrack[i][j] == 'R':
        return OutputLCS(Backtrack, s, i, j-1, final)
    else:
        final = final + s[i]
        return OutputLCS(Backtrack, s, i-1, j-1, final)



inputs = ReadFile()
s = inputs[0]
t = inputs[1]
i = len(s)-1
j = len(t)-1
final = ''
Backtrack = LCSbacktrack(s,t)
print(Backtrack)
print(OutputLCS(Backtrack, s, i, j, final))
