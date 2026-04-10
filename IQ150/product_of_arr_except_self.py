class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_multi = 1;r_multi = 1
        l_arr = [0]*len(nums)
        r_arr = [0]*len(nums)
        for i in range(len(nums)):
            j = -i-1
            l_arr[i] = l_multi
            r_arr[j] = r_multi
            l_multi *=nums[i]
            r_multi *= nums[j]
        return [l*r for l,r in zip(l_arr,r_arr)]