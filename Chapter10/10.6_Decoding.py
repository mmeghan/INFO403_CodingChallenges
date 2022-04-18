'''
Goal: Implement the Viterbi algorithm solving the Decoding problem
Input: A string x, followed by the alphabet from which x was constructed followed by states States,
        transition matrix Transition, and emission matrix Emission of an HMM (Sigma, States, Trasition, Emission)
Output: A path that maximizes the (unconditional) probability Pr(x,pi) over all possible paths pi

./testcases/10.6Decoding_Sample.txt
'''
def ReadFile():
    with open('./datasets/dataset_609242_7.txt', 'r') as f:
        x = str(f.readline().strip())
        f.readline()
        Symbols = f.readline().strip().split()
        f.readline()
        States = f.readline().strip().split()
        f.readline()
        f.readline()
        Transition = {}
        for i in range(len(States)):
            matrix = [float(k) for k in f.readline().strip().split()[1:]]
            for j in range(len(States)):
                Transition[States[i]+States[j]] = matrix[j]
        
        f.readline()
        f.readline()
        Emission = {}
        for i in range (len(States)):
            matrix = [float(k) for k in f.readline().strip().split()[1:]]
            for j in range(len(Symbols)):
                Emission[States[i]+Symbols[j]] = matrix[j]
    return x, Symbols, States, Transition, Emission

def Viterbi (x, Symbols, States, Transition, Emission):
    startingProb = [1/len(States)]* len(States)
    V = [{}]
    for State in States:
        V[0][State] = {"prob": startingProb[0] * Emission[State+x[0]], "prev": None }
    #Run Viterbi when t > 0 
    for i in range(1,len(x)):
        V.append({})
        for State in States:
            maxTransitionProb = max(V[i-1][prevState]["prob"] * Transition[prevState+State] for prevState in States)
            for prevState in States:
                if V[i-1][prevState]["prob"] * Transition[prevState+State] == maxTransitionProb:
                    maxProbability = maxTransitionProb * Emission[State+x[i]]
                    V[i][State] = {"prob": maxProbability, "prev": prevState}
                    break 

    #get the highest probability 
    opt = []
    maxProbability = max(value["prob"] for value in V[-1].values())

    previous = None
    #Get most probable state and its back track 
    for State, data in V[-1].items():
        if data["prob"] == maxProbability:
            opt.append(State)
            previous = State
            break 

    #continue to backtrack to get to the first observation 
    for i in range (len(V) -2, -1, -1):
        opt.insert(0, V[i+1][previous]["prev"])
        previous = V[i+1][previous]["prev"]
       
    
    return opt, maxProbability

x, Symbols, States, Transition, Emission = ReadFile()

Path, maxProbability = Viterbi(x, Symbols, States, Transition, Emission)
print(''.join(i for i in Path))


