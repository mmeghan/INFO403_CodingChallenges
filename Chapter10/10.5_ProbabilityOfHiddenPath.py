'''
Goal: Compute the probability of a hidden path 
Input:  hidden path π followed by the states States and 
        transition matrix Transition of a Hidden Markov Model (HMM) (Sigma, States, Transition, Emission)
Output: The probability of this path, Pr(pi)

./testcases/10.5HiddenPathProbability_Sample.txt

'''
import numpy as np 

def ReadFile():
    with open('./datasets/dataset_609241_8.txt', 'r') as f:
        Path = str(f.readline().strip())
        f.readline()
        States = f.readline().strip().split()
        f.readline()
        f.readline()
        Matrix = [line.strip().split() for line in f.readlines()]

        Transition = {}
        for row in Matrix:
            for i, prob in enumerate(row[1:]):
                Transition[row[0] + States[i]] = float(prob)
    return Path, States, Transition

def HiddenPath (Path, States, Transition):
    #inital probability of states is split evenly between the states 
    Pr = 1/ len(States)
    #for the rest of the path probabily is based on the transitions matrix
    for i in range(len(Path)-1):
        #multiply the current probabily by the previous probabilities sum
        Pr *= Transition[Path[i:i+2]]
    return Pr

    

Path, States, Transition = ReadFile()
Pr = HiddenPath(Path, States, Transition)
print('Pr', Pr)