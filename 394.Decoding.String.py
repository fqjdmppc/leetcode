class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = ['[']
        for _ in s:
            if _ == '[':
                l.append('[')
            elif _ == ']':
                rep = ''
                while l[-2] and l[-2][-1].isdigit():
                    rep = l[-2][-1] + rep
                    l[-2] = l[-2][:-1]
                l[-2] += (l[-1][1:] * int(rep))
                l.pop()
            else:
                l[-1] += _
        return l[0][1:]