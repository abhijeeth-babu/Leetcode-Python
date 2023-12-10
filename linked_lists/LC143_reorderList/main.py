class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return
        
        slow, fast = head, head

        # find mid 1->2->3->4->5->6 ==> 4 is the mid
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #split and reverse 
        # 1->2->3->4  and 5->6
        head2 = self.reverse_list(slow.next)
        slow.next = None

        # join 
        # 1 to 5 then 5 to 2
        # then move the heads to their initial next values and repeat
        curr1 = head
        curr2 = head2

        while curr2:
            curr1_next = curr1.next
            curr2_next = curr2.next

            curr1.next = curr2
            curr2.next = curr1_next

            curr1 = curr1_next
            curr2 = curr2_next
    
    def reverse_list(self, head):
        if not head or not head.next:
            return head
        new_head = self.reverse_list(head.next)
        head.next.next = head
        head.next = None
        return new_head