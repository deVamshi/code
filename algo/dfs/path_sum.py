# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Do a dfs search on the tree and keep adding the current node val
# Inorder traversal

class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        
        def dfs(node, curSum):
            if not node: return False
            curSum += node.val
            if not node.left and not node.right:
                return curSum == targetSum
            return (dfs(node.left, curSum) or dfs(node.right, curSum))
        
        return dfs(root, 0)
        