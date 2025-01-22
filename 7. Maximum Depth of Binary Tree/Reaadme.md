### Explanation

#### Recursive Traversal:
- The `maxDepth` function is called recursively for each node's left and right children.
- At each node, the function computes the depth of the left subtree (`left_height`) and the right subtree (`right_height`).

#### Base Case:
- If the node is `None` (i.e., the end of a branch), the function returns `0`, signifying that an empty tree has a depth of `0`.

#### Combination Step:
- For each node, the depth is calculated as: 1 + max(left_height, right_height).
- The `+1` accounts for the current node's level, while the `max` ensures that the deeper subtree determines the total depth.

#### Why It Works:
- The algorithm works by dividing the problem into smaller subproblems (finding the depth of the left and right subtrees) and combining the results.
- This divide-and-conquer strategy ensures that:
- Every node is visited exactly once.
- The solution is efficient, with a time complexity of **O(n)**, where `n` is the number of nodes in the tree.
