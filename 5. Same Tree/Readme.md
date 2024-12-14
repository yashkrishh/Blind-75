### Key Points

1. **Logical "and" Operator in Python:**
   - In Python, the correct operator for logical "and" is `and`, not `&&`.

2. **Handling `None` Nodes Properly:**
   - Ensure that cases where only one of the nodes is `None` are handled correctly with the following condition:
     ```python
     if p is None or q is None or p.val != q.val:
         return False
     ```

3. **Time Complexity of `isSameTree`:**
   - The time complexity of the `isSameTree` function is **O(n)**, where \( n \) is the total number of nodes in the smaller of the two trees (\( p \) and \( q \)).
   - This is because the algorithm performs a **depth-first traversal** of both trees simultaneously.
