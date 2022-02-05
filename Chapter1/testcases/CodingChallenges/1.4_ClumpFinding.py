from os import read


def readFile(file):
    with open (file, 'r') as f:
        lines = f.read()
        genome = lines.split('\n', 1)[0]
        vars = lines.split('\n', 2)[1]
    
    k = int(vars.split(' ',3)[0])
    L = int(vars.split(' ', 3)[1])
    t = int(vars.split(' ',3)[2])
    return(genome, k, L, t)

def FrequencyTable(txt, k):
    dict = {}
    n = len(txt)
    for i in range (0,(n-k)):
        pattern = txt[i:(i+k)]
        if pattern in dict.keys():
            count = dict.get(pattern)
            count += 1
            dict[pattern] = count 
        else:
            dict[pattern] = 1
    return(dict)

def FindClumps(file):
    reader = readFile(file)
    patterns = []
    n = len(reader[0])
    for i in range(0, (n-reader[2])):
        window = reader[0][i:(reader[2])]
        freqMap = FrequencyTable(window, reader[1])
        for key in freqMap:
             if freqMap.get(key) >= reader[3] and key not in patterns:
                patterns.append(key)
        i = i + reader[2] -1
    
    listToStr = ' '.join([str(elem) for elem in patterns])
    return(listToStr)

print(FindClumps('dataset_609063_5.txt'))
#print(FindClumps('./ClumpFinding/inputs/input_3.txt'))
