class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False

        if sum == root.val and root.left == None and root.right == None:
            return True

        l = self.hasPathSum(root.left, sum - root.val)
        r = self.hasPathSum(root.right, sum - root.val)

        return l or r
