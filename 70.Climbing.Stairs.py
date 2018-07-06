class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        elif n == 1: return 1
        else:
            a, b = 1, 2
            for i in range(2, n):
                a, b = b, a + b
        return b
            