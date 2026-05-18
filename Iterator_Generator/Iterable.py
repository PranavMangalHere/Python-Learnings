## iterator is an object with the state so that it remembers where it is during iteration
## you can only go forward using iterator
# nums = [1,2,3]

# # for num in nums:
# #     print(num)
    
# i_nums = nums.__iter__()

# # print(i_nums)

# # print(next(i_nums))
# # print(next(i_nums))
# # print(next(i_nums))
# # print(next(i_nums)) 

# # while True:
# #     try:
# #         item = next(i_nums)
# #         print(item)
# #     except StopIteration:
# #         break

# class MyRange:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
        
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if(self.start >= self.end):
#             raise StopIteration
#         current = self.start
#         return current
    
# ##  GENERATORS____________

# def my_range(start):
#     current = start
#     while True:
#         yield current
#         current += 1
    

    
    
# nums = my_range(1)

# for num in nums:
#     print(nums) 

class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence 
        self.index = 0
        self.words = self.sentence.split()
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index 
        self.index += 1
        return self.words[index]
            
my_sentence = Sentence("this is a test")

for word in my_sentence:
    print(word)