# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # We pick complete left sub tree
        root.left = self.invertTree(root.left)
        # We pick complete right sub tree
        root.right = self.invertTree(root.right)
        # then we swap the complete sub trees 
        # we perform this for each sub tree node
        root.left , root.right = root.right, root.left

        return root














