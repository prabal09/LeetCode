import heapq
class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # This is using MAX-HEAP
        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapq.heapify(nums)

        for _ in range(k-1):
            heapq.heappop(nums)

        return -heapq.heappop(nums)


import heapq
class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # This is using MIN-HEAP
        min_heap = []

        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap,num)
            else:
                heapq.heappushpop(min_heap,num)

        return min_heap[0]
