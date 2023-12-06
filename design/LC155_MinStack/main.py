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

# alternatice solution

# class MinStack:

#     def __init__(self):
#         self.st = []
#         self.min_st = []
        

#     def push(self, val: int) -> None:
#         self.st.append(val)
#         if not self.min_st:
#             self.min_st.append(val)
#         else:
#             self.min_st.append(min(self.min_st[-1], self.st[-1]))
        

#     def pop(self) -> None:
#         self.min_st.pop()
#         return self.st.pop()

#     def top(self) -> int:
#         return self.st[-1]
        

#     def getMin(self) -> int:
#         return self.min_st[-1]
