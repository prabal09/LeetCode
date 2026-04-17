class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        if min(nums) > 0:
            return []
        
        nums.sort()

        start = 0;
        
        # print(nums)

        ans = []
        while start < len(nums)-2:
            
            L = start + 1; R = len(nums)-1
            if start > 0 and nums[start] == nums[start-1]:
                # print('same num so skipping',start)
                start +=1
                continue
            # print('starting with ',start, nums[start])
            while L<R:
                # print(start,L,R)
                if nums[L] + nums[R] + nums[start] == 0:
                    ans.append([nums[start],nums[L],nums[R]])
                    # print('added ',[nums[start],nums[L],nums[R]])
                    L +=1
                    while nums[L] == nums[L-1] and L<R:
                        L+=1
                    
                elif nums[L] + nums[R] + nums[start] > 0:
                    R -=1
                else:
                    L +=1
            start+=1
        return ans
    
class Solution:     # TC O(n^2) SC O(1) or O(n) if we consider the output list or the sorting space
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            l,r = i+1, len(nums) - 1
            while l<r:
                three_sum = a + nums[l]+ nums[r]
                if three_sum > 0: r-=1
                elif three_sum < 0: l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return res