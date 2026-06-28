class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [pt[0]**2 + pt[1]**2 for pt in points]
        points_sorted = [x for _, x in sorted(zip(dist, points))]
        return points_sorted[:k]
        # O(nlogn)
