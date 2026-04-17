class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i = j = 0
        m,n = len(matrix),len(matrix[0])
        UP_WALL = 0
        RIGHT_WALL = n
        DOWN_WALL = m
        LEFT_WALL = -1
        ans = []
        RIGHT,DOWN,LEFT,UP = "RIGHT","DOWN","LEFT","UP"
        direction = RIGHT
        print( m*n)
        while len(ans) < m*n:
            print('len(ans)',len(ans))
            if direction == RIGHT:
                print('direction ',direction,len(ans))
                while (j< RIGHT_WALL):
                    ans.append(matrix[i][j])
                    j +=1 # j increases from left to right
                i +=1 # To move down
                j -=1 # To get within bounds
                RIGHT_WALL -=1
                direction = DOWN
            
            elif direction == DOWN:
                print('direction ',direction,len(ans))
                # print(DOWN_WALL)
                while (i< DOWN_WALL):
                    ans.append(matrix[i][j])
                    i +=1 # i increases from up to down
                i -=1 # To get within bounds 
                j -=1 # To move left
                DOWN_WALL -=1
                direction = LEFT
                

            elif direction == LEFT:
                print('direction ',direction,len(ans))
                while (j> LEFT_WALL):
                    ans.append(matrix[i][j])
                    j -=1 # i decreases from right to left
                i -=1 # To move up 
                j +=1 # To get within bounds
                LEFT_WALL +=1
                direction = UP
                

            elif direction == UP:
                print('direction ',direction,len(ans))
                while (i> UP_WALL):
                    ans.append(matrix[i][j])
                    i -=1 # i decreases from bottom to top
                i +=1 # To get within bounds
                j +=1 # To move right
                UP_WALL +=1
                direction = RIGHT
                
        
        return ans