def minSubArrayLen(target: int, nums: list[int]) -> int:
    # Initialize the left pointer and running sum
    left = 0
    current_sum = 0
    min_length = float('inf')

    # Expand the window using the right pointer
    for right in range(len(nums)):
        current_sum += nums[right]

        # Shrink the window from the left as long as the condition is met
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_length if min_length != float('inf') else 0
