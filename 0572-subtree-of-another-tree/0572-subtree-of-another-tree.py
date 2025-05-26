# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(root1,root2):
            if root1 == None and root2==None:
                return True
            if  root1 ==None or root2 == None:
                return False
            if root1.val!=root2.val:
                return False
            return sameTree(root1.left,root2.left) and sameTree(root1.right,root2.right) 
        
        if root == None:
            return False
        if sameTree(root,subRoot):
            return True
            
        left = self.isSubtree(root.left,subRoot)
        right =  self.isSubtree(root.right,subRoot)
        
        return left or right







        