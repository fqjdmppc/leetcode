class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        q = set()
        ret = 0
        for _ in s:
            if _ not in q:
                q.add(_)
            else:
                while _ in q:
                    q.remove(s[left])
                    left += 1
                q.add(_)
            ret = max(ret, len(q))
        return ret