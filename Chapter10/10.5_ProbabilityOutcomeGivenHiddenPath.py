'''
Goal: Solve the probability of an outcome given a hidden path problem 
Input: A string x, followed the alphabet from which x was constructed, followed by a hidden path, 
        followed by the states States and emission matrix Emission of an HMM (Sigma, States, Transition, Emission)
Output: The conditional probability Pr(x|pi) that x will be emitted given the HMM follows the hidden path

./testcases/10.5ProbOutcomeGivenHiddenPath_Sample.txt


'''
def ReadFile():
    with open ('./datasets/dataset_609241_10.txt', 'r') as f:
        x = str(f.readline().strip())
        f.readline()
        Symbols = f.readline().strip().split()
        f.readline()
        Path = str(f.readline().strip())
        f.readline()
        States = f.readline().strip().split()
        f.readline()
        f.readline()
        Matrix = [line.strip().split() for line in f.readlines()]

        Emissions = {}
        for row in Matrix:
            for i, prob in enumerate(row[1:]):
                Emissions[row[0] + Symbols[i]] = float(prob)
        return x, Symbols, Path, States, Emissions

def ConditionalProbability (x,States, Path, Emission):
    Pr = 1
    for i in range (len(x)):
        Pr *= Emission[Path[i]+x[i]]
    return Pr

x, Symbols, Path, States, Emission = ReadFile()

Pr = ConditionalProbability(x, States, Path, Emission)
print(Pr)