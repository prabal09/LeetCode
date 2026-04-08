# TC O(n) SC O(1)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0;
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
            # print(nums)
        return k
    
class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_c = nums[:]
        k = len(nums_c)
        for i in range(len(nums)):
            if nums[i] == val:
                nums_c.remove(val)
                k-=1
        nums[:] = nums_c
        return k