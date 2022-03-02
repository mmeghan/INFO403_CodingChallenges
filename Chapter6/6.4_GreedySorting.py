'''
Goal: Implement Greedy Sorting 
Input: A permutation P
Output: The sequence of permutations corresponding to apply GreedySorting to P, ending with the identity permutation 

./datasets/dataset_609160_4.txt

./testcases/GreedySorting/sample.txt

'''

def ReadFile():
    with open('./testcases/GreedySorting/classEx.txt', 'r') as f:
        P = f.readlines()
    P = [x.strip() for x in P]
    P = P[0].split(' ')
    P[0] = P[0].split('(')
    P[0] = P[0][-1]
    P[-1] = P[-1].split(')')
    P[-1] = P[-1][0]
    for i in range (len(P)):
        if P[i][0] == '-':
            P[i] = -int(P[i][1:])
        else:
            P[i] = int(P[i][1:])
    return P
    

def GreedySorting(P):
    permutations = []
    for i in range(len(P)):
        #if the value at position i does not equal iteration i plus 1
        if P[i] != i+1:
            print('P[i]:', P[i])
            # remove all the '+' and '-'
            Pd = [abs(x) for x in P[:]]
            print(Pd)
            index = Pd.index(abs(i+1))
            #create substring of P and reverse then multiply every number by -1
            substring = P[i:index+1]
            print(substring)
            substring.reverse()
            substring = [-1 * x for x in substring]
            print(substring)
 
            #add togther previous elements of P + current substring + everything in P after substring 
            Pa = P[0:i] + substring + P[index+1:]
            print(Pa)
            permutations.append(Pa)
            print('P:', P)

            #if the element P[i] equals the negative of iteration i + 1
            if Pa[i] == -(i+1):
                #Pb equals all of of Pa
                Pb = Pa[:]
                #multiply -1 by Pa[i]
                Pb[i] = -1 * Pa[i]
                #add this iteration to permutations 
                permutations.append(Pb)
                #set P to the most recent premutation 
                P = Pb[:]
            else: 
                #set P to the most recent premutation 
                P = Pa[:]
    for i in range(len(permutations)):
        for j in range(len(permutations[0])):
            if permutations[i][j] > 0:
                permutations[i][j] = '+' + str(permutations[i][j])
            else: permutations[i][j] = str(permutations[i][j])

    final = []
    for element in permutations:
        final.append(' '.join(element))
    return final     



P = ReadFile()
print('P:',P)
print('\n')
permutations = GreedySorting(P)
print('-------')
with open('./solutions/GreedySortingSolution.txt','w') as s:
    for per in permutations:
        s.write(per + '\n')
s.close()