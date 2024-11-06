'''Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.'''


# Solution
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        
        ans = 2

        for point_1 in points:

            hash_map = defaultdict(int)
            
            for point_2 in points:
                if point_1 != point_2:
                    x1, y1 = point_1
                    x2, y2 = point_2

                    if x1 == x2:
                        hash_map["inf"] += 1
                    else:
                        hash_map[(y2-y1)/(x2-x1)] += 1
            ans = max(ans, max(hash_map.values()) + 1)
        return ans