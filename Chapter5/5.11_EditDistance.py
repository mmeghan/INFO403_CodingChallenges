'''
Goal - find the edit distance between two string
input - two strings 
output - the edit distance between these strings 

>idea is to fram each problem as an instance of the longest path in a DAG problem
>edit distance = the minimum number of edit operations needed to transform one string into another
>edit operations can be insertion, deletion or substitution of a single symbol

./testcases/07_EditDistance/inputs/test3.txt') as f:
'''

def ReadFile():
    with open('./datasets/dataset_609147_3.txt') as f:
        string1 = f.readline().strip()
        string2 = f.readline().strip()

    return (string1, string2)

def EditDistance(string1, string2):
    #process all character one by one for both strings
    #traverse from the end of the strings to determine if they match 
    #id the last character of two strings are the same, do nothing. Ignore last character and get count for remaining strings
    #recur for lengths string1-1 and string2-1
    #else if the last characters are not the same, consider all operations on string1, recursively compute minimum cost for all three operations 
        #insert: recur for len(string1) and len(string2)-1
        #remove: recur for len(string1)-1 and len(string2)
        #replace: recur for len(string1)-1 and len(string2)-1
    m = len(string1)
    n = len(string2)
    stringMatrix = [[0 for x in range(n+1)] for x in range(m+1)]

    #fill matrix from bottom up 
    for i in range(m+1):
        for j in range(n+1):
            #if the first string is empty only option is to insert all characters 
            if i ==0:
                stringMatrix[i][j] = j
            #if second string is empty only option is to remove all character
            elif j == 0:
                stringMatrix[i][j] = i
            #if last characters are same, ignore last character and recur for remaining string
            elif string1[i-1] == string2[j-1]:
                stringMatrix[i][j] = stringMatrix[i-1][j-1]
            #if last characters are different, consider all possiblities and find minimum 
            else:
                stringMatrix[i][j] = 1 + min(stringMatrix[i][j-1], stringMatrix[i-1][j], stringMatrix[i-1][j-1])

    return stringMatrix[m][n]

inputs = ReadFile()
string1 = str(inputs[0])
string2 = str(inputs[1])
print(EditDistance(string1, string2))