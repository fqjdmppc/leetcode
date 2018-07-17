class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {'2':'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        def go(depth, cur, ret):
            if depth == len(digits):
                if cur: ret.append(cur)
            elif digits[depth] in d:
                for _ in d[digits[depth]]:
                    go(depth + 1, cur + _, ret)
        
        ret = []
        go(0, '', ret)
        return ret
            