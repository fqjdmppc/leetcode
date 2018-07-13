class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        x = [0, len(height) - 1]
        y = [1, -1]
        ret = -1
        while x[0] < x[1]:
            ret = max(ret, min(height[x[0]], height[x[1]]) * (x[1] - x[0]))
            flag = height[x[0]] > height[x[1]]
            x[flag] += y[flag]
        
        return ret