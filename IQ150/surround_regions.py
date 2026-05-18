class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()

        rows,cols = len(board), len(board[0])

        def dfs(r,c):
            if r >=0 and c >=0 and r < rows and c < cols and (r,c) not in visited and board[r][c] != "X":
                visited.add((r,c))
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
            else:
                return None

        for r in range(rows):
            dfs(r,0)
            dfs(r,cols-1)

        for c in range(cols):
            dfs(0,c)
            dfs(rows-1,c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in visited:
                    board[r][c] = "X"
