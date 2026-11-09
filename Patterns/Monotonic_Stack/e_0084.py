class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []  # Pairs of (index, height)
        max_area = 0
        
        for i, h in enumerate(heights):
            start = i
            # If the current bar is shorter than the bar at the top of the stack,
            # we must pop from the stack and calculate areas.
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                # The popped bar can extend from its original start index up to i
                max_area = max(max_area, height * (i - idx))
                # The current bar can extend backwards to include the popped bar's position
                start = idx
                
            stack.append((start, h))
            
        # Clear out any remaining bars in the stack
        for idx, height in stack:
            max_area = max(max_area, height * (len(heights) - idx))
            
        return max_area
