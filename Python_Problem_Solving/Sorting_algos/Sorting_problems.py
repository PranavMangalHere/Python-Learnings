# Bubble Sort
arr = [8,4,7,6,4,3,2,1]

# for i in range(len(arr)):
#     for j in range(len(arr) - i - 1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]

# print(arr)

# selection sort
arr = [8,4,7,6,4,3,2,1]

# for i in range(len(arr)):
    
#     min = 9999
#     ind = -1
#     for j in range(i+1, len(arr)):
#         if min > arr[j]:
#             min = arr[j]
#             ind = j
        
#     if min < arr[i]:
#         arr[i], arr[ind] = arr[ind], arr[i]

# print(arr)

# from sortedcontainers import SortedSet

# s = {5, 1, 8, 3, 2}

# sorted_s = SortedSet(s)

# print(type(sorted_s))


#  ----------------------------- Inserting Sorting -------------------------

# arr = [5, 3, 4, 1]

# for i in range(1, len(arr)):

#     current = arr[i]
#     j = i - 1
#     print(f"iteration no. {i} and current element {current}")

#     while j >= 0 and arr[j] > current:
#         arr[j + 1] = arr[j]
#         print(f"{arr} and {j}")
#         j -= 1
        
#     arr[j + 1] = current
#     print(f"Current array {arr}")
#     print("------------------------------------")

# print(arr)

# arr = [7,5,4,3,2,1]

# for i in range(1, len(arr)):
#     current = arr[i]
#     j = i-1
#     while j >= 0 and arr[j] > current:
#         arr[j+1] = arr[j]
#         j-=1
    
#     arr[j+1] = current
    
# print(arr)