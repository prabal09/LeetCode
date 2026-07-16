import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        projects = sorted([(c,p) for c,p in zip(capital,profits)])

        maxProfit_heap = []

        i = 0
        numProjects = len(projects)

        for _ in range(k):

            # add affordable projects to the heap
            while i < numProjects and projects[i][0] <=w:

                curr_profit = projects[i][1]
                heapq.heappush(maxProfit_heap,-curr_profit)

                i +=1

            if not maxProfit_heap:
                break

            w += -heapq.heappop(maxProfit_heap)

        return w
