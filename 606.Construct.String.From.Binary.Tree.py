class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def search(t):
            if t.left is None and t.right is None:
                return str(t.val)
            elif t.right is None:
                return str(t.val) + "(" + search(t.left) + ")"
            elif t.left is None:
                return str(t.val) + "()(" + search(t.right) + ")"
            else:
                return str(t.val) + "(" + search(t.left) + ")(" + search(t.right) + ")"
        
        if not t:
            return ""
        else:
            return search(t)