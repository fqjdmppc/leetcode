class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n, m = len(word1), len(word2)
        if n == 0 or m == 0:
            return max(n, m)
        f = [[_ for _ in range(m + 1)], [0] * (m + 1)]
        for i in range(1, n + 1):
            f[1][0] = i
            for j in range(1, m + 1):
                f[1][j] = min(f[0][j] + 1, f[1][j - 1] + 1, f[0][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1))
            # print(f)
            f[0] = f[1].copy()
            
        return f[0][-1]