# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def go(root, ret):
            if not root: return 0
            else:
                x, y = go(root.left, ret), go(root.right, ret)
                ret[0] = max(ret[0],x + y + 1)
                return max(x, y) + 1
            
        ret = [1]
        go(root, ret)
        return ret[0] - 1