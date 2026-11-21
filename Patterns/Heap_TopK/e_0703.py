import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)  # O(n)

        # Keep only the k largest elements
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)

        # If size exceeds k, remove the smallest of the top k+1 elements
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        # The root is always the kth largest element
        return self.min_heap[0]
