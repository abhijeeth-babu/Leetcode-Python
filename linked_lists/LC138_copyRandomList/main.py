class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        temp = head
        # dict that tracks orginal and copy nodes
        d = {}

        # add org as keys and create copy as values
        while temp:
            d[temp] = Node(temp.val, None, None)
            temp = temp.next
        
        # copy.next = value of org.next in dict
        # copy.random = value of org.random in dict
        for org in d.keys():
            d[org].next = d.get(org.next, None)
            d[org].random = d.get(org.random, None)
        
        return d.get(head, None)