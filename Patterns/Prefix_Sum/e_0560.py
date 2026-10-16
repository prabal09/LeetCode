class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0:1}
        count = 0
        curr_sum = 0
        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            if diff in prefix_sums:
                count +=prefix_sums[diff]
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum,0) + 1

        return count

'''
- Time Complexity: (O(n)
- Space Complexity: (O(n)
'''
