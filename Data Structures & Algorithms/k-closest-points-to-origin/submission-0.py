
        

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        import math
        l1 = []
        for i in range(len(points)):
            l1.append([math.sqrt(points[i][0] ** 2 + points[i][1] ** 2), i])

        l1.sort()

        l2 = []
        for j in range(k):
            l2.append(points[l1[j][1]]) 

        return l2