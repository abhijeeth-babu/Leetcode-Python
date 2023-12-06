import random 


class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.map = {}


    def insert(self, val):
        if val not in self.map:
            self.arr.append(val)
            self.map[val] = len(self.arr) - 1
            return True
        return False

    def remove(self, val):
        if val not in self.map or not self.arr:
            return False
        idx_to_remove = self.map[val]
        last_elem = self.arr[-1]
        self.map[last_elem] = idx_to_remove
        # delete after insertion into map to make sure for the edge case of only 1 element 
        del self.map[val]
        self.arr[idx_to_remove], self.arr[-1] = self.arr[-1], self.arr[idx_to_remove]
        self.arr.pop()
        return True
        

    def getRandom(self):
        rand_idx = random.randrange(len(self.arr))
        return self.arr[rand_idx]

