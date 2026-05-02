class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(map(list,intervals))
        # print(intervals)
        
        M_intervals = [intervals[0]];X = 0
        for I in intervals[1:]:
            # print(I,X)
            if I[0]<= M_intervals[X][1]:
                M_intervals[X][1] = max(I[1],M_intervals[X][1])
            else:
                M_intervals.append(I)
                X +=1
            # print(M_intervals)
            
        return M_intervals