# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        # Traverse the list with two pointers
        while fast is not None and fast.next is not None:
            slow = slow.next           # Move slow pointer one step
            fast = fast.next.next      # Move fast pointer two steps
            if slow == fast:           # If they meet, a cycle exists
                return True
        return False                   # If traversal ends, no cycle exists

# Function to test the solution
def main():
    # Create a linked list with a cycle
    head = ListNode(3)
    second = ListNode(2)
    third = ListNode(0)
    fourth = ListNode(-4)
    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = second  # Creates a cycle back to the second node

    # Create a linked list without a cycle
    head_no_cycle = ListNode(1)
    head_no_cycle.next = ListNode(2)

    solution = Solution()

    # Test the lists
    print("Cycle in first list:", solution.hasCycle(head))            # Output: True
    print("Cycle in second list:", solution.hasCycle(head_no_cycle))  # Output: False

if __name__ == "__main__":
    main()
