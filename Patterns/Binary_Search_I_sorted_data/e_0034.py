class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def binarySearch(findLeft = True):
            left, right = 0, len(nums)-1
            idx = -1

            while left <= right:
                mid = (left + right)//2

                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    idx = mid

                    if findLeft:
                        right = mid - 1
                    else:
                        left = mid + 1
            return idx

        first_pos = binarySearch(findLeft = True)
        last_pos = binarySearch(findLeft = False)

        return [first_pos, last_pos]

'''
Time Complexity: O(log n)
Space Complexity: O(1)
'''
