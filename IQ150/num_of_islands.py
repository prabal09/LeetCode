from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            directions = [(-1,0),(1,0),(0,1),(0,-1)]
            while q:
                r1,c1 = q.popleft()
                for dr,dc in directions:
                    if 0<=r1+dr<rows and 0<=c1+dc<cols and ((r1+dr,c1+dc)) not in visited and grid[r1+dr][c1+dc] == "1":
                        visited.add((r1+dr,c1+dc))
                        q.append((r1+dr,c1+dc))

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1":
                    visited.add((r,c))
                    bfs(r,c)
                    islands +=1
        return islands
