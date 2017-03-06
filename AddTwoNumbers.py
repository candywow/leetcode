# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = l1
        head = l
        while True:
            l.val += l2.val
            if l.val > 9:
                l.val = l.val - 10
                if l.next == None:
                    l.next = ListNode(0)
                self.addTwoNumbers(l.next, ListNode(1))

            if l2.next == None:
                return head
            elif l.next == None:
                l.next = l2.next
                return head
            else:
                l = l.next
                l2 = l2.next
