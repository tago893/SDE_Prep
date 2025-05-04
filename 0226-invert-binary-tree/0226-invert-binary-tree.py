# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return
        right_tree=self.invertTree(root.right)
        left_tree=self.invertTree(root.left)
        root.left = right_tree
        root.right = left_tree
        return root