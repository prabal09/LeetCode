class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        count = 0
        prefix_sums = {0:1}

        curr_summ = 0

        for num in nums:
            curr_summ += num
            diff = curr_summ - goal
            if diff in prefix_sums:
                count += prefix_sums[diff]

            prefix_sums[curr_summ] = prefix_sums.get(curr_summ,0) + 1

        return count

'''
- Time Complexity: O(n)
- Space Complexity: O(n)
'''
