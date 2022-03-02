# In class chapter 6 examples 
# further represent the beginning and end of permutation P by adding 0 to the left of the first element 
# and n + 1 to the right of the last element

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


def FindBreakPoints(P):
    breakpoints = 0 
    n = len(P)
    P = [0] + P = [n+1]



P = ReadFile()

