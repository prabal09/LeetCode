class Solution:
    def minSubArrayLen(self, nums: list[int], target: int) -> int:
        min_len = float('inf')
        left = 0
        arr_sum = 0
        for right, num in enumerate(nums):
            arr_sum +=num

            while arr_sum >= target:
                min_len = min(min_len,right - left + 1)
                arr_sum -= nums[left]
                left += 1
        return min_len if min_len != float('inf') else 0

'''
Time: O(n)
Space: O(1)
'''
