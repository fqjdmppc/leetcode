class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        f = [True] + [False] * len(s)
        for i in range(len(s) + 1):
            if f[i]:
                for _ in wordDict:
                    if i + len(_) <= len(s):
                        # print(i, _, i + 1 + len(_), s[i: i + len(_)])
                        f[i + len(_)] = (f[i + len(_)] or (s[i: i + len(_)] == _))
                # print(i, f)
        return f[-1]