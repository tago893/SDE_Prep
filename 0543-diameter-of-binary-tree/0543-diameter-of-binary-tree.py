# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def solve(root):
            nonlocal diameter
            if root == None:
                return 0
            left = solve(root.left)
            right = solve(root.right)
            diameter = max(diameter,left+right)
            return max(left,right)+1
        solve(root)
        return diameter