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
            left = max(solve(root.left),0)
            right = max(solve(root.right),0)
            max_path_sum=max(max_path_sum,root.val + left + right)
            return root.val + max(left,right)
        solve(root)
        return max_path_sum