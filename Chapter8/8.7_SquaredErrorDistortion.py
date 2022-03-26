'''
Goal: Compute the squared error distortion of a set of data points with respect to 
      a set of data points with respect to a set of centers
Input: A set of points Data and a set of centers Centers
Output: The squared error distortion Distortion(data, centers)

Distoration(Data, Centers) = (1/2) Sigma of all points DataPoint in Data D(DataPoint, Centers)^2

testcases/DistortionError_Sample

'''

def ReadFile():
    with open('./datasets/dataset_609200_3.txt', 'r') as f:
        ints = f.readline().strip().split()
        k = int(ints[0])
        m = int(ints[1])
        centers = set()
        for i in range(k):
            centers.add(tuple(map(float, f.readline().strip().split())))
        f.readline()
        data = {tuple(map(float, line.strip().split())) for line in f.readlines()}
    return k, m, centers, data

def min_euclidian_distance(p, centers):
    #want to minimize some distance function between centers and data over all possible choices of centers 
    #calculates Euclidean distance as the length of the line segment connecting two points    
    return min(sum((i-j) ** 2 for i, j in zip(p,q)) ** 0.5 for q in centers)

def SquaredErrorDistortion(data,centers):
    #Given a set of data and set of centers, the squared error distortion of data and centers 
    # is defined as the mean squared distance from reach point to its nearest center
    distortion = sum(min_euclidian_distance(point, centers) **2 for point in data) / len(data)
    return distortion

k, m, centers, data = ReadFile()
distortion = SquaredErrorDistortion(data, centers)
print(distortion)
