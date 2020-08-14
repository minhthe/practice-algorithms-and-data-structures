'''https://leetcode.com/problems/invert-binary-tree/'''
class Solution:
	def invertTree(self, root: TreeNode) -> TreeNode:
		if root is None: return root
		root.left , root.right = self.invertTree(root.right), self.invertTree(root.left)
		return root