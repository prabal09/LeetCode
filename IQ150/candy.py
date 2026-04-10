class Solution:
    def candy(self, ratings: List[int]) -> int:
        arr_candy = [1]*len(ratings)

        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                arr_candy[i] = arr_candy[i-1]+1
        
        # print(arr_candy)
        for j in range(len(ratings)-2,-1,-1):
            # print(j)
            # print('before',arr_candy)
            if ratings[j]>ratings[j+1]:
                # print(j,':=',ratings[j],ratings[j+1])
                arr_candy[j] = max(arr_candy[j],arr_candy[j+1]+1)
                # print('after',arr_candy)
        # print(arr_candy)
        return sum(arr_candy)