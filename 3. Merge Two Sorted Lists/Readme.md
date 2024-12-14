# Key Concept: Shared References in Python

- **Shared References:**
  - Both `dummy` and `current` initially reference the same `ListNode` object: `dummy = ListNode()` and `current = dummy`.
  - In Python, variables like `dummy` and `current` don't store the actual `ListNode` objects; instead, they store references to those objects.
  - As a result, any modification to the object via `current` (such as setting `current.next`) also affects the object referenced by `dummy`.

## Why `dummy.next` Updates Correctly

### Shared Reference at Start:
- `dummy` and `current` point to the same node when they are initialized. 
- If you set `current.next = some_node`, this operation modifies the same object that `dummy` points to.

### Updating `current` Does Not Break the Connection:
- When you update `current` (`current = current.next`), you are only changing what `current` points to; the link between `dummy` and the rest of the list remains intact.
- Specifically:
  - `current` now references the next node.
  - The `dummy` node's `next` pointer still references the correct start of the merged list.

# Explanation of the Code

## Dummy Node
- A **dummy node** is used to simplify the process of appending nodes to the merged list.
- The actual merged list starts from `dummy.next`.

## Iterate Through the Lists
- The `while list1 and list2` loop ensures you only compare and append nodes when both lists have elements left.

## Handle Remaining Nodes
- After exiting the loop, one of the lists may still have nodes. These are directly appended to the merged list.

## Return the Merged List
- Return `dummy.next` to skip the dummy node and get the head of the merged list.

---

# Possible Issues

### If you give - `list1.val != None` and `list2.val != None`
- This condition will cause an **AttributeError** if either `list1` or `list2` is `None`, because `None` does not have a `val` attribute.
- **Solution:** 
  - Check if `list1` or `list2` is `None` before accessing `val`.


