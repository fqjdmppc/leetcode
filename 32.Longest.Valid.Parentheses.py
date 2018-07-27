class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1: 
            return 0
        else:
            ret = 0
            f = [0] * len(s)
            for i in range(1, len(s)):
                if s[i] == '(':
                    f[i] = 0
                elif i - f[i - 1] - 1 >= 0 and s[i - f[i - 1] - 1] == '(':
                    f[i] = f[i - 1] + 2 + (0 if i - f[i - 1] - 2 < 0 else f[i - f[i - 1] - 2])
                else:
                    f[i] = 0
                ret = max(ret, f[i])
                # print(f)
        return ret
                