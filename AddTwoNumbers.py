# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = head = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            l.next = ListNode(0)
            l = l.next
            if l1:
                l.val += l1.val
                l1 = l1.next
            if l2:
                l.val += l2.val
                l2 = l2.next
            carry, l.val = divmod(l.val + carry, 10)

        return head.next
