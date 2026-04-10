class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        summ = 0
        n = len(s)
        # print(list(range(-1,-n-1,-1)))
        for i in range(-1,-n-1,-1):
            # print(i,s[i])
            if i !=-1 and nums[s[i]] < nums[s[i+1]]:
                var =-nums[s[i]]
            else:
                var =+nums[s[i]]
            summ +=var
            # print(summ)
        return summ