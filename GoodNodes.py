# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            # if node is null there is no good nodes exists so we return 0
            if not node:
                return 0

            # if current node value is >= maxVal tilldate it means the path to that node from root is a goodNode
            res = 1 if node.val >= maxVal else 0
            # we recalculate the max values soFar for the future if any
            maxVal = max(maxVal, node.val)
            # now go and check paths from root ->> current node's left subtree
            res += dfs(node.left, maxVal)
            # Also go and chek paths from root ->> current node's right subtree
            res += dfs(node.right, maxVal)

            # return the final results of total goodNodes/ Paths found
            return res

        return dfs(root, root.val)
