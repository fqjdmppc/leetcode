# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def go(root, ret):
            if not root: return 
            x = [0,0]
            left, right = root.left, root.right
            cur = root
            root.left = root.right = None
            if left is not None:
                go(left, x)
                cur.right = x[0]
                cur = x[1]
            if right is not None:
                go(right, x)
                cur.right = x[0]
                cur = x[1]
            cur.left = cur.right = None
            ret[0] = root
            ret[1] = cur
            
        go(root, [0, 0])
                