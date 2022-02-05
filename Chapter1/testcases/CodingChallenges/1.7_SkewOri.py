##input- DNA genome string 
##output- All integer(s) i minimizing Skew(i)(gemone) among all values of i from 0 to |genome|
##Goal- fine a position in a genome where the skew diagram attains a minimum 

def CalcSkew(file):
    with open (file, 'r') as f:
        genome = f.read().strip()
    Skews = []
    currSkew = 0
    Skews.append(currSkew)
    for i in range(0,len(genome)):
        if genome[i] == "C":
            currSkew -= 1
        elif genome[i] == "G":
            currSkew += 1 
        Skews.append(currSkew)
    print(Skews)
    mins = findMinimum(Skews)
    return (mins)

def findMinimum(Skews):
    mins = " "
    smallest = min(Skews)
    for i in range(0,len(Skews)):
        if Skews[i] == smallest:
            mins += str(i) + ' '
    return(mins)

print(CalcSkew('dataset_609066_10.txt'))
