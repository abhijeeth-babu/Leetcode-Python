class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        temp = head
        sz = 0
        while temp:
            sz += 1
            temp = temp.next
        
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        k = sz + 1 - n
        for _ in range(k-1):
            temp = temp.next
        temp.next = temp.next.next
        
        return dummy.next