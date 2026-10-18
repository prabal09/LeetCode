from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize the result array with 0s
        res = [0] * len(temperatures)
        # The stack will store indices of the temperatures array
        stack = []

        for curr_idx, curr_temp in enumerate(temperatures):
            # While stack is not empty and current temp is warmer than the top of stack
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                # Calculate how many days we had to wait
                res[prev_idx] = curr_idx - prev_idx

            # Always push the current day's index onto the stack
            stack.append(curr_idx)

        return res
