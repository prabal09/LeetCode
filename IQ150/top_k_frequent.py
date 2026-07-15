import heapq
from collections import Counter
class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        heap = []

        for num, count in freq.items():
            if len(heap) < k:
                heapq.heappush(heap,(count,num))
            else:
                heapq.heappushpop(heap,(count,num))

        return [num for _, num in heap]
