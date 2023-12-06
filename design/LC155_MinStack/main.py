class Node:
    
    def __init__(self, val) -> None:
       self.val = val
       self.next = None
       self.min = None


class MinStack:

    def __init__(self):
        self.last = None

    def push(self, x):
        if not self.last:
            self.last = Node(x)
            self.last.min = x
            return
        temp = Node(x)
        temp.min = min(self.last.min, x)
        temp.next = self.last
        self.last =  temp


    def pop(self):
        if not self.last:
            return
        popped = self.last.val
        self.last = self.last.next
        return popped

    def top(self):
        if not self.last:
            return
        return self.last.val
    

    def getMin(self):
        if not self.last:
            return
        return self.last.min
