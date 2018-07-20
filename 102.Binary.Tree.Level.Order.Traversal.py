# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def go(root, depth, ret):
            if root is None:
                return
            if depth >= len(ret):
                ret.append([root.val])
            else:
                ret[depth].append(root.val)
            go(root.left, depth + 1, ret)
            go(root.right, depth + 1, ret)
        
        ret = []
        go(root, 0, ret)
        return ret
                