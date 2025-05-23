#  Time Complexity : O(1)
#  Space Complexity : O(n) n=> number of elements added
#  Did this code successfully run on Leetcode : Yes
#  Any problem you faced while coding this : I was using a variable to store min values first and was not able to come up with a solution to use an array


#  Your code here along with comments explaining your approach
class MinStack(object):

    def __init__(self):
        self.stack = []
        # Using arr to update when current min is removed
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val,self.min_stack[-1]))
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]