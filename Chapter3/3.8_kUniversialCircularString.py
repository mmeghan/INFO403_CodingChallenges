'''
Code Challenge: Solve the k-Universal Circular String Problem.

Input: An integer k.
Output: A k-universal circular string.
'''
def GenerateBinaryStrings(bit_count):
    binary_strings = []
    def genbin(n, bs=''):
        if len(bs) == n:
            binary_strings.append(bs)
        else:
            genbin(n, bs + '0')
            genbin(n, bs + '1')
    genbin(bit_count)
    return binary_strings

def kUniversalString(n):
    patterns = GenerateBinaryStrings(n)
    dB = DeBrujin(patterns)
    path = EulerianCycle(dB)
    