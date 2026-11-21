class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [pt[0]**2 + pt[1]**2 for pt in points]
        points_sorted = [x for _, x in sorted(zip(dist, points))]
        return points_sorted[:k]
        # O(nlogn); O(n)
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(xi,yi):
            return xi**2 + yi**2
        if k == 0:
            return []
        if len(points) == k:
            return points

        heap = []
        # build a heap of size k
        for x,y in points:
            d = dist(x,y)

            if len(heap) < k:
                heapq.heappush(heap,(-d,x,y))
            else:
                heapq.heappushpop(heap,(-d,x,y))

        return [[x,y] for d,x,y in heap]

# O(nlogk); O(k)
