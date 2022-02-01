'''
We can therefore summarize this solution using the following pseudocode, which relies on three problems that we have already solved:

The de Bruijn Graph Construction Problem;
The Eulerian Path Problem;
The String Spelled by a Genome Path Problem.
StringReconstruction(Patterns)
    dB ← DeBruijn(Patterns)
    path ← EulerianPath(dB)
    Text ← PathToGenome(path)
    return Text
Code Challenge: Solve the String Reconstruction Problem.

Input: An integer k followed by a list of k-mers Patterns.
Output: A string Text with k-mer composition equal to Patterns. (If multiple answers exist, you may return any one.)

'''