class Solution:

    def isValidBST(self,root,lower=float('-inf'),upper=float('inf')):
        if not root:
            return True
        if root.val>=upper or root.val <=lower:
            return False
        return self.isValidBST(root.left,lower,root.val) and self.isValidBST(root.right,root.val,upper)