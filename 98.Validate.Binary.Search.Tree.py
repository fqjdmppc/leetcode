# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def go(root):
            if root is None: return []
            else:
                return go(root.left) + [root.val] + go(root.right)
        
        if not root or root.left == root.right == None: return True 
        a = go(root)
        for q,w in zip(a[:-1], a[1:]):
            if q >= w: return False
        return True
                
                    
                
        