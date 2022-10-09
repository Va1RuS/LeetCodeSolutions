# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        def dfs(node):
            if node:
                if node.val in seen:
                    return True
                seen.add(k - node.val)
                return dfs(node.left) or dfs(node.right)
        return dfs(root)