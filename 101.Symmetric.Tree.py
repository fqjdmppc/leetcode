# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def lr(root):
            if root == None: return (None, )
            else: return (root.val, ) + lr(root.left)+ lr(root.right) 
            
        def rl(root):
            if root == None: return (None, )
            else: return (root.val, ) + rl(root.right) +  rl(root.left)
        
        return True if root == None else lr(root.left) == rl(root.right)