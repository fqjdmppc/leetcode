class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = len(s)
        flag = [[False] * len(s) for _ in s]
        for _ in range(len(s)):
            flag[_][_] = True
        for j in range(1, len(s)):
            for i in range(len(s)):
                if i + j < len(s) and s[i] == s[i + j] and (j == 1 or flag[i + 1][i + j - 1]):
                    ret += 1
                    flag[i][i + j] = True
        return ret
        