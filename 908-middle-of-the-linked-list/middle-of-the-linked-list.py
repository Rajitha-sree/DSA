# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # n=0
        # head1 = head
        # while head1!=None:
        #     n+=1
        #     head1 = head1.next
        # if n% 2 == 0:
        #     n = n//2
        #     n = n
        # else:
        #     n = n//2
        # temp = head
        # while n>0:
        #     temp = temp.next
        #     n-=1

        # return temp
        slow = head
        fast = head
        while fast!=None and fast.next!=None:
            slow =  slow.next
            fast = fast.next.next

        return slow