class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = 0
        curr_max, max_sum = 0, float('-inf')
        curr_min, min_sum = 0, float('inf')

        for num in nums:
            total_sum += num

            # Kadane's for Maximum Subarray
            curr_max = max(num, curr_max + num)
            max_sum = max(max_sum, curr_max)

            # Kadane's for Minimum Subarray
            curr_min = min(num, curr_min + num)
            min_sum = min(min_sum, curr_min)

        # If all numbers are negative, return max_sum directly
        return max_sum if max_sum < 0 else max(max_sum, total_sum - min_sum)
            
