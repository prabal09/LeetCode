class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        fruit_counts = {}
        left = 0
        max_fruits = 0

        for right in range(len(fruits)):
            fruit_counts[fruits[right]] = fruit_counts.get(fruits[right], 0) + 1

            while len(fruit_counts) > 2:
                left_fruit = fruits[left]
                fruit_counts[left_fruit] -= 1
                if fruit_counts[left_fruit] == 0:
                    del fruit_counts[left_fruit]
                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits

# "Find the longest contiguous subarray containing at most 2 distinct elements."
'''
[1,2,1] -> 3
[0,1,2,2] -> 3
[1,2,3,2,2] -> 4
'''

class Solution:
    def longestContiguousSubarr(self, nums: list[int]) -> int:
        max_len = 0
        left = 0
        window = {}
        for right, num in enumerate(nums):
            window[num] = window.get(num,0) + 1

            while len(window) > 2:
                left_num = nums[left]
                window[left_num] -=1
                if window[left_num] == 0:
                    window.pop(left_num)
                left +=1
            max_len = max(max_len, right - left + 1)

        return max_len

'''
Time: O(n)
Space: O(1)
'''
