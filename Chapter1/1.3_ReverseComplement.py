def FindComplement(file):
    with open (file, 'r') as f:
        txt = f.read().rstrip()
    #print(txt, '\n')
    reverseComp = ""
    i = (len(txt)-1)

    while i >= 0:
        if txt[i] == "A":
            reverseComp+= "T"
        elif txt[i] =="T":
            reverseComp+= "A"
        elif txt[i] == "C":
            reverseComp+= "G"
        elif txt[i] == "G":
            reverseComp+= "C"
      
        i = i-1

    print(reverseComp)
    return(reverseComp)
FindComplement('dataset_609062_2.txt')