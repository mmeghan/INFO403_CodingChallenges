'''
Goal: Find the number of breakpoints in a permutatino 
Input: A permutation
Output: The number of breakpoints in the permutation

breakpoint =  pair of consecutive elements that are “out of order” (or not consecuative neighbors)
adjecenty = pairs in which the second element is equal to the first element plus 1. (everything else is a breakpoint)


 further represent the beginning and end of permutation P by adding 0 to the left of the first element and 
 n + 1 to the right of the last element

 
./testcases/BreakPoints/sample.txt
./testcases/Breakpoints/NumberOfBreakpoints.txt


Answer for NumberofBreakpoints.txt: 178

'''
def ReadFile():
    with open('./datasets/dataset_609161_6.txt', 'r') as f:
        txt = f.readlines()
    txt = [x.strip() for x in txt]
    txt = txt[0].split(' ')
    P = []
    for i in range(len(txt)):
        if txt[i][0] == '-':
            P.append(-int(txt[i][1:]))
        else:
            P.append(int(txt[i][1:]))
    return P

def FindBreakpoints(P):
    breakpoints = 0
    n = len(P)
    P.insert(0, 0)
    P.insert(n+1, n+1)
    #print(P)
    for i in range(len(P)-1):
        if P[i] == P[i+1] -1:
            continue
        else:
            #print(P[i], P[i+1])
            breakpoints += 1
    return breakpoints


P = ReadFile()
#print(P)
#print(len(P))
breakpoint = FindBreakpoints(P)
print(breakpoint)