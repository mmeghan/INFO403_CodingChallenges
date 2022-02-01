def read(fname):
    with open(fname) as file:
        lines = file.read()
        txt = lines.split('\n', 1)[0]
        k = int (lines.split('\n',2)[1])
        print(k, '\n')
    FrequencyTable(txt, k)
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
    HighestFrequency(dict)
def HighestFrequency(dict):
    freq_pattern = []
    max_key = max(dict, key=dict.get)
    max_freq = dict[max_key]
    for key in dict:
        if dict.get(key) == max_freq:
            freq_pattern.append(key)
    print(freq_pattern)



read('dataset_609061_13.txt')
