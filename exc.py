# age=int(input("Enter Your Age :"))
# if age < 18:
#     print("Not Elibible for vote")
# elif age >= 18 and age <= 100:
#     print("You are Eligible for vote")
#     if age >= 50 and age <=100:
#         print("Senior Citigen")

# class Phone:
#     def __init__(self, name, brand):
#         self.name=name
#         self.brand=brand

# class Ph(Phone):
#     def __init__(self, name, brand, Ram):
#         super(). __init__(name,brand)
#         self.Ram=Ram

# p1=Phone(3310,'Nokia')
# print(p1.name)
# p2=Ph(30,'nokia','3gb')
# print(p2.Ram)

# empty_list=[]
# for i in range(1,500):
#     empty_list.append(i)
# new_list=[]
# for j in empty_list:
#     e=str(j)
#     new_list.append(e)
# for k in new_list:
#     if k[::-1]==k:
#         print(k)
#     else:
#         pass


# num1=1.5
# num2=2.5
# s=float(sum(num1,num2))
# print(s)

# def pattern(upto, increaseby):
#     for i in range(0, row_input):
#         print("*" * (row_input-i))

# row_input = int(input('Number of rows: '))
# mf = pattern(row_input, 1)


# y=int(input("Enter a year :"))
# if y%4==0 and y%100!=0 or y%400==0:
#     print(f"Yoy Enter {y} a leap Year!")
# else:
#     print(f"You Enter {y} not a leap year!")

# import datetime
# x=datetime.datetime.now()
# print(x)

# from math import pi
# r=float(input("Enter Redious"))
# s=2*pi*r
# print(s)

# name=input("Enter Name :")
# print(name[-1] + ' '+ name[0])

# f_name= input("Enter First name :")
# l_name=input("Enter last name :")
# print(f'{l_name} {f_name}')

# l=(input("Input a list :")).split(',')
# t=(input("Input a tuple :")).split(',')
# print(list(l))
# print(tuple(t))


# name=input("Enter a filename").split(".")
# print(f"{name[-1]}")

# colors=["Red","Green","White" ,"Black"]
# print(colors[0::3])

# date=11,12,2019
# print('your date id %i/%i/%i'%date)


# n=int(input("enter a number :"))
# n1=int("%s" % n)
# n2=int("%s%s" % (n,n))
# n3=int("%s%s%s" % (n,n,n))
# print(n1+n2+n3)

# import calendar
# y=int(input("Enter Year :"))
# m=int(input("Enter month :"))
# print(calendar.month(y,m))

# from datetime import date
# f_date=date(2019,7,11)
# l_date=date(2020,7,20)
# nunu=l_date-f_date
# print(nunu)

# from math import pi
# r=int(input("Enter Redious :"))
# v=4.0/3.0 * pi * r**3 
# print(f'The Sphere is {v}')

# for i in range(1,100):
#     n=7*i
#     print(n)


#----Parameterized Constructor---->
# class Person:
#     def __init__(self, name, age):
        
#         self.name=name
#         self.age=age

#     def add(self):
#         print(f"your name {self.name} and your age is {self.age}")

# p1=Person('Niladri',20)
# print(p1.name)
# print(p1.age)
# p1.add()


#----Default Constructor----->
# class Student:
#     def __init__(self):
#         print("This is Default Constructor")

#     def add(self,name):
#         print(f'hello {name}')

# s1=Student()
# s1.add('Niladri')


# import pdb
# pdb.set_trace()
# n=int(input("Enter rows :"))
# for i in range(n):
#     for j in range(i+1):
#         print("# ",end="")
#     print()

# lwra= input("Enter input :")
# oputput=" ".join(lwra.split()[::-1])
# print(oputput)

# days=8370
# year=int(days/375)
# print(year)

#work with CSV Files----->

# from csv import reader
# with open('new.csv', 'r') as f:
#     csv_reader=reader(f)
#     next(csv_reader)
#     for row in csv_reader:
#         print(row)


# from csv import DictReader

# with open('new.csv', 'r') as f:
#     csv_reader=DictReader(f)
#     for row in csv_reader:
#         print(row)

# from csv import writer
# with open ("new1.csv",'w', newline='') as f:
#     csv_write=writer(f)
#     csv_write.writerow(['name','country'])
#     csv_write.writerow(['Niladri','INDIA'])
#     csv_write.writerow(['Timir','INDIA'])
#     csv_write.writerow(['Kaniska','INDIA'])

#     csv_write.writerows([['name','country'],['Niladri','INDIA'],['Timir','INDIA'],['Kaniska','INDIA']])

# from csv import DictWriter

# with open ('new1.csv', 'w',newline='' ) as f:
#     csv_write=DictWriter(f, fieldnames=['firstname','lastname','age'])
#     csv_write.writeheader()
#     csv_write.writerow ({
#         'firstname' : 'Niladri',
#         'lastname'  : 'Biswas',
#         'age'       : 22
#     })
#     csv_write.writerow({
    
#         'firstname' : 'Timir',
#         'lastname'  : 'Hazra',
#         'age'       : 21
#     })
#     csv_write.writerow({

#         'firstname' : 'Kaniska',
#         'lastname'  : 'Bose',
#         'age'       : 23
#     })
#     csv_write.writerows([
          
#           {'firstname':'Niladri','lastname':'Biswas','age':22},
#           {'firstname':'Subho','lastname':'Mondal','age':22},
#           {'firstname':'Kaniska','lastname':'Biswas','age':23}
#     ])


# import calendar
# y=int(input("Enter year: "))
# m=int(input("Enter Month :"))
# x=calendar.month(y,m)
# print(x)

# from csv import DictReader, DictWriter
# with open('new1.csv', 'r') as rf:
#     with open('new2.csv', 'w', newline='') as wf:
#         csv_reader=DictReader(rf)
#         csv_write=DictWriter(wf,fieldnames=['firstname','lastname','age'])
#         for row in csv_reader:
#             fname, l_name, Age = row ['firstname'],row['lastname'],row['age']
#             csv_write.writerow({
                
#                     'firstname' : fname,
#                     'lastname'   : l_name,
#                     'age'        : Age

                
#             })

# def odd_even(x):
#     empty_list=[]
#     empty_list1=[]
#     for i in x:
#         if i % 2==0:
#             empty_list.append(i)
#         else:
#             empty_list1.append(i)
#     return empty_list,empty_list1               
# number=[1,2,3,4,5,6]
# print(odd_even(number))

# def revese_list(x):
#     empty_list=[]
#     for i in range(len(x)):
#         popped=x.pop()
#         empty_list.append(popped)
#     return empty_list
# number=[1,2,3,5]
# print(revese_list(number))

# def reves_ele(x):
#     empty_list=[]
#     for i in x:
#         empty_list.append(i[::-1])
#     return empty_list
# name=['xyz','abc','efg']
# print(reves_ele(name))

# l=[5,3,6,8,9,4,2]
# def bubble_sort(bal):
#     for i in range(0,len(l)-1):
#         for j in range(0,len(l)-1-i):
#             if l[j]>l[j+1]:
#                 l[j],l[j+1]=l[j+1],l[j]
#     return bal

# print(bubble_sort(l))


# l=[5,3,6,8,9,4,2]
# def Selection_sort(bal):
#     for i in range(6):
#         mainpos=i
#         for j in range(i,6+1):
#             if l[j] < l[mainpos]:
#                 mainpos=j
#         l[i],l[mainpos]=l[mainpos],l[i]
#     return bal
# print(Selection_sort(l))


#---Number Swiping

# x=int(input("Enter the number of x :"))
# y=int(input("Enter the number of y: "))   

# x=x+y 
# y=x-y 
# x=x-y 

# print(f'after swiping x = {x} y = {y}')


# l=[4,5,9,2,3,7,8,1]
# def bubble_sort(x):
#     for i in range(len(l)):
#         for j in range(len(l)-1-i):
#             if l[j] > l[j+1]:
#                 l[j],l[j+1]=l[j+1],l[j]
#     return x

# print(bubble_sort(l))


#---name pattern---->

# name=input("your name :")
# length=len(name)
# for row in range(length):
#     for col in range(length-row):
#         print(name[col], end='')
#     print()




# l=[4,6,8,3,2,9,1]
# def bubble_sort(x):
#     for num in range(len(l)):
#         for shorting in range(len(l)-1-num):
#             if l[shorting] > l[shorting+1]:
#                 l[shorting],l[shorting+1]=l[shorting+1],l[shorting]
#     return x
# print(bubble_sort(l))

# s1=input("Enter String :")
# s2=input("Enter string :")
# if s1[::-1] == s2:
#     print("Anagram")
# else: 
#     print("not Anagram")

# s1=input("Enter String :")
# s2=s1[::-1]
# print(s2)

# def reverseWordSentence(Sentence):
#     words = Sentence.split(" ")
#     newWords = [word[::-1] for word in words]
#     newSentence = " ".join(newWords)
#     return newSentence
# Sentence = "Hello ! Niladri Biswas"
# print(reverseWordSentence(Sentence))

# s1= input("Enter any sentence :").split(' ')
# print(s1)
# s2= [words[::-1] for words in s1]
# s3=' '.join(s2)
# print(s3)


# l=[2,4,7,8,9,7,1]
# def bubble_sort(x):
#     for i in range(len(l)-1):
#         for j in range(len(l)-1-i):
#             if l[j] < l[j+1]:
#                 l[j],l[j+1] = l[j+1],l[j]
#     return x
# print(bubble_sort(l))


# Python program to print all 
# prime number in an interval 

# start = int(input("Enter The start Number :"))
# end = int(input("Enter The End Number :"))

# for val in range(start, end + 1): 
	
# # If num is divisible by any number 
# # between 2 and val, it is not prime 
#     if val > 1: 
#         for n in range(2, val): 
#             if (val % n) == 0: 
#                 break
#         else: 
#             print(val) 

# l=[2,7,8,5,3,9,1,0]
# for i in range(7):
#     mainpos=i
#     for j in range(i,7+1):
#         if l[j] < l[mainpos]:
#             mainpos=j
#         l[i],l[mainpos] = l[mainpos],l[i]
# print(l)

# import random
# from time import sleep
# tails=0
# Hades=0
# flip = int(input("How many times you tosses ? :"))
# for i in range(flip):
#     result= random.randint(0,1)
#     sleep(0.5)
#     if result < 0.5:
#         print("tails")
#         tails += 1
#     else:
#         print("Hades")
#         Hades += 1
# print(f"Your Result is :Hades= {Hades} and Tails = {tails}")

# Linear Search Tree ------>
# l=[10,5,8,7,45,9,3]
# n=10
# pos=-1
# def search(l, n):
#     for i in range(len(l)):
#         if l[i]==n:
#             globals() ['pos'] = i
#             return True
# if search(l,n):
#     print(f"Found at {pos}")
# else:
#     print("Not Found")

# my_dict={
#     'a' : 'Chitas',
#     'b' : 'are',
#     'c' : 'fast'
# }

# for i in my_dict:
#     print(my_dict[i])

# Binary Search Tree---->
# l=[1,2,3,4,5,6,7,8,9,45,50]
# n=45
# pos=-1

# def Binary_Search(l,n):
#     Lower=0
#     Uper=len(l)-1
#     while Lower <= Uper:
#         mid=(Lower + Uper)//2
#         if l[mid]==n:
#             globals()['pos']=mid
#             return True
#         else:
#             if l[mid] < n:
#                 Lower= mid+1
#             else:
#                 Uper=mid-1
#     return False

# if Binary_Search(l,n):
#     print(f"found At {pos}")
# else:
#     print("not Found")


# how to print 70 to 80 withou given any number---->

# lst = ['a','b','c','d','e','f','g','h','i','j','k','l']
# a = lst.index('h')
# b = lst.index('k')
# c = lst.index('i')
 
 
# d = lst.index('b')
 
# k = b*c + d
 
# for i in range(a*b,k):
#     print (i)


# factorial number---->
# n=int(input("Enter a number :"))
# fact=1
# if n >=0:
#     for i in range(1,n+1):
#         fact= fact * i
#     print(fact)
# else:
#     print("negetive numbers dont have factorial")




# -----Quick Sort---->

# l=[5,6,8,2,0,3,1,100]

# def quicksort(sequence):
#     length=len(sequence)
#     if length <= 1:
#         return sequence
#     else:
#         pivot=sequence.pop()
#     item_greater=[]
#     item_lower=[]
#     for i in sequence:
#         if i > pivot:
#             item_greater.append(i)
#         else:
#             item_lower.append(i)
#     return quicksort(item_lower) + [pivot] + quicksort(item_greater)

# print(quicksort(l))

#----all prime from list--->
# l=[1,2,3,4,5,6,7,8]
# for i in l:
#     if i > 1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)

# vowel count---->
# s=input("Enter a sentence :")
# sentence= s.lower()
# count=0
# l=['a','e','i','o','u']
# for i in sentence:
#     if i in l:
#         count += 1
# print(f"number of vowel is {count}")


# l=[9,2,1,5,4,8,7,0]
# def mergesort(l):
#     if len(l) > 1:
#         mid=len(l)//2
#         left_list=l[:mid]
#         right_list=l[mid:]
#         mergesort(left_list)
#         mergesort(right_list)
#         i=0
#         j=0
#         k=0
#         while i < len(left_list) and j < len(right_list): 
#             if left_list[i] < right_list[j]:
#                 l[k] = left_list[i]
#                 i += 1
#                 k += 1
#             else:
#                 l[k] = right_list[j]
#                 j += 1
#                 k += 1
#         while i < len(left_list):
#             l[k] = left_list[i]
#             i += 1
#             k += 1
#         while j < len(right_list):
#             l[k] = right_list[j]
#             j += 1
#             k += 1
#     return l
# print(mergesort(l))

# how to find the duplicate value in a list---->
# l1=[1,1,3,3,0,5,0]
# l2=[i for i in range(len(l1)) if l1[i]==1 or l1[i]==3 or l1[i]==0]
# print(l2)


# ----remove duplicate values from a string--->
# a=input("write any sentence :")
# a1=a.lower()
# a2=0
# a3=""
# for i in a:
#     if a.index(i)==a2:
#         a3 += i
#     a2 += 1
# print(a3)


# how to remove duplicate values from list---->
# s1=['akash','biswas','niladri','biswas']
# s2=set(s1)
# s3=list(s2)
# print(s3)

# test_list=[1,2,2,5,6,8,9,1,9]
# unique_list=[]
# for i in test_list:
#     if i not in unique_list:
#         unique_list.append(i)
# print(unique_list)

# checkDublicatevalue------->
# def checkIfDuplicates_1(listOfElems):
#     if len(listOfElems) == len(set(listOfElems)):
#         return False
#     else:
#         return True

# listOfElems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test']
# result = checkIfDuplicates_1(listOfElems)
# print(result)
# if result:
# print('Yes, list contains duplicates')
# else:
# print('No duplicates found in list')  

# Python program to print  
# duplicates from a list  
# of integers 
# def Repeat(x): 
#     _size = len(x) 
#     repeated = [] 
#     for i in range(_size): 
#         k = i + 1
#         for j in range(k, _size): 
#             if x[i] == x[j] and x[i] not in repeated: 
#                 repeated.append(x[i]) 
#     return repeated 
  
# # Driver Code 
# list1 = [10, 20, 30, 20, 20, 30, 40,  
#          50, -20, 60, 60, -20, -20] 
# print (Repeat(list1))   
 
# prime number----->
# start=int(input("Enter where to start:"))
# end=int(input("Enter where to end :"))
# for i in range(start, end-1):
#     if i >= 2:
#         for j in range(2, i):
#             if i%j==0:
#                 break
#         else:
#             print(i)

# prime number from list--->
# l=[1,2,3,4,5,6,7,8,9,10]
# for i in l:
#     if i >= 2:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)

# check one number prime or not---->
# n=8
# for i in range(2, n):
#     if n%i==0:
#         print("not prime")
#         break
# else:
#     print("prime")

# string sorting--->
# def code(s):
#     return "".join(sorted((set(s.casefold().replace(" ","")))))
# s=input()
# print(code(s))

# sum of numbers in a string---->

# import re
# str1=input()
# str2=input()
# str3=input()
# str4=input()
# if len(str1)>=1 and len(str1)<=105:
#     s=sum(map(int,re.findall('\d+',str1)))
# if len(str2)>=1 and len(str2)<=105:
#     s1=sum(map(int,re.findall('\d+',str2)))
# if len(str3)>=1 and len(str3)<=105:
#     s2=sum(map(int,re.findall('\d+',str3)))
# if len(str4)>=1 and len(str4)<=105:
#     s3=sum(map(int,re.findall('\d+',str4)))
# print(s)
# print(s1)
# print(s2)
# print(s3)

# # Zig-Zag----->
# N=int(input("Enter number of elements :"))
# A=list(map(int, input("Enter the number :").split()))[:N]
# flag=True
# for i in range(1,len(A)):
#     if flag and A[i] < A[i-1]:
#         A[i],A[i-1]=A[i-1],A[i]
#     else:
#         if not flag and A[i] > A[i-1]:
#             A[i],A[i-1]=A[i-1],A[i]
#     flag= not flag

# for x in A:
#     print(x, end=" ")


# s=("\\")
# print("/"*11)
# print("|"*+2+"  "+'hii'+"|"*2)
# print((s)*11)

# print("//////////")
# print("| | Hii | |")
# print("\\\\\\\\\\\\\\\\\\\\")

# hacker rank problems---->
# q) If n is odd, print Weird
# If n is even and n in the inclusive range of 2  to 5 , print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20 , print Not Weird ?

# n=int(input("Enter number :"))
# if n%2!=0:
#     print("Weird")
# else:
#     if n>=2 and n<=5:
#         print("Not Weird")
#     else:
#         if n>=6 and n<=20:
#             print("Weird")
#         else:
#             print("Not Weird")

# print 1 to 10 without using loop--->
# n=1
# def func(n):
#     if (n<=10):
#         print(n, end=" ")
#         func(n+1)
# func(n)

# how to find nth position value in number---> 
# n=1234567
# s=n//(100000) #12
# s=n//(10000)%10 #3 
# print(s)

# Anagram----->
# s1=input("Enter string :")
# s2=input("Enter string :")
# sorted_str=sorted(s1)
# sorted_str1=sorted(s2)
# if sorted_str==sorted_str1:
#     print("Anagram")
# else:
#     if len(sorted_str)!=len(sorted_str1):
#         print("length of string should same")
#     else:
#         print("not anagram")


# class Stack:
#     def __init__(self):
#         self.items=[]

#     def push (self, item):
#         return self.items.append(item)

#     def pop_item(self):
#         return self.items.pop()

#     def get_item(self):
#         return self.items

# s=Stack()
# s.push(1)
# s.push(2)
# s.pop_item()
# print(s.get_item())

# factorial with Recursion--->
# def fact(n):
#     if n==0:
#         return 1
#     return n * fact(n-1)
# print(fact(5))

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Linklist:
#     def __init__(self):
#         self.start=None

#     def Insert_last(self,value):
#         new_node=Node(value)
#         if self.start==None:
#             self.start=new_node
#         else:
#             temp=self.start
#             while temp.next!=None:
#                 temp=temp.next
#             temp.next=new_node

#     def Insert_first(self,value):
#         new_node=Node(value)
#         new_node.next=self.start
#         self.start=new_node

#     def Insert_middle(self,midvalue,value):
#         if midvalue==None:
#             print("Insert Privious value")
#         else:
#             new_node=Node(value)
#             new_node.next=midvalue.next
#             midvalue.next=new_node
        
                
#     def view_list(self):
#         if self.start==None:
#             print("empty list")
#         else:
#             temp=self.start
#             while temp!=None:
#                 print(temp.data)
#                 temp=temp.next

#     def Delete_first(self):
#         if self.start==None:
#             print("no data")
#         else:
#             self.start=self.start.next

#     def delete_with_key(self,key):
#         temp=self.start
#         if temp.data==key:
#             self.start=temp.next
#         else:
#             temp=self.start
#             while temp.data!=key:
#                 temp1=temp
#                 temp=temp.next
#             temp1.next=temp.next

#     def delete_with_position(self,pos):
#         temp=self.start
#         if pos==0:
#             self.start=temp.next
#         else:
#             count=0
#             while count!=pos:
#                 temp1=temp
#                 count += 1
#                 temp=temp.next 
#             temp1.next=temp.next

#     def Delete_last(self):
#         if self.start==None:
#             print("No data")
#         else:
#             temp=self.start
#             while temp.next!=None:
#                 temp1=temp
#                 temp=temp.next
#             temp1.next=None

#     def search()

# mylist=Linklist()
# mylist.Insert_last(10)
# mylist.Insert_last(20)
# mylist.Insert_last(30)
# mylist.Insert_middle(mylist.start,5)
# mylist.Insert_last(40)
# mylist.Insert_first(50)
# mylist.Insert_first(60)
# mylist.view_list()
# print()
# # mylist.delete_with_key(60)
# # mylist.delete_with_position(3)
# mylist.Delete_last()
# mylist.view_list()

