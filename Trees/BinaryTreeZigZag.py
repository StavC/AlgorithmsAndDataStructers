# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        self.helper(root, 0, levels)
        return levels

    def helper(self, node, level, levels):

        if len(levels) == level:
            levels.append([])

        if level % 2 == 1:
            levels[level].append(node.val)
        else:
            levels[level].insert(0, node.val)

        if node.right:
            self.helper(node.right, level + 1, levels)

        if node.left:
            self.helper(node.left, level + 1, levels)
