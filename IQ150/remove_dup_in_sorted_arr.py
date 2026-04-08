# O(nlongn) SC O(n)
class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums1 = list(set(nums))
        uni = len(nums1)
        nums1.sort()
        nums[:len(nums1)] = nums1
        # print(nums,uni)
        return uni

class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        if nums == []:
            return 0
        else:
            i = 0;j=i+1
            while j<=len(nums)-1:
                if nums[i]==nums[j]:
                    j+=1
                else:
                    k+=1
                    nums[k-1] = nums[j]
                    i = j
        return k
    
class Solution3:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[i - 1]:
                nums[i] = nums[j]
                i += 1
        return i