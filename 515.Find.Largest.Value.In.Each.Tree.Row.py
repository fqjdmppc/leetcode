# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        mm = dict()
        def search(root, deep):
            if root is None:
                return
            elif deep not in mm:
                mm[deep] = root.val
            elif mm[deep] < root.val:
                mm[deep] = root.val
            
            search(root.left, deep + 1)
            search(root.right, deep + 1)
        
        if (root is None):
            return []
        else:
            search(root, 0)
        ret = []
        for _ in range(1 + max(mm.keys())):
            ret.append(mm[_])
            
        return ret