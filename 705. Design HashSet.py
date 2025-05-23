#  Time Complexity : O(1)
#  Space Complexity : O(k) k=> number of elements added
#  Did this code successfully run on Leetcode : Yes
#  Any problem you faced while coding this : It was a bit hard to figure out the code in python


#  Your code here along with comments explaining your approach


class MyHashSet(object):

    def __init__(self):
        self.primary_arr = 1000
        self.secondary_arr = 1000
        self.storage = [None] * self.primary_arr # it is assigned with None initially
    def hash1(self,key):
        return key % 1000
    def hash2(self,key):
        return key // 1000


    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        idx1 = self.hash1(key)
        idx2 = self.hash2(key)
        if self.storage[idx1] == None:
            if idx1 == 0:
                self.storage[idx1] = [False] * (self.secondary_arr + 1)
            else:
                self.storage[idx1] = [False] * self.secondary_arr
        self.storage[idx1][idx2] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        idx1 = self.hash1(key)
        idx2 = self.hash2(key)
        if self.storage[idx1] == None:
            return
        self.storage[idx1][idx2] = False
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        idx1 = self.hash1(key)
        idx2 = self.hash2(key)
        if self.storage[idx1] == None:
            return False
        else:
            return self.storage[idx1][idx2]