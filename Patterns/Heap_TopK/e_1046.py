import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Negate weights to simulate a max-heap using Python's min-heap
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            # Pop the two heaviest stones (most negative values)
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)

            # If weights differ, push the remainder back into the heap
            if y != x:
                heapq.heappush(max_heap, -(y - x))

        return -max_heap[0] if max_heap else 0
