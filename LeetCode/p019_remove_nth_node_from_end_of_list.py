# P019 Remove Nth Node From End of List
# Medium


# Given a linked list, remove the n-th node from the end of list and return its head.
# Note:
# Given n will always be valid.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    ### 笨办法,先判断链表长度, 再正向解决
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur, length = head, 0
        while cur:
            length += 1
            cur = cur.next

        p_length = length-n
        if p_length == 0:
            return head.next
        else:
            curr = head
            while p_length > 1:
                curr = curr.next
                p_length -= 1

            curr.next = curr.next.next
            return head

class Solution(object):
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy

        for i in range(n):
            fast = fast.next

        while fast.next:
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next

        return dummy.next

    # D-1-2-3-4-5-N
    # s   f          // 先定位s和f

    # D-1-2-3-4-5-N
    #       s   f  // 一起移动s和f直到f.next碰到末尾

    # 为什么要设置dummy?
    # D-1-2-3-4-5-N
    # s         f     // # 不设置dummy的话无法应对跳过head的情况


if __name__ == '__main__':
    # Given linked list: 1->2->3->4->5, and n = 2
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    # becomes 1->2->3->5
    f = Solution().removeNthFromEnd(a, 2)
    assert f.val == 1
    assert f.next.val == 2
    assert f.next.next.val == 3
    assert f.next.next.next.val == 5
    assert not f.next.next.next.next

    a = ListNode(1)
    f = Solution().removeNthFromEnd(a, 1)
    assert not f

    print('all passed')
