
# class EvenIterator:
#     def __init__(self, limit):
#         self.limit = limit
#         self.start = 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while self.start <= self.limit:
#             val = self.start
#             self.start += 1
#             if val %2 == 0:
#                 return val
#         raise StopIteration

# for i in EvenIterator(10):
#     print(i)

class SlidingWindow:
    def __init__(self, nums, size):
        self.nums = nums
        self.size = size
        self.start = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.start + self.size <= len(self.nums):
            lst = self.nums[self.start: self.start + self.size]
            self.start += 1
            
            return lst
        raise StopIteration

nums = [1, 2, 3, 4, 5]

for window in SlidingWindow(nums, 3):
    print(window)