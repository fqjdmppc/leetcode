class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter
        if len(s) != len(t): return False
        else:
            s = Counter(s)
            t = Counter(t)
            for _ in s:
                if s[_] != t[_]:
                    return False
            return True