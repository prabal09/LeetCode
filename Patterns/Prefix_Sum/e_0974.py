class Solution:
    def subarraysDivByK(self,nums: list[int], k: int) -> int:
        # Hash map to store frequencies of prefix sum remainders
        remainder_counts = {0: 1}

        running_sum = 0
        total_subarrays = 0

        for num in nums:
            running_sum += num
            remainder = running_sum % k

            # If the remainder exists in our map, add its frequency to total
            if remainder in remainder_counts:
                total_subarrays += remainder_counts[remainder]
                remainder_counts[remainder] += 1
            else:
                remainder_counts[remainder] = 1

        return total_subarrays
