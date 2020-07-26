# class Laptop:
#     discount_percentage=10 #<-----class Variable
#     def __init__(self, name, model_name, price):
#         self.name=name
#         self.model_name=model_name
#         self.price=price
#         self.Laptop_name= name + ' ' + model_name
    
#     @staticmethod
#     def hello():
#         print("hello, static method called")

#     def apply_discount(self):
#         discount=(self.discount_percentage/100)*self.price
#         return self.price - discount
        

# lapy=Laptop('Acer','Nitro-5', 45000)
# lapy.discount_percentage=20
# print(f"Your discount is {lapy.apply_discount()}")
# print(lapy.__dict__)

# lapy1=Laptop('hp','albtx2', 23000)
# lapy1.discount_percentage=50
# print(f"Your Discount is {lapy1.apply_discount()}")
# print(lapy1.__dict__)

# class Circle:
#     pi=3.14   #<----- Class Variable
#     def __init__(self,redious):
#         self.redious=redious

#     def circle_calculation(self):
#         return 2*Circle.pi*self.redious

# c1=Circle(7)
# print(c1.circle_calculation())

# a=lambda x,y : x+y
# print(a(2,3))

# def func(x):
#     return x % 2==0
# print(func(9))

# func=lambda x : x%2==0
# print(func(4))

# func= lambda x : x[::-1]
# print(func('niladri'))

# func=lambda x : True if len(x) >= 5 else False
# print(func('nilad'))
    
# position tracker---->

# names=['abc' , 'abcder','Niladri']
# pos=0
# for i in names:
#     print(f"{pos}---->{i}")
#     pos += 1

# for pos, i in enumerate(names):
    # print(f"{pos}--->{i}")

# def func(x,y):
#     for pos, i in enumerate (x):
#         if i == y:
#             return pos
#     return -1
# names=['abc' , 'abcder','Niladri']
# print(func(names,"Niladri"))

# def square(x):
#     return x**2

# names=[1,2,3,4,5]

# square1= list(map(lambda a : a**2 ,names))
# print(square1)

# names=['abc' , 'abcder','Niladri']
# l=map(len, names)
# for i in l:
#     print(i)
        
# names=[2,1,3,6,5,8]
# is_even=list(filter(lambda a : a%2==0, names))
# for i in is_even:
#     print(i)

# for i in is_even:
#     print(i)

# names=['niladri','akash','nilu']
# names2=['user1','user2','user3']
# print(list(zip(names2, names)))

# new_list=[(1,2),(3,4),(5,6),(7,8)]
# l1, l2=list(zip(*new_list))
# print(list(l1))
# print(list(l2))

# return average of numbers in list----------->

# def average(*args):
#     empty_list=[]
#     for i in zip(*args):  #-----for unpacking list
#         empty_list.append(sum(i)/len(i))
#     return empty_list
# print(average([1,2,3,5],[4,5,6,7],[7,8,9,10]))

# average=lambda *args : [sum(i)/len(i) for i in zip(*args)]
# print(average([1,2,3,4], [5,6,7,8], [9,10,11,12])) 

# def all_input(*args):
#     if all([(type(i)==int or type(i)==float) for i in args]):
#         total=0
#         for j in args:
#             total+=j
#         return total
#     else:
#         return "wrong Input"
# print(all_input(1,2,3,4,5,6))

# students1= {
#     'Niladri' : {'score' : 90, 'age' : 21},
#     'Kaniska' : {'score' : 70, 'age' : 22},
#     'Timir' : {'score' : 60, 'age' : 21},
# }

# print(max(students1, key=lambda item : students1[item] ['score'] ))

# def square(a):
#     return a**2

# s= square
# print(s(7))

# print(s.__name__)
# print(square.__name__)

# def outer_func(msg):
#     def inner_func():
#         print(f'your Massage is {msg}')
#     return inner_func
# v=outer_func("Hi! You are Niladri")
# v()

# def to_power(x):
#     def select_number(n):
#         return n**x
#     return select_number
# cube=to_power(3)
# print(cube(7))

#-----decoraters Function------->

# def decoraters_function(any_function):
#     def wrapper_function(*args, **kwargs):
#         print('This is awasome function')
#         any_function(*args, **kwargs)
#     return wrapper_function

# @decoraters_function
# def func1(a):
#     print(f'This is function1 {a}')

# func1(2)

# class Person:    
#     def __init__(self, first_name, last_name, age):  
#         self.first_name=first_name  
#         self.last_name=last_name
#         self.age=age

#     def age_ckeck(self):
#         return self.age > 18

#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
    
# p1=Person('Niladri', 'Biswas', 22)
# print(p1.age_ckeck())
# print(p1.full_name())

# class Circle:
#     pi=3.14
#     def __init__(self, redius):
#         self.redius=redius
#     def limitation_calculation(self):
#         return 2*Circle.pi*self.redius
# c=Circle(4)
# c1=Circle(5)
# print(c.__dict__)
# print(c1.__dict__)
# print(c.limitation_calculation())
# print(c1.limitation_calculation())

# class Person:
#     count_instance=0
#     def __init__(self, fst_name, lst_name, age):
#         Person.count_instance+=1
#         self.fst_name=fst_name
#         self.lst_name=lst_name
#         self.age=age
    
#     @classmethod   #----class Method
#     def count_instances(cls):
#         return f"You have created {cls.count_instance} instance of Parson Class"
    
#     @staticmethod  #---Static method
#     def hello():
#         return 'hello , Static method called'

# p1=Person('Niladri','Biswas',22)
# p2=Person('Niladri','Biswas',22)
# print(Person.count_instance)
# print(p1.fst_name)
# print(p2.fst_name)
# print(Person.count_instances())
# print(Person.hello())

# class Phone:
#     def __init__(self, brand, model_name, price):
#         self.brand=brand
#         self.model_name=model_name
#         self._price=max(price,0)
#     @property     #property decoretor
#     def full_specification(self):
#         return f'Brand name {self.brand} Model name {self.model_name} price {self.price}'
    
#     @property
#     def price(self):
#         return self._price

#     @price.setter
#     def price(self, new_price):
#          self._price = max(new_price, 0)
    

    
# p1=Phone('Nokia','Nokia 1100',1000)
# p1.price=-500
# print(p1.brand)
# print(p1.model_name)
# print(p1.price)
# print(p1.full_specification)


#----Inheritance----->

# class Phone:
#     def __init__(self, brand, model_name, price):
#         self.brand=brand
#         self.model_name=model_name
#         self._price=max(price,0)

#     def full_specification(self):
#         return f'Brand name {self.brand} Model name {self.model_name}'
    
#     def phon_call(self):
#         return f'calling from {self.number}....'
    


# class Smartphone(Phone): #-----child class/inherite Phone class
#     def __init__(self, brand, model_name, price, ram, internal_memory, rear_cam):
#         super().__init__(brand, model_name, price)

#         self.ram=ram
#         self.internal_memory=internal_memory
#         self.rear_cam=rear_cam

# class Flagship_phone(Smartphone): #----multilavel_inheritance
#     def __init__(self, brand, model_name, price, ram, internal_memory, rear_cam, front_cam, display):
#         super().__init__(brand, model_name, price, ram, internal_memory, rear_cam)

#         self.front_cam=front_cam
#         self.display=display


# p1=Phone('Nokia','Nokia 1100',1000)
# p2=Smartphone('One Plase','One Pluse 7 pro',37500,'6 GB','64 GB','24+5 MP')
# p3=Flagship_phone('Samsung','Note 10 Plus',79500,'12 GB','128 GB','13+5+2 MP','32 MP','Super AMOLED')
# print(p1.brand)
# p1.number=8145977541
# print(p1.model_name)
# print(p1._price)
# print(p1.full_specification())
# print(p1.phon_call())

# print(p2.brand)
# p2.number=9609201051
# print(p2.model_name)
# print(p2._price)
# print(p2.internal_memory)
# print(p2.rear_cam)
# print(p2.full_specification() + f"The Price is '{p2._price}' '")
# print(p2.phon_call())

# print(p3.brand)
# p3.number=9126736975
# print(p3.model_name)
# print(p3._price)
# print(p3.front_cam)
# print(p2.internal_memory)
# print(p2.rear_cam)
# print(p3.display)
# print(p3.full_specification() + f'The Display is {p3.display}')
# print(p3.phon_call())

# print(help(Smartphone))  #---Method Resolution Order/MRO

# class Phone:
#     def __init__(self, brand, model_name, price):
#         self.brand=brand
#         self.model_name=model_name
#         self._price=price

#     def phone_name(self):
#         return f"name is {self.brand} and price is {self._price}"

    
#     def __len__(self): #----Magic Method/Dunder Method
#         return len(self.phone_name())

#     def __add__(self, other):
#         return self._price + other._price

# p1=Phone('Nokia','Nokia 1100',1000)
# p2=Phone('Nokia','Nokia 1100',2200)
# print(p1 + p2)
# print(len(p1))
# print(help(Phone))

#----Error Rising Example------>

# def add(a,b):
#     if (type(a) and type(b) == int):
#         return a+b
#     else:
#         raise TabError ("Something Went Wrong")
# print(add(2,3))

# class Animal:
#     def __init__(self,name):
#         self.name=name

#     def sound(self):
#         raise NotImplementedError("You have to define this method in subclass")

# class Dog(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed=breed

# class Cat(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed=breed

#     def sound(self):
#         return "Maou Maou"

# d1=Dog('Puppy','Pug')
# print(d1.sound())    


# Exception Handling------>
# while True:
#     try:
#         age=int(input("Enter Your Age :"))
#         break
#     except ValueError:
#         print("Ivalid Input!")
#     except:
#         print("unexpected Error...")
# if age >= 18:
#     print("You Can Play this game")
# else:
#     print("You cant play this game")


# while True:
#     try:
#         no=int(input("enter no"))
#     except ValueError:
#         print("enter proper value")
#     except:
#         print("unexpected error")
#     else:
#         print("this is else part")
#         break
#     finally:
#         print("this is finally part")

# def division(x,y):
#     try:
#         return x/y
#     except ZeroDivisionError:
#         print("dont pass zero value")
#     except TypeError:
#         ("put proper value")
#     except:
#         print("Unexpected error")
# print(division(4,'0'))

#----Custom Exception------>

# class NameTooShortError(ValueError):
#     pass

# def value(x):
#     if len(x) < 8:
#         raise NameTooShortError("The Name is Too Short!")

# user_name=input("Enter Your Name :")
# print(value(user_name))

#----Debugging------>

# import pdb
# pdb.set_trace()

# name=input("Enter Your Name :")
# Age=input("Enter Your Age :")
# age1=int(Age) + 5
# print(f"Your name is {name} & Your Age is {age1}")

#----read Files------>

# f=open("textfile.txt") #----open() ----Method
# print(f'coursur position - {f.tell()} ') #----tell()----Method
# f.seek(0) #-----seek()----Method
# # print(f.read())  #----read()---Method
# print(f.readline()) #-----readline()----Method
# print(f.readline()) #-----readline------Method
# f.close() #----close()----Method

# f=open("textfile.txt")
# lines=f.readlines() #----readlines()----Method
# for i in lines:
#     print(i,end="")
# f.close()

# with-----block---->
# context Manager

# with open("textfile.txt") as f:
#     data=f.read()
#     print(data)


# write File---->

# with open("textfile.txt" , 'w') as f: #-----'w' Mode---->
    # f.write("Hii")

# with open("textfile.txt", 'a') as f: #-----'a'----Mode--->
    # f.write('Akash Niladri Biswas')

# with open('file.txt' ,'r+') as f:    #-------'r+'---- mode--->
#     f.seek(len(f.read())) 
#     f.write("Hello There")

# with open("file.txt" , 'r') as rf:
#     with open("file1.txt", 'w') as wf:
#         wf.write(rf.read())


# try:
#     with open("file2.txt", 'r') as rf:
#         with open ('file3.txt' , 'a') as wf:
#             for i in rf.readlines():
#                 name,salary=i.split(',')
#                 wf.write(f'{name}\'s Salary is {salary}')
# except ValueError:
#     print("Unexpected Error But Code Will Run Currectly")



# os Module------>

# import os
# print(os.getcwd())

# os.mkdir("Program")

# print(os.path.exists("Program"))

# print(os.listdir())

# for i in os.listdir():
#    print('F:\Python' + '\\' + i)

# for i in os.listdir():
#     print(os.path.join(os.getcwd(),i))

# f=os.walk(r'F:\Python\Program')
# for current_path, folder_name,files_name in f:
#     print(f"Current Path : {current_path}")
#     print(f"Folder Name : {folder_name}")
#     print(f"File Name : {files_name}")

# edit Photo with python----->

from PIL import Image, ImageEnhance, ImageFilter
import os

# img1= Image.open("dog1.jpg")
# img1.save("dog1.png")
# img1.show()
# MAX_SIZE = (250,250)
# img1.thumbnail(MAX_SIZE)
# img1.save("dogsmall.jpg")

# for i in os.listdir():
#     if i.endswith(".jpg"):
#         img1= Image.open(i)
#         file_name, extension=os.path.splitext(i)
#         img1.save(f"{file_name}.png")

# img1=Image.open('dog1.jpg')
# enhancer= ImageEnhance.Color(img1)  #-----for color edit
# enhancer.enhance(0).save('Edited.jpg')

img1=Image.open('dog1.jpg')
enhancer= ImageEnhance.Sharpness(img1) #-----Sharpness---->
enhancer.enhance(5).save('Edited.jpg')

            
            
           




    

