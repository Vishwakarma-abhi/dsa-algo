# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both are null then same structure return True
        if not p and not q:
            return True
        
        # if both are present then first check the values
        if p and q  and p.val == q.val:
            # if yes then check thier left sub treee and right subtree
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

        else:
            return False