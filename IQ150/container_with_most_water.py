class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        l = 0; r = len(height) - 1
        while l < r:
            max_water = max(max_water,(r-l)*min(height[l],height[r]))
            if height[l] > height[r]:
                r -=1
            else:
                l+=1
        return max_water
