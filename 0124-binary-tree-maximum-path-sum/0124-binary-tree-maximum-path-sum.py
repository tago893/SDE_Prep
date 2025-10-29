# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float("-inf")
        def solve(root):
            nonlocal max_path_sum
            if root == None:
                return 0
            left = solve(root.left)
            right = solve(root.right)
            max_path_sum=max(max_path_sum,root.val + left + right,root.val,root.val+max(left,right))
            return root.val + max(left,right,0)
        solve(root)
        return max_path_sum