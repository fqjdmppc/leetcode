class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if not n or not m: return 0
        elif n == 1 or m == 1: return 1
        f = [1] * m
        for i in range(1, n):
            for j in range(1, m):
                f[j] += f[j - 1]
        return f[-1]
                