def read(fname):
    with open(fname) as file:
        lines = file.read()
        string1 = lines.split('\n', 1)[0]
        string2 = lines.split('\n',2)[1]
    HammingDistance(string1, string2)

def HammingDistance(string1, string2):
    mismatches= 0
    for i in range(0,len(string1)):
        if string1[i] != string2[i]:
            mismatches += 1
    print(mismatches)
    return mismatches 

read('dataset_609067_3.txt')


