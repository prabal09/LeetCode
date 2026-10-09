class Solution:
    def twoSum(self,nums: list[int], target: int) -> list[int]:
        seen = {}
        for i,num in enumerate(nums):
            compliment = target - num
            if compliment in seen:
                return [i,seen[compliment]]
            seen[num] = i

'''
Time Complexity: (O(n))
Space Complexity: (O(n))
'''
