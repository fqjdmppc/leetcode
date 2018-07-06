class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def nlr(root):
            if root == None: return tuple()
            else: return (root.val, ) + nlr(root.left) + nlr(root.right)
            
        def lnr(root):
            if root == None: return tuple()
            else: return nlr(root.left) + (root.val, ) + nlr(root.right)
        
        def f(root, t1, t2):
            if root == None:
                return False
            elif root.val == t1[0] and nlr(root) == t1 and lnr(root) == t2:
                return True
            else:
                return f(root.left, t1, t2) or f(root.right, t1, t2)
        
        return f(s, nlr(t), lnr(t))
        
        