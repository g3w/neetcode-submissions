# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []


        q = []
        res = []

        cur_level = 0
        q.append(root)

        while q:
            lenq = len(q)
            res.append([])

            for _ in range(lenq):
                node = q.pop(0)
                res[cur_level].append(node.val)

                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)
            cur_level += 1

        return res

                
