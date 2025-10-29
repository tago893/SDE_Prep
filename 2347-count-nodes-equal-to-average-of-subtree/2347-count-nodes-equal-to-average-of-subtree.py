# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.final_count = 0
    def count_of_avg_nodes(self,currentNode):
        if currentNode is None:
            return (0,0)
        left = self.count_of_avg_nodes(currentNode.left)
        right = self.count_of_avg_nodes(currentNode.right)
        sum_of_values = currentNode.val+left[0]+right[0]
        no_of_nodes = 1+left[1]+right[1]
        if currentNode.val == (sum_of_values//no_of_nodes):
            self.final_count+=1
        
        return (sum_of_values,no_of_nodes)
        
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count_of_avg_nodes(root)
        return self.final_count
            