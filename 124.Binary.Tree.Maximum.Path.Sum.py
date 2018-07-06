# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def find(root,arg):
            if id(root) in arg[0]:
                return arg[0][id(root)]
            if root is None:
                return float('-inf')
            else:
                ret = max(find(root.left,arg), find(root.right,arg), 0) + root.val
                arg[1] = max(arg[1], find(root.left,arg) + root.val + find(root.right,arg), ret)
                arg[0][id(root)] = ret
                return ret
        arg = [dict(), float('-inf')]
        find(root,arg)
        
        return arg[1]
        