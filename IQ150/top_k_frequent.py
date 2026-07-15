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


from collections import Counter
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)

        bucket = [0]*(len(nums)+1)

        for num,freq in freqs.items():
            if bucket[freq] == 0:
                bucket[freq] = [num]
            else:
                bucket[freq].append(num)

        res = []
        for i in range(len(nums),-1,-1):
            if bucket[i] !=0:
                res.extend(bucket[i])
            if len(res) == k:
                break
        return res
