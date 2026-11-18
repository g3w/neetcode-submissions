# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(node):

            if not node:
                return 0
            

            lheight = height(node.left)
            rheight = height(node.right)
            
            # if subtree already unbalanced
            if lheight == -1 or rheight == -1:
                return -1

            if abs(lheight-rheight) > 1:
                return -1
            return 1 + max(lheight, rheight)

        return height(root) != -1
        