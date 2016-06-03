# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        l = len(points)
        if l == 0:
            return 0
        elif l == 1:
            return 1
        elif l == 2:
            return 2
        
        ret = 0
        dct = {}
        for i in range(l):
            dct = {}
            dup = 0
            for j in range(l):
                if i == j:
                    continue
                
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    dup += 1
                    continue
                elif points[i].x == points[j].x:
                    slope = 'vertical'
                else:
                    slope = 1.0 * (points[i].y - points[j].y) / (points[i].x - points[j].x)
                
                if slope in dct:
                    dct[slope] += 1
                else:
                    dct[slope] = 1
            #print dct, dup
            
            if len(dct) == 0:
                if dup > ret:
                    ret = dup
            else:
                for key, num in dct.items():
                    if num + dup > ret:
                        ret = num + dup
            
        return ret+1
