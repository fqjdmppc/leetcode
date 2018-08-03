# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        else:
            r = TreeNode(preorder[0])
            x = inorder.index(preorder[0])
            r.left = self.buildTree(preorder[1: 1 + x], inorder[: x])
            r.right = self.buildTree(preorder[1 + x: ], inorder[x + 1:])
            return r