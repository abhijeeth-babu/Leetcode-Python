class Solution:
    def isValidSerialization(self, preorder):
        nodes = preorder.split(",")
        spots = 1

        for node in nodes:
            spots -= 1

            if spots < 0:
                return False

            if node != "#":
                spots += 2

        return spots == 0
