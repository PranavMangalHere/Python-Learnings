"""
Iteration is a general term for taking each item of soething, one after another.Any time you use a loop, explicit or 
implicit to go over a group of items that is iteration 
"""

# # Example -- ITERATOR 
# from collections import namedtuple
# from typing import Iterator

# Page = namedtuple("Page", ["text", "number"])

# class Book:
    
#     def __init__(self) -> None:
#         self.pages = []
#     def add_page(self, text: str) -> None:
#         self.pages.append(Page(text, number=len(self.pages) + 1))
#     def __iter__(self):
#         return BookIter(self)
    
# class BookIter:
#     def __init__(self, book:Book):
#         self.pages = book.pages
#         self.book = book
#         self._cursor = 0 
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if len(self.pages) > self._cursor:
#             result = self.pages[self._cursor]
#             self._cursor += 1
#             return result
#         raise StopIteration

# book = Book() 
# for i in range(1, 5): 
#     book.add_page(f"page_{i}") 
# for page in book: 
#     print(page) 



# Same Example using GENERATOR
from collections import namedtuple
from typing import Iterator

Page = namedtuple("Page", ["text", "number"])

class Book:
    
    def __init__(self) -> None:
        self.pages = []
    def add_page(self, text: str) -> None:
        self.pages.append(Page(text, number=len(self.pages) + 1))
    def __iter__(self):
        for page in self.pages:
            yield page

book = Book()
for i in range(1, 5):
    book.add_page(f"page_{i}")

for page in book:
    print(page)
    
""" 
✔ Same output
✔ Much less code
✔ No explicit __next__()
✔ No manual cursor handling
"""

"""What yield is secretly doing
When Python sees yield
It creates an iterator object automatically
Maintains execution state (cursor, local variables)
Raises StopIteration automatically when finished"""

#   --------- Why BookIter is reusable but generators are not  ---------

# 🔁 BookIter is reusable (multi-pass iterator)
# Each time you iterate:  ((for page in book: ))
# This happens:
# Book.__iter__() → returns a NEW BookIter object
# Each BookIter has:
#  ->Its own _cursor = 0
#  ->Fresh iteration state
# So you can do this safely:

# for p in book:
#     print(p)
# for p in book:
#     print(p)   # works again
"""Because:
✔ New iterator instance
✔ Cursor resets"""


# ___ BUT In Generator Case ____

# ⚠️ Generators are NOT reusable (single-pass)
# A generator is the iterator itself, not a factory.
# Example:
# gen = (page for page in book.pages)
# for p in gen:
#     print(p)
# for p in gen:
#     print(p)   # NOTHING prints

# Why?
#  ->Generator keeps internal state
#  ->Once exhausted, it’s dead
#  ->No reset unless recreated


# | Feature         | `BookIter` class        | Generator (`yield`)       |
# | --------------- | ----------------------- | ------------------------- |
# | Code length     | Long                    | Short                     |
# | Cursor handling | Manual                  | Automatic                 |
# | StopIteration   | Manual                  | Automatic                 |
# | Readability     | More complex            | Very clean                |
# | Reusability     | Yes (new instance)      | Yes **only if recreated** |
# | Best for        | Complex iteration logic | Simple linear iteration   |

"""
5️⃣ When NOT to use generators
Avoid generators when:
-You need random access
-You want to pause, reset, or clone iterator state
-Iteration logic is very complex
-You want explicit control over iteration behavior
-In those cases → custom iterator class wins.

6️⃣ Interview-friendly one-liner
Iterators are reusable because __iter__() returns a new iterator each time, 
whereas generators are single-pass objects that get exhausted once unless recreated."""