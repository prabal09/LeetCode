def gameOfLife(board):
    rows = len(board)
    cols = len(board[0])
    
    # Directions for the 8 neighbors
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for r in range(rows):
        for c in range(cols):
            live_neighbors = 0
            
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                # Check if neighbor exists and was originally alive
                # We use abs(board[nr][nc]) == 1 OR state 2 to represent "was alive"
                if 0 <= nr < rows and 0 <= nc < cols and abs(board[nr][nc]) == 1:
                    live_neighbors += 1
            
            # Rule 1 or 3: Live cell dies
            if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                board[r][c] = -1 # -1 means "was alive, now dead"
            
            # Rule 4: Dead cell becomes alive
            if board[r][c] == 0 and live_neighbors == 3:
                board[r][c] = 2  # 2 means "was dead, now alive"

    # Second pass: Finalize the board
    for r in range(rows):
        for c in range(cols):
            if board[r][c] > 0:
                board[r][c] = 1
            else:
                board[r][c] = 0