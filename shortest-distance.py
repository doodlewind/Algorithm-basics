from datetime import datetime
import random
import math
N = 5000
RANGE = 100000
INF = 1000001


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "[" + str(self.x) + "," + str(self.y) + "]"


def distance(a, b):
    return math.sqrt((a.x - b.x)*(a.x - b.x) + (a.y - b.y)*(a.y - b.y))


def basic_min_distance(p):
    min_distance = [distance(p[0], p[1]), 0, 1]
    for i in range(N):
        for j in range(i+1, N):
            d = distance(p[i], p[j])
            if d < min_distance[0]:
                min_distance = [d, i, j]
    print "Min Distance:", min_distance[0], "Points:", p[min_distance[1]], p[min_distance[2]]


def d_c_min_distance(arr):
    if len(arr) == 1:
        return INF

    mid = len(arr)/2
    x_mid = arr[mid-1].x
    l_min = d_c_min_distance(arr[:mid])
    r_min = d_c_min_distance(arr[mid:])
    dist = min(l_min, r_min)
    min_dist = dist
    for point_l in arr[:mid]:
        for point_r in arr[mid:]:
            if point_r.x - x_mid < dist and math.fabs(point_r.y - point_l.y) < dist:
                lr_dist = distance(point_l, point_r)
                if lr_dist < min_dist:
                    min_dist = lr_dist
            if point_r.x - x_mid > dist:
                break
    return min_dist


if __name__ == '__main__':
    points = []
    coordinates = random.sample(xrange(RANGE), N * 2)
    for k in range(0, N * 2, 2):
        points.append(Point(coordinates[k], coordinates[k+1]))

    start = datetime.now()
    basic_min_distance(points)
    end = datetime.now()
    print "Time of basic method:", end - start

    start = datetime.now()
    points.sort(key=lambda a: a.x)
    print "Min distance:", d_c_min_distance(points)
    end = datetime.now()
    print "Time of divide conquer method:", end - start