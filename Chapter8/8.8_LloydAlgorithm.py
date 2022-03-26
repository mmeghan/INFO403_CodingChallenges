'''
Goal: Implement the Lloyd algorthim for k-means clustering 
Input: Integers k and m followed by a set of points Data in m-dimensional space
Output: A set Centers consisting of k points (centers) resluting from applying the Lloyd algorithm to Data and Centers,
        where the first k points from Data are selected as the first k centers 
LLoyd Algorithm:
    - first chooses k arbitary distinct points Centers from Data as centers 
    - assign each data point to the cluster correspinding to its nearest center 
    - assign each clusters center of gravity to be the clusters new center 

Center of Gravity: the point whose i-th coordinate is the average of the i-th coordinates of all points 
./testcases/LloydAlgorithm_Sample.txt
'''
import math 
import sys

def ReadFile():
    with open ('./datasets/dataset_609201_3.txt', 'r') as f:
        ints = f.readline().strip().split()
        k = int(ints[0])
        m = int(ints[1])
        points = []
        for line in f:
            points.append([float(p) for p in line.split()])
    return k, m, points

def min_euclidian_distance(point1, point2):
    #want to minimize some distance function between centers and data over all possible choices of centers 
    #calculates Euclidean distance as the length of the line segment connecting two points    
    sum = 0 
    for i in range(len(point1)):
        sum += (point1[i] - point2[i])**2
    return math.sqrt(sum)

def CenterOfGravity(cluster):
    center = [0]*len(cluster[0])
    for point in cluster:
        #loop though every point in the cluster 
        for i in range(len(point)):
            #add the vlaue of the point cordinate to the center, both x and y coordinates
            center[i] += point[i]
    #find the average value for the x and y coordinates from all points in the cluster to find the center of gravity 
    center = [center[i]/len(cluster) for i in range(len(center))]
    return center 

def Centers2Clusters(centers, points):
    clusters = [[] for i in range(len(centers))]
    for point in points:
        #loop though the list of points and establish the minimum distacnce as a crazy large number and the index of the first cluster to be zero
        min_distance = sys.maxsize
        cluster = 0 
        for i, c in enumerate(centers):
            #for every increment(i) and center in centers if the distance between the point and center is less than the huge number 
            #set the minimum distance as that value and create a cluster 
            #add that point to its cluster 
            if min_distance > min_euclidian_distance(point, c):
                min_distance = min_euclidian_distance(point, c)
                cluster = i
        clusters[cluster].append(point)
    return centers, clusters

def Clusters2Centers(clusters, centers):
    for i, cluster in enumerate(clusters):
        #for every increment(i) and cluster in clusters calculate the center of gavity from the points in the cluster
        centers[i] = CenterOfGravity(cluster)
    return centers 

def LLoydAlgorithm(k, points):
    centers = [points[i] for i in range(k)]
    clusters = [0]

    prevCenters, prevClusters = None, None
    #while the previous centers and clusters aren't the current centers and clusters 
    while prevCenters != centers and prevClusters != clusters:
        #set the previous centes and clusters as the current iteration 
        prevCenters = list(centers)
        prevClusters = list(clusters)

        centers, clusters = Centers2Clusters(centers, points)
        centers = Clusters2Centers(clusters, centers)
    #formating to reduce the number of decimal places given 
    for center in centers:
        for i in range(len(center)):
            center[i] = format(round(center[i], 3), '.3f')
    return centers

k, m, points = ReadFile()
centers = LLoydAlgorithm(k, points)
with open('./solutions/LloydAlgorithm_Solution.txt' , 'w') as solution:
    for center in centers:
        for value in center:
            solution.write(value + ' ')
        solution.write('\n')
