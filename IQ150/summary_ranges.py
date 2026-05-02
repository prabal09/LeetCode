class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        while i < len(nums):
            j = i+1
            start = str(nums[i])
            num = nums[i]
            # print('before entering while',i,j)
            while j <= len(nums)-1 and num + 1 == nums[j]:
                # print('after entering while',i,j)
                num = nums[j]
                j +=1
            end = start + "->" + str(num) if num != nums[i] else start
            res.append(end)
            i = j
        return res