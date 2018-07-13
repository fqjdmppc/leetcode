class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        n,m = len(matrix), len(matrix[0])
        flag = (m > n)
        limitr = (m if flag else n)- 1
        for i in range(n if flag else m):
            l, r = 0, limitr
            while l < r:
                q = (l + r) // 2
                if (matrix[i][q] if flag else matrix[q][i]) < target:
                    l = q + 1
                else:
                    r = q      
            if (matrix[i][l] if flag else matrix[l][i]) == target: return True
            else: limitr = min(limitr, l + 1)
            # print(l)
                
        return False
                
                    