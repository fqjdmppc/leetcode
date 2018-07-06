class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        import copy
        s = []
        def ga(i, j):
            if i < 0 or j < 0: return 0
            else: return s[i][j]
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        if len(matrix) == 1 or len(matrix[0]) == 1:
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == '1':
                        return 1
            return 0
        lx, ly = len(matrix[0]), len(matrix)
        s = [([0] * lx) for _ in range(ly)]
        m = copy.deepcopy(s)
        mm = 0
        for i in range(0, ly):
            for j in range(0, lx):
                s[i][j] = ga(i - 1, j) + ga(i , j - 1) - ga(i - 1,j - 1) + ord(matrix[i][j]) - 48
                if (i == 0 or j == 0) and matrix[i][j] == '1':
                    m[i][j] = 1
                    mm = 1
        
        for i in range(1, ly):
            for j in range(1, lx):
                if (matrix[i][j] == '1'):
                    x = min(m[i - 1][j], m[i][j - 1])
                    m[i][j] = x + (not(s[i][j] - ga(i - x - 1, j)- ga(i, j - x - 1) + ga(i - x - 1, j - x - 1) != (x + 1) ** 2))
                    if m[i][j] > mm:
                        mm = m[i][j]
                        
                        
                        
        return mm ** 2