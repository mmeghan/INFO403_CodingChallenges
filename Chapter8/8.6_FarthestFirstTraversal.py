'''
Goal: Implement the FarthestFisrtTraversal clustering heuristic.
Input: Integers k and m followed by a set of points Data in m-dimensional space
Output: A set Centers consisting of k points (centers) resulting from applying FarthestFisrtTraversal(data,k)
        where the first pint from data is chosen as the first center to initalize the algorithm

FarthestFirstTraversal(Data, k) 
    Centers ← the set consisting of a single randomly chosen point from Data
    while |Centers| < k 
        DataPoint ← the point in Data maximizing d(DataPoint, Centers) 
        add DataPoint to Centers 
    return Centers 

  ./testcases/FarthestFirstTraversal_Sample.txt  
'''



def ReadFile():
    with open('./datasets/dataset_609199_2.txt', 'r') as f:
        ints = f.readline()
        ints = ints.split(' ')
        k = int(ints[0])
        m = int(ints[1])
        first_point = tuple(map(float, f.readline().strip().split()))
        data = {tuple(map(float, line.strip().split())) for line in f.readlines()}

    return k, m, first_point, data
def min_euclidian_distance(p, centers):
    #want to minimize some distance function between centers and data over all possible choices of centers 
    #calculates Euclidean distance as the length of the line segment connecting two points    
    return min(sum((i-j) ** 2 for i, j in zip(p,q)) ** 0.5 for q in centers)

def FarthestFirstTraversal(first_point, data, k):
    centers = {first_point}
    #adding a new center for k clusters 
    for i in range(k-1):
        #adds a new center from the point in data that is farthest from the centers chosen so far
        new_center = max(data, key = lambda x:min_euclidian_distance(x,centers))
        data.remove(new_center)
        centers.add(new_center)
    return centers

k, m, first_point, data = ReadFile()
centers = FarthestFirstTraversal(first_point, data, k)
with open('./solutions/Farthest1stTraversal_Solution.txt', 'w') as solution:
    for point in centers:
        solution.write(str(point) + '\n')

