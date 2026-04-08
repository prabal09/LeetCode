class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res,maxC = nums[0],1
        for i in range(len(nums)):
            if nums[i] in count.keys():
                count[nums[i]] +=1
                if count[nums[i]] > maxC:
                    maxC = count[nums[i]]
                    res = nums[i]
            else:
                count[nums[i]] =1
        return res

class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = nums[0], 1
        for n in nums[1:]:
            if res == n:
                count +=1
            else:
                count -=1
                if count == 0:
                    res = n
                    count = 1
            print(n,res,count)
        return res