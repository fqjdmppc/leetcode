class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'}': '{', ']': '[', ')': '('}
        q = list()
        for _ in s:
            if not q or _ not in d or q[-1] != d[_]:
                q.append(_)
            else:
                q.pop()
        return not bool(q)