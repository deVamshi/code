# https://leetcode.com/problems/rotting-oranges/

# We use bfs to solve this issue

class Solution:
    def orangesRotting(self, grid) -> int:
        # Just a check
        if grid == None or len(grid) == 0: return 0
        # To store visited places
        visited = []
        fresh_oranges = 0
        # Changed oranges mean, How many oranges we have rottened
        changed_oranges = 0
        q = []
        m = len(grid)
        n = len(grid[0])
        # This will find the places of all rotten oranges and calculates the total fresh oranges
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    fresh_oranges += 1
                if grid[row][col] == 2:
                    q.append([row, col])
        # if there are no fresh oranges then rotting can happen in o minutes
        if fresh_oranges == 0: return 0
        # if there are fresh oranges but no rotten ones then q will be 
        # empty the it is impossible to do tha
        if len(q) == 0: return -1
        # way to find all the 4 position from a given point
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        minutes = 0
        while len(q) != 0:
            qLength = len(q)
            for i in range(qLength):
                xPos, yPos = q.pop(0)
                for j in range(4):
                    x = xPos + dx[j]
                    y = yPos + dy[j]
                    if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == 2 or grid[x][y] == 0: continue
                    freshOrLoc = [x, y]
                    if freshOrLoc not in visited:
                        # if the location is not visited only then check it
                        # once that is done add it to visited place
                        # everytim you rotten an orange change increase the count
                        q.append(freshOrLoc)
                        visited.append(freshOrLoc)
                        changed_oranges += 1
                    
                
            # if q is not yet empty then it took 1 min to rotten the prev
            # oranges and again we loop
            if len(q) != 0: minutes += 1
        # if fresh oranges count equal the count of oranges that are rotten
        # then we have rottened all oranges so return minutes count
        # else it wasn't possible to rotten all oranges so return -1
        if fresh_oranges == changed_oranges: return minutes
        return -1