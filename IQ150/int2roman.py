class Solution:
    def intToRoman(self, num: int) -> str:
        sym = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 
               50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D',
               900:'CM', 1000: 'M'}
        divs = list(sym.keys())
        roman = ''
        for i in divs[::-1]:
            div = num//i
            num = num % i
            # print(i,div)
            for j in range(div):
                roman +=sym[i]
            # print(div,sym[div])
            # roman = roman + sym[div]
        return roman


