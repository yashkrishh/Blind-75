# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are None, the trees are the same
        if p is None and q is None:
            return True
        # If one is None or the values are different, the trees are not the same
        if p is None or q is None or p.val != q.val:
            return False
        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Main function to test the Solution
def main():
    # Create test trees
    tree1 = TreeNode(1, TreeNode(2), TreeNode(3))  # Tree 1:    1
                                                   #           / \
                                                   #          2   3
    tree2 = TreeNode(1, TreeNode(2), TreeNode(3))  # Tree 2:    1
                                                   #           / \
                                                   #          2   3
    tree3 = TreeNode(1, TreeNode(2), TreeNode(4))  # Tree 3:    1
                                                   #           / \
                                                   #          2   4

    # Check if trees are the same
    solution = Solution()
    print("Tree 1 and Tree 2 are the same:", solution.isSameTree(tree1, tree2))  # Output: True
    print("Tree 1 and Tree 3 are the same:", solution.isSameTree(tree1, tree3))  # Output: False

if __name__ == "__main__":
    main()
