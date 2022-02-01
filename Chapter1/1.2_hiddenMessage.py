def read(fname):
    with open(fname) as file:
        lines = file.read()
        txt = lines.split('\n', 1)[0]
        ##print(txt)
        pattern = lines.split('\n',2)[1]
        ##print(pattern)
    find(txt, pattern)
def find(txt, pattern):
    count = 0
    i = 0
    ##print(len(txt))
    ##print(len(pattern))
    for i in range(0, (len(txt) - len(pattern))):
        if txt[i:(i+len(pattern))] == pattern:
            count = count +1
    print (count) 

read('dataset_609061_6.txt')