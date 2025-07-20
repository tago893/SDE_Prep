# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = [root.val]
        def helper(root):
            if root == None:
                return 0
            lt = max(helper(root.left),0)
            rt = max(helper(root.right),0)
            max_path_sum[0] = max(max_path_sum[0], root.val+lt+rt)
            return root.val + max(lt,rt)
        helper(root)
        return max_path_sum[0]