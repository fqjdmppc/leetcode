# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def go(root, greater_sum):
            if not root:
                return 0
            else:
                r = go(root.right, greater_sum)
                root.val += (r or greater_sum)
                ret = root.val if not root.left else go(root.left, root.val)
                # print(root.val, greater_sum, r, ret)
                return ret
        
        go(root, 0)
        return root