class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        if not nums:
            return 0

        for n in num_set:
            if (n-1) in num_set:
                continue

            curr = n
            curr_streak = 1
            while curr + 1 in num_set:
                curr_streak +=1
                curr += 1

            longest_streak = max(curr_streak, longest_streak)

        return longest_streak

'''
Time Complexity: (O(n))
Space Complexity: (O(n))
'''
