class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        X = len(intervals)
        for I, ix in enumerate(intervals):
            if newInterval[0] < ix[0]:
                X = I
                break
        intervals.insert(X,newInterval)
        # print(intervals)
        M_intervals = [intervals[0]];X = 0
        for I in intervals[1:]:
            # print(I,X)
            if I[0]<= M_intervals[X][1]:
                M_intervals[X][1] = max(I[1],M_intervals[X][1])
            else:
                M_intervals.append(I)
                X +=1
        return M_intervals
