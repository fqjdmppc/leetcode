class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def trans(x):
            ret = '('
            for i in range(1, len(x)):
                ret += '(' if x[i] > x[i-1] else ')'
            return ret
        
        def gen(cur, depth, result):
            if depth == n * 2:
                if cur[-1] == 0:
                    result.append(trans(cur))
            else:
                gen(cur + [cur[-1] + 1], depth + 1, result)
                if cur[-1] > 0:
                    gen(cur + [cur[-1] - 1], depth + 1, result)
            
            
        ret = []
        gen([1], 1, ret)
        return ret