class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(list(set(nums)))

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False

'''
Time Complexity: (O(n))
Space Complexity: (O(n))
'''
