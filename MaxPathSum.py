# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # This we calculated max path including left and right max path
            res[0] = max(res[0], root.val+leftMax + rightMax)

            # this we return the max path from eitht left and right for the root 's node
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]
