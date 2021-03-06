"""
https://leetcode.com/problems/linked-list-cycle-ii/
LC142 Linked List Cycle II
Medium

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.
"""

from typing import *
from A01_ListNode import *


class Solution_A:

    def detectCycle(self, head: ListNode) -> ListNode:
        """
        Time O(N), Space O(N), use set to search existing node
        ListNode instance is hashable, this method search at O(1), and will not break down the original linked list
        """
        ss = set()
        while head:
            if head.next in ss:
                return head.next
            else:
                ss.add(head)
                head = head.next
        return None


if __name__ == "__main__":
    # Use is instead of == to avoid max recursion when comparing cycling linked list
    testCase = Solution_A()

    L1 = genNode([3, 2, 0, 4])
    L1.next.next.next.next = L1.next
    # 3 2 0 4
    # a b c d
    # d->b
    assert testCase.detectCycle(L1) is L1.next, "Example 1"

    L2 = genNode([1, 2])
    L2.next.next = L2
    # 1 2
    # a b
    # b->a
    assert testCase.detectCycle(L2) is L2, "Example 2"

    L3 = genNode([1])
    assert not testCase.detectCycle(L3), "Edge 1, no cycle"

    print("All passed")
