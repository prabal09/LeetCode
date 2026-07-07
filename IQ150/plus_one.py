class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] !=9:
            digits[-1] +=1
            return digits
        else:
            carry = 1
            for d in range(len(digits) - 1, -1, -1):
                # print(d,carry)
                # print(digits[d])
                num = digits[d] + carry
                # print(num)
                if num == 10:
                    carry = 1
                    digit = 0
                    digits[d] = digit
                else:
                    carry = 0
                    digit = num
                    digits[d] = digit
                # print(digits)
            if carry == 1:
                digits = [1] + digits
                # print(digits)
            return digits
