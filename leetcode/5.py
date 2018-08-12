'''计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0  # 空树
        if root.left != None and root.left.left == None and root.left.right == None:  # 边界，左节点不为空且左节点的左节点以及左节点的右节点为空
            return root.left.val + self.sumOfLeftLeaves(root.right)  # 左节点的值加上右节点的递归
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)  # 递归


