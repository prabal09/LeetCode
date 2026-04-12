class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        i = 0; d = 1
        M = [[ ] for _ in range(numRows)]
        # print(M)
        for ch in s:
            # print(ch)
            M[i].append(ch)
            if i == numRows-1:
                d=-1
            if i==0:
                d = 1
            if d == -1:
                i-=1
            else:
                i+=1
        # print(M)
        s_ans = ''
        for i in range(numRows):
            s_ans += ''.join(M[i])
        return s_ans