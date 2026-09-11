class Solution:
    def maximumInvitations(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # Track which boy is matched with each girl. -1 means unassigned.
        girl_to_boy = [-1] * n

        def dfs(boy, visited):
            for girl in range(n):
                # If the boy can invite this girl and she hasn't been looked at in this round
                if grid[boy][girl] == 1 and not visited[girl]:
                    visited[girl] = True

                    # If the girl is free OR her current partner can find someone else
                    if girl_to_boy[girl] == -1 or dfs(girl_to_boy[girl], visited):
                        girl_to_boy[girl] = boy
                        return True
            return False

        accepted_invitations = 0

        # Try to find a match for each boy
        for boy in range(m):
            visited = [False] * n  # Reset visited array for each boy's search
            if dfs(boy, visited):
                accepted_invitations += 1

        return accepted_invitations
