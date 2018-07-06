class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def do(s, i, ret):
            if i >= len(s):
                ret[0].append(s)
            elif 'z' >= s[i].lower() >= 'a':
                do(s[0: i] + s[i].lower() + s[i + 1:], i + 1, ret)
                do(s[0: i] + s[i].upper() + s[i + 1:], i + 1, ret)
            else:
                do(s, i + 1, ret)
        
        r = [[]]
        do(S, 0, r)
        return r[0]