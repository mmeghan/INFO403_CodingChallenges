'''
Goal: Construct the suffix array of a string.
Input: A string Text 
Output: SuffixArray(Text), as a space-separated collection of integers.

./testcases/SuffixArray_Sample.txt
'''
from numpy import arange, empty_like


def ReadFile():
    with open('./datasets/dataset_609220_2.txt' , 'r') as f:
        Text = f.readline().strip()
    return Text 

def SuffixArray(s,auxiliary=False,padLCP=False):
    r = [i for (_,i) in sorted([(s[i:],i) for i in range(len(s))],
                               key=lambda x:x[0])]
    if auxiliary:
        n    = len(s)
        p    = empty_like(r)
        p[r] = arange(len(p), dtype=p.dtype)   # https://stackoverflow.com/questions/9185768/inverting-permutations-in-python
        LCP  = []
        for i in range(len(r)-1):
            i0     = r[i]
            i1     = r[i+1]
            LCP.append(0)
            for j in range(n-max(i0,i1)):
                if s[i0+j] == s[i1+j]:
                    LCP[-1] += 1
                else:
                    break
        if padLCP:
            LCP.insert(0,0)
        return (r,p,LCP)
    else:
        return r

Text = ReadFile()
Result = SuffixArray(Text)
with open('./solutions/SuffixArray_Solution.txt' , 'w') as solution:
    line = ' '.join(str(i) for i in Result)
    solution.write(f'{line}\n')