# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def solve(root,curr):
            if root == None:
                return 0
            
            curr = curr*10+root.val
            if root.left == None and root.right == None: 
                return curr
            return solve(root.left,curr) + solve(root.right,curr)
       
        
        return solve(root,0)