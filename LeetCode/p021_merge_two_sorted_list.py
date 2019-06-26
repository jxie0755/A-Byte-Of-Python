# p021 Merge two sorted list
# Easy

# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.

from typing import *
from a0_TreeNode import *
from a0_ListNode import *


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        current = head

        while l1 is not None or l2 is not None:
            if l1 is None:
                current.next = l2
                l2 = l2.next


            elif l2 is None:
                current.next = l1
                l1 = l1.next


            elif l1.val < l2.val:
                current.next = l1
                l1 = l1.next

            else:
                current.next = l2
                l2 = l2.next

            current = current.next

        return head.next

if __name__ == '__main__':

    l1 = genNode([1,2,4])
    l2 = genNode([1,3,4])

    check = Solution().mergeTwoLists(l1, l2)
    assert repr(check) == '1->1->2->3->4->4'

    print('all passed')
