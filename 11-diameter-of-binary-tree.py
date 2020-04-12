# The diameter of a tree T is the largest of the following quantities:

# * the diameter of T’s left subtree
# * the diameter of T’s right subtree
# * the longest path between leaves that goes through the root of T 
# (this can be computed from the heights of the subtrees of T)

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def height(root, ret=0):
            if not root:
                return ret
            else:
                return max(height(root.left, ret+1), height(root.right, ret+1))

        d_left = 0
        d_right = 0
        longest_path = 0
        
        if root:
            lh = height(root.left)
            rh = height(root.right)
            longest_path = lh + rh
        
            if root.left:
                d_left = self.diameterOfBinaryTree(root.left)
        
            if root.right:
                d_right = self.diameterOfBinaryTree(root.right)
        
        return max(d_left, d_right, longest_path)
        
        
# 106 / 106 test cases passed.
# Status: Accepted
# Runtime: 744 ms
# Memory Usage: 16.4 MB
