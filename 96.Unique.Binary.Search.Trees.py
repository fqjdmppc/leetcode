class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # f(n) = sigma(f(i)*f(n-i))
        f = [1, 1, 2]
        for i in range(3, n + 1):
            f.append(0)
            for j in range(i):
                f[-1] += f[j] * f[i - j - 1]       
        return f[n]