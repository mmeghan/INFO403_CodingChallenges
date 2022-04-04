'''
Goal: Construct the Burrows-Wheeler transform of a string.
Input: a string Text 
Output:BWT(Text).


'''
def ReadFile():
    with open('./testcases/BurrowsWheeler_Sample.txt', 'r') as f:
        Text = f.readline().strip()
    return Text 

Text = ReadFile()