class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        if not p or len(p) > len(s):
            return []
        else:
            s += '@'
            ret = []
            y = Counter(p)
            x = Counter(s[:len(p)])
            i = len(p)
            while i < len(s):
                if not bool(x - y):
                    ret.append(i - len(p))
                x[s[i - len(p)]] -= 1
                x[s[i]] += 1
                i += 1
            return ret