# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def go(root, p, q, ret):
            if not root:
                return False
            elif ret:
                return True
            else:
                x = (root.val == p.val or root.val == q.val) + go(root.left, p, q, ret)
                if x == 2:
                    ret.append(root)
                else:
                    x += go(root.right, p, q, ret)
                    if x == 2:
                        ret.append(root)
                return bool(x)
        
        ret = []
        go(root, p, q, ret)
        return ret[0]