# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    moves = 0
    def solve(self,root,moves)->int:
        if root == None:
            return 0
        
        left = self.solve(root.left,moves)
        right = self.solve(root.right,moves)
        self.moves += (abs(left)+abs(right))
        print(moves)

        return (left+right+root.val)-1
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.solve(root,self.moves)
        return self.moves