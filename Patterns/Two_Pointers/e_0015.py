class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()  # Step 1: Sort the array

        for i in range(len(nums) - 2):
            # Step 2: Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # If the fixed number is greater than 0, no remaining triplet can sum to 0
            if nums[i] > 0:
                break

            # Step 3: Two-pointer traversal
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1

        return res

'''
Time Complexity: (O(n**2)
Space Complexity: (O(n))
'''
