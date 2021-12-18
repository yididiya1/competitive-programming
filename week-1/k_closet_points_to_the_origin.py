from math import sqrt


def kClosest(points, k):
    distance = list(map(lambda x: x[0]**2 + x[1]**2, points))
    #print(distance)
    result = []
    distance_point = []
    
    for i in range(len(points)):
        v = (distance[i],points[i])
        distance_point.append(v)
    
    
    distance_point.sort(key=lambda tup: (tup[0]))
    
    #print(distance_point)
    
    for i in range(k):
        result.append(distance_point[i][1])
    
    return result




example = kClosest([[1,3],[-2,2]],1)
print(example)
