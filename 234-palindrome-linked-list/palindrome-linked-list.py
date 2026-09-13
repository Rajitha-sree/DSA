# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow = head
        fast = head
        flag = 0
        while(fast!=None and fast.next!=None):
            slow = slow.next
            fast = fast.next.next
            
        curr = slow
        prev = None
        while curr:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n

        
        l = head
        start = prev
        while start:
            if start.val == l.val:
                start=start.next
                l = l.next

            else:
                flag = 1
                break

        if flag==1:
            return False
        else:
            return True

        
        