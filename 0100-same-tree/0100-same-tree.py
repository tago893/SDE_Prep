# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root1:Optional[TreeNode], root2:Optional[TreeNode])-> bool:
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        if(root1.val != root2.val):
            return False
        return self.dfs(root1.left,root2.left) and self.dfs(root1.right,root2.right)
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        answer = False
        answer = self.dfs(p,q)
        return answer
