# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the start of the merged list
        dummy = ListNode()
        current = dummy
        
        # Merge the two lists
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Append the remaining nodes from either list1 or list2
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        
        # Return the merged list starting from the first node after dummy
        return dummy.next

# Helper function to create a linked list from a Python list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Main function to demonstrate the solution
def main():
    # Example 1
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    print("List 1:")
    print_linked_list(list1)
    print("List 2:")
    print_linked_list(list2)
    
    solution = Solution()
    merged_list = solution.mergeTwoLists(list1, list2)
    print("Merged List:")
    print_linked_list(merged_list)
    
    # Example 2
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    print("\nList 1:")
    print_linked_list(list1)
    print("List 2:")
    print_linked_list(list2)
    
    merged_list = solution.mergeTwoLists(list1, list2)
    print("Merged List:")
    print_linked_list(merged_list)

# Run the main function
if __name__ == "__main__":
    main()
