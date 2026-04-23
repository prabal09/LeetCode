class Solution:
    def isHappy(self, n: int) -> bool:
        summ = 0
        n1 = n;
        false_when_sumsq_is = 89
        while n1 !=0:
            rem = n1 % 10
            summ += rem**2

            # print(rem,summ)
            n1 = n1 // 10
            if n1 == 0:
                # print('n1 == 0')
                if summ == 1:
                    return True
                if summ ==false_when_sumsq_is:
                    return False
                n1 = summ
                summ = 0
        return False