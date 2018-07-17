class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x = [0xffffffff] * len(grid[0])
        x[0] = 0
        for i in range(len(grid)):
            x[0] += grid[i][0]
            for j in range(1, len(x)):
                x[j] = min(x[j - 1], x[j]) + grid[i][j]
        return x[-1]
                