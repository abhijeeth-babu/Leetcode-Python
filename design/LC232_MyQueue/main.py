class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.st = []
        self.helper = []

    def push(self, x):
        """
        Push element x to the back of queue.
        """
        self.st.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        """
        while self.st:
            self.helper.append(self.st.pop())
        popped = self.helper.pop()
        while self.helper:
            self.st.append(self.helper.pop())
        return popped
    

    def peek(self):
        """
        Get the front element.
        """
        return self.st[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        """
        return not self.st
