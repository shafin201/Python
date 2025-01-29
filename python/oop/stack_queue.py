#Stack
book = []
book.append("Learn C")
book.append("Learn C++")
book.append("Learn Python")
book.append("Learn Java")
book.append("Learn PHP")
print("\n")
print(book)
book.pop()
print(book)
print("\n")
print("Now the top book is:",book[-1])
print("\n")
#Queue

from collections import deque

bank = deque(["Mithun","Shafin","Nirob"])
print(bank)
bank.popleft()
print(bank)
print("Now the top bank is:",bank[0])
