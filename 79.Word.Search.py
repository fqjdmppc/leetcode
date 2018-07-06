class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(board) == 0 or len(board[0]) == 0:
            return False
        max_x, max_y = len(board), len(board[0])
        
        def dfs(x, y, wi, used):
            if wi >= len(word):
                return True
            for xi, yi in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                xi += x
                yi += y
                if max_x > xi >=0 and max_y > yi >= 0 and (xi, yi) not in used and word[wi] == board[xi][yi]:
                    used.add((xi, yi))
                    if dfs(xi, yi, wi + 1, used):
                        return True
                    else:
                        used.remove((xi, yi))
            return False
        
        for i in range(max_x):
            for j in range(max_y):
                if board[i][j] == word[0]:
                    s = set([(i, j)])
                    if dfs(i, j, 1, s):
                        return True
                    
        return False
        