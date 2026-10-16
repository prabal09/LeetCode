class Solution:
    def pivotIndex(self, nums: list[int]) -> int:

        total_summ = sum(nums)
        left_summ = 0

        for i, num in enumerate(nums):
            if left_summ == total_summ - left_summ - num:
                return i
            left_summ += num

        return -1

'''
Time Complexity: O(n)
Space Complexity: O(1)
'''
