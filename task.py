# # Sorting a numeric list--->
# l=[13,1,25,40,130,135,55,57,90]
# def bubble_sort(x):
#     for i in range(len(l)):
#         for j in range(len(l)-1-i):
#             if l[j] > l[j+1]:
#                 l[j],l[j+1]=l[j+1],l[j]
#     return x

# print(bubble_sort(l))

# remove the last object from a list in python---->
# l=['a','b','c','d','e']
# l.pop()
# print(l)

# what does [::-1} do?--->
# l=[1,2,3,4,5]
# print(l[::-1}) --->SyntaxError: invalid syntax


# map() function----->
# (function, iteretion)--->
# We can double all numbers using map() --->
# def addition(x):
#     return x + x
# num = (1, 2, 3, 4) 
# res = map(addition, num) 
# print(list(res))

# count the number of capital letters in a file--->
# string=input("Enter string:")
# count=0
# for i in string:
#     if i.isupper():
#         count += 1
# print(f"The number of uppercase characters is:{count}")

