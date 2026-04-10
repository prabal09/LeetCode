class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxL = [0]*n
        maxR = [0]*n
        l= r = 0
        for i in range(n):
            j = -i-1
            maxL[i] = l
            maxR[j] = r
            l = max(l,height[i])
            r = max(r,height[j])
        # print(maxL,maxR)
        rw = 0
        for k in range(n):
            pot = min(maxL[k],maxR[k])-height[k]
            rw += max(0,pot)
        return rw