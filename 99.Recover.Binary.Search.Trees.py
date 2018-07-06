# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def check_result(cur, ret, p, para):
            if len(ret) >= 2:
                return 
            
            if len(cur) < 2:
                cur.append(p)
                if len(cur) < 2:
                    return
            else:
                cur[0], cur[1] = cur[1], p
            
            if len(ret) == 0 and cur[0].val > cur[1].val:
                para[0] = cur[1]
                ret.append(cur[0])
                cur.remove(cur[0])
            elif len(ret) == 1 and cur[1].val < cur[0].val:
                ret.append(cur[1])
                cur.remove(cur[1])
            
        cur = root
        ret = []
        check_cur = []
        para = [1]
        while cur is not None:
            if cur.left is not None:
                # find right-most child
                p = cur.left
                while p.right is not None and p.right != cur:
                    p = p.right
                if p.right == cur:
                    check_result(check_cur, ret, cur, para)
                    p.right = None
                    cur = cur.right
                else:
                    p.right = cur
                    cur = cur.left
            else:
                check_result(check_cur, ret, cur, para)
                cur = cur.right
        
        if len(ret) == 1:
            ret[0].val, para[0].val = para[0].val, ret[0].val
        else:
            ret[0].val, ret[1].val = ret[1].val, ret[0].val
        