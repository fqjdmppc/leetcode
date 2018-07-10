# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == q == None:
            return True
        elif ((p is None or q is None) and (p != q)) or (p.val != q.val): 
            return False
        elif p.left == q.left == None and q.right == p.right == None:
            return True
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            
                