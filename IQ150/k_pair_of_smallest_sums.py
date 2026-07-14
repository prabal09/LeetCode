import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []

        heap = []
        m,n = len(nums1), len(nums2)
        # build the heap
        for i in range(min(m,k)):
            heapq.heappush(heap,(nums1[i]+nums2[0],i,0))

        # make k iterations in the heap
        res = []
        # print(heap)
        while heap and len(res) < k:
            summ,i,j = heapq.heappop(heap)
            # print(i,j)
            # i,j = iters
            res.append([nums1[i],nums2[j]])

            if j + 1 < len(nums2):
                heapq.heappush(heap,(nums1[i]+nums2[j+1],i,j+1))

        return res
