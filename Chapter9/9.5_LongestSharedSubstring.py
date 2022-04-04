'''
Goal: Find the Longest Substring shared by two strings 
Input: String1 and String 2
Output: The longest substring that occurs in both Text1 and Text2.
./testcases/LongestSharedSubstring_Sample.txt

'''
from numpy  import empty_like,arange,argmax

def ReadFile():
    with open('./datasets/dataset_609219_6.txt', 'r') as f:
        String1 = f.readline().strip()
        String2 = f.readline().strip()
    return String1 , String2

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

def LongestSharedSubstring(s,t):
    # find_straddling
    #
    # Find indices of LCPs that straddle end of s,
    # i.e. one string is from s, the other from t
    
    def find_straddling():
        previous_from_s = False
        Pairs           = []
        for i in range(len(lcp)):
            from_s          = r[i]<len(s)+2
            if i>0 and previous_from_s != from_s:
                Pairs.append(i)
            previous_from_s = from_s
        return Pairs
    
    text           = s + '$' + t + '#'
    r,_,lcp        = SuffixArray(text,auxiliary=True,padLCP=True)
    candidate_LCPs = [lcp[i] if i in  find_straddling() else 0 for i in range(len(lcp))]
    index          = argmax(candidate_LCPs)
    return text[r[index]:r[index]+candidate_LCPs[index]]



String1, String2 = ReadFile()
Result = LongestSharedSubstring(String1, String2)
print(Result)