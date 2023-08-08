class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.m = len(grid)
        self.n = len(grid[0])
        col = range(self.n)
        output = 0

        # Option 2 - change the land to 0, which is water
        def changeTheLand(neighbors):
            for x, y in neighbors:
                if x == -1 or x == self.m or y == -1 or y == self.n:
                    continue 
                elif grid[x][y] == '1':
                    grid[x][y] = '0'
                    changeTheLand([(x-1, y), (x, y-1), (x, y+1), (x+1, y)])

        for x in range(self.m):
            for y in col:
                if grid[x][y] == '1':
                    grid[x][y] = '0'
                    changeTheLand([(x-1, y), (x, y-1), (x, y+1), (x+1, y)])
                    output += 1
                
        return output

        # Option 1 - marking the land, then skip if the index have been marked
        """
        def markTheLand(neighbors):
            for x, y in neighbors:
                if x == -1 or x == self.m or y == -1 or y == self.n or (x,y) in self.new_map:
                    continue 
                elif grid[x][y] == '1':
                    self.new_map.add((x, y))
                    markTheLand([(x-1, y), (x, y-1), (x, y+1), (x+1, y)])

        self.new_map = set()

        for x in range(self.m):
            for y in col:
                if (x, y) not in self.new_map and grid[x][y] == '1':
                    self.new_map.add((x, y))
                    markTheLand([(x-1, y), (x, y-1), (x, y+1), (x+1, y)])
                    output += 1
                
        return output
        """
