class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        while temp:
            if temp.next and temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        
        return dummy.next