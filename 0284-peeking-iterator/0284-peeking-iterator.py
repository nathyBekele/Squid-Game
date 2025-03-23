# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.nums = iterator

        copy_iterator = deepcopy(iterator)
        self.list_nums = []

        while copy_iterator.hasNext():
            self.list_nums.append(copy_iterator.next())

        # print(self.list_nums)
        self.curr = -1

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.list_nums[self.curr + 1]
        

    def next(self):
        """
        :rtype: int
        """
        self.curr += 1
        return self.nums.next()
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.nums.hasNext()

        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].