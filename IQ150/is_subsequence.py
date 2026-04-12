class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':return True
        
        S = len(s)
        T = len(t)

        if S>T:return False

        i = 0
        for j in range(T):
            if s[i]==t[j]:
                i+=1
                if i == S: return True
        return False