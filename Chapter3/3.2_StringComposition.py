#input - An integer k adn a strign text 
#output- Compositionk(Text), where k-mers 

def ReadFile(file):
    with open(file, 'r') as f:
        data = f.readlines()
        k = int(data[0])
        genome = data[1].strip()
    return (genome, k)

def StringComposition(file):
    inputs = ReadFile(file)
    genome = inputs[0]
    k = inputs[1]

    Compositions = []
    for i in range(len(genome) +k -1):
        substring = genome[i:(i+k)]
        if len(substring) != k:
            continue
        Compositions.append(substring)
    solution =  open('StringCompositionSolution.txt', 'a')
    for sub in Compositions:
        solution.write(sub)
        solution.write('\n')

StringComposition('dataset_609095_3.txt')
