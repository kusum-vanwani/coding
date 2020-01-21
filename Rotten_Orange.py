from collections import deque
class Solution:


    def orangesRotting(self, grid) :
        r, c = len(grid), len(grid[0])
        qu = deque()
        for r_num in range(r):
            for c_num in range(c):
                if grid[r_num][c_num] == 2:
                    qu.append((r_num,c_num, 0))

        row_neigh = [0, -1, 0, 1]
        col_neigh = [-1, 1]

        d = 0
        while qu:
            curr_r, curr_c, d = qu.popleft()
            for row,col in ((curr_r,curr_c-1),(curr_r, curr_c+1), (curr_r-1,curr_c),(curr_r+1,curr_c)):
                if (row) >= 0 and  (row) < r and  (col) >= 0 and (col) < c :
                    if grid[row][col] == 1:
                        grid[row][col] = 2
                        qu.append((row,col, d+1))

        for rn in range(r):
            if 1 in grid[rn]:
                return -1

        return d


s = Solution()
grid = [[2,1,1],[0,1,1],[1,0,1]]

s.orangesRotting(grid)

grid =  [[2,1,1],[1,1,0],[0,1,1]]
s.orangesRotting(grid)