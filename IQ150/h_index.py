class Solution1:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        citations = citations[::-1]
        res = 0
        print(citations)
        for i in range(len(citations)):
            if citations[i]>=i+1:
                res+=1
        return res

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        papers = [0]*(len(citations)+1)
        n_papers = len(citations)
        for i in citations:
            if i>=len(citations):
                papers[n_papers]+=1
            else:
                papers[i]+=1

        h = n_papers
        papers_c = papers[n_papers]
        while papers_c < h:
            h-=1
            papers_c += papers[h]
        return h
