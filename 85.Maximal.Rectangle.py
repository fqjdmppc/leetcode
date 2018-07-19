import copy
class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        n, m = len(matrix), len(matrix[0])
        flag = True
        if n < m:
            n, m = m, n
            flag = False
            
        x = [[0] * m for _ in range(m)]
        ret = -float('inf')
        for i in range(n):
            for l in range(m):
                if (matrix[i][l] if flag else matrix[l][i]) == '0':
                    x[l] = [-1] * m
                else:
                    for r in range(l, m):
                        if (matrix[i][r] if flag else matrix[r][i]) == '1' and (l == r or x[l][r - 1] >= 0):
                            x[l][r] = 1 if x[l][r] < 0 else (x[l][r] + 1)
                        else:
                            x[l][r] = -1
                        ret = max(ret, (r - l + 1) * x[l][r])
            
        return 0 if ret < 0 else ret
                    
            
        