class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1

        buckets = [[] for _ in range(len(nums)+1)]
        for num, freq in count.items():
            buckets[freq] = num

        result = []

        for bucket in buckets[::-1]:
            for i in range(len(bucket)):
                result.append(bucket[i])
                if len(result) == k:
                    return result

'''
Time Complexity: (O(n)
Space Complexity: O(n)
'''

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # 1. Count frequencies
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # 2. Maintain a min-heap of size k
        heap = []
        for num, freq in count.items():
            # Push pair of (frequency, number) to sort by frequency
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        # 3. Extract numbers from heap
        return [num for freq, num in heap]
