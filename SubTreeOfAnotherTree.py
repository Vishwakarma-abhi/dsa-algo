# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # If there is no subroot then its always true
        if not subRoot:
            return True
        # If there is No Root then its false because kind of no search space
        if not root:
            return False
        
        # Now check for current tree root tree is equivalent with subRoot or not
        if self.sameTree(root,subRoot):
            return True
        
        # if it is not equivalent then cehck in the left subTree and Right Tree 
        # you will find in either of them or in none

        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))

    def sameTree(self,root,subRoot):
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left,subRoot.left) and self.sameTree(root.right,subRoot.right))

        return False
        