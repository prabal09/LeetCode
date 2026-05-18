from collections import defaultdict
from math import gcd
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        best_line_max = 1
        for i in range(len(points)):
            anchor = points[i]
            # print(anchor, end = " ")
            slopes_counter = defaultdict(tuple)
            for j in range(i+1,len(points)):
                point_j = points[j]
                dx = point_j[0] - anchor[0]
                dy = point_j[1] - anchor[1]
                g = gcd(dx,dy)
                if dx < 0:
                    dx,dy = -dx,-dy
                elif dx == 0 and dy < 0: # Handle the vertical line case
                    dy = -dy
                slope = (dx//g,dy//g)
                slopes_counter[slope] = slopes_counter.get(slope,0) + 1
            if slopes_counter:
                best_line_max = max(best_line_max,1+max(slopes_counter.values()))
                # print(slopes_counter)
        return best_line_max
