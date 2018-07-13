class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for k in range(n // 2):
                for j in range(n - k - k - 1):
                    r = [[k, k + j], [n - k - j - 1,k], [n - k -1, n - k - j - 1], [k + j, n - k - 1]]
                    matrix[r[0][0]][r[0][1]], matrix[r[1][0]][r[1][1]],matrix[r[2][0]][r[2][1]],matrix[r[3][0]][r[3][1]] = matrix[r[1][0]][r[1][1]],matrix[r[2][0]][r[2][1]], matrix[r[3][0]][r[3][1]], matrix[r[0][0]][r[0][1]]