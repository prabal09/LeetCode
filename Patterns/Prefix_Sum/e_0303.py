class NumArray:

    def __init__(self, nums: list[int]):
        if nums:
            self.nums = nums
            self.prefix_nums = [nums[0]]*len(nums)
            for i in range(1,len(self.nums)):
                self.prefix_nums[i] = self.prefix_nums[i-1] + self.nums[i]
        else:
            self.prefix_nums = []

    def sumRange(self, left: int, right: int) -> int:
        if left != 0:
            return self.prefix_nums[right] - self.prefix_nums[left-1]
        return self.prefix_nums[right]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

'''
Time Complexity: __init__: (O(n); sumRange: O(1)
Space Complexity: O(n) for the prefix-sum array.
'''
