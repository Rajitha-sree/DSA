# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        temp = head
        while fast!=None and fast.next!= None:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                while temp != slow:
                    temp = temp.next
                    slow = slow.next
                return temp


        return None