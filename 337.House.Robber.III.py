# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        f = dict()
        def tohash(root, flag):
            return str(id(root)) + '+' + str(flag)
        
        def go(root, flag):
            if root is None: return 0
            elif tohash(root, flag) in f:
                return f[tohash(root, flag)]
            elif flag:
                f[tohash(root, flag)] = root.val + go(root.left, False) + go(root.right, False)
                return f[tohash(root, flag)]
            else:
                a1 = max(go(root.left, False), go(root.left, True))
                a2 = max(go(root.right, False), go(root.right, True))
                f[tohash(root, flag)] = a1 + a2
                return f[tohash(root, flag)]
            
        return max(go(root, True), go(root, False))