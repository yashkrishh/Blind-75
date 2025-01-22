# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # Base case: if the current node is null, return 0
        
        # Recursively find the depth of the left and right subtrees
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        
        # Return the height of the current node as 1 + max(left, right)
        return 1 + max(left_height, right_height)

# Example usage
if __name__ == "__main__":
    # Construct a sample tree
    #         3
    #        / \\
    #       9  20
    #          /  \\
    #         15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    # Calculate max depth
    solution = Solution()
    print("Maximum Depth of the Tree:", solution.maxDepth(root))
