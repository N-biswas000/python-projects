#def add_two(num1,num2):
 #   return num1+num2
#print(add_two(10,12))

#number=[1, 2, 3, 4, 5, 6]
#def squre_list1(y):
    #squre_list2=[]
    #for i in y:
        #squre_list2.append(i**2)
    #return squre_list2
#print(squre_list1(number))

# number=[1, 2, 3, 4]
# def reversed_list(x):
#     reversed1=number[::-1]
#     return reversed1
# print(reversed_list(number))

#number=[1, 2, 3, 4]
# def rev_list(x):
#     empty_list=[]
#     for i in range(len(x)):
#         popped_list=x.pop()
#         empty_list.append(popped_list)
#     return empty_list
# print(rev_list(number))

# word=['xyz', 'omp', 'tvp']
# def reversed_ele(x):
#     empty_list=[]
#     for i in x:
#         empty_list.append(i[::-1])
#     return empty_list
# print(reversed_ele(word))

# def filter_odd_even(x):
#     odd_nums=[]
#     even_nums=[]
#     for i in x:
#         if i%2==0:
#             even_nums.append(i)
#         else:
#             odd_nums.append(i)
#         output=[even_nums,odd_nums]
#     return output
# number=[1, 2, 3, 4, 5, 6, 7, 8]
# print(filter_odd_even(number))

# number=[1, 2, 3, 4, 5]
# number1=[1, 2, 7, 8, 9]
# def common_ele(x,y):
#     empty_list=[]
#     for i in x:
#         if i in y:
#             empty_list.append(i)
#     return empty_list
# print(common_ele(number,number1))

# def reversed_list(x):
#     x.reverse()
#     return x
# num=[1,2,3,4,5]
# print(reversed_list(num))    

# number=[1,2,3,4,5]
# def reversed_list(x):
#     empty_list=[]
#     while number:
#          popped=number.pop()
#          empty_list.append(popped)
#     return empty_list
# print(reversed_list(number))

# name1=['Niladri']
# name2=['Biswas']
# def add_two(x,y):
#     empty_list=[]
#     name1.extend(name2)
#     name3=(' ').join(name1)
#     empty_list.append(name3)
#     return empty_list
# print(add_two(name1,name2))

# words=('abc','efg',['xyz','ijk'])
# words[2].append('hgf')
# print(words)


# user_info= {
#          'name': 'Niladri',
#          'age' : 22,
#          'fav_movies' : ['Tare Zamin Paar', 'Tarzan'],
#          'fav_tuines': ['awakoning','fairy tale'],
# }
# for i in user_info.keys():
#     print(i)


# user_info= {
#          'name': 'Niladri',
#          'age' : 22,
#          'fav_movies' : ['Tare Zamin Paar', 'Tarzan'],
#          'fav_tuines': ['awakoning','fairy tale'],
# }

# for i in user_info.values():
#     print(i)

# user_info= {
#          'name': 'Niladri',
#          'age' : 22,
#          'fav_movies' : ['Tare Zamin Paar', 'Tarzan'],
#          'fav_tuines': ['awakoning','fairy tale'],
# }

# for key, value in user_info.items():
#     print(f"your key {key} and value {value} ")

#add data to dictionary----->

# user_info= {
#          'name': 'Niladri',
#          'age' : 22,
#          'fav_movies' : ['Tare Zamin Paar', 'Tarzan'],
#          'fav_tuines': ['awakoning','fairy tale'],
# }
# user_info['fav_song'] = ['song1', 'song2']
# print(user_info)

# pop method----->

# user_info= {
#          'name': 'Niladri',
#          'age' : 22,
#          'fav_movies' : ['Tare Zamin Paar', 'Tarzan'],
#          'fav_tuines': ['awakoning','fairy tale'],
# }
# popped_item=user_info.pop('fav_movies')
# print(f"pop item is {popped_item}")
# print(type(popped_item))
# print(user_info)

# popitem method --------->

# user_info= {
#          'name': 'Niladri',
#          'age' : 22,
#          'fav_movies' : ['Tare Zamin Paar', 'Tarzan'],
#          'fav_tuines': ['awakoning','fairy tale'],
# }
# popped_item=user_info.popitem()
# print(user_info)
# print(type(popped_item))
# print(f"pooped item is {popped_item}")

# update dictionary-------->

# user_info= {
#          'name': 'Niladri',
#          'age' : 22,
#          'fav_movies' : ['Tare Zamin Paar', 'Tarzan'],
#          'fav_tuines': ['awakoning','fairy tale'],
# }

# more_info={'name' : 'Niladri Biswas','hobbies' : ['watching movies','watching Cricket','Social media']}
# user_info.update(more_info)
# print(user_info)

# def cube_values(n):
#     empty_dict={}
#     for i in range(1,n+1):
#         empty_dict[i]=i**3
#     return empty_dict
# print(cube_values(10))

# def word_counter(s):
#     empty_dict={}
#     for i in s:
#         empty_dict[i]=s.count(i)
#     return empty_dict
# print(word_counter('niladri'))

# user={}

# name=input("Enter Your Nmae :")
# age=input("Enter Your Age :")
# fav_movies=input("Enter Your Favorite Movies separeted by (,) :").split(',')
# fav_song=input("Enter Your Favorite Songs separeted by (,) :").split(',')

# user['name']= name
# user['age']= age
# user['fav_movies']= fav_movies
# user['fav_song']= fav_song

# for i,j in user.items():
#     print(f"{i} : {j}")

# s={1,2,3,4,2}
# print(s)

# l=[1,2,3,3,4,2,6,7,6,5,8,9,5]
# s2=list(set(l))
# print(s2)

# s={1,2,3}
# s.discard(3)
# print(s)

# s1={5,6,7}
# s={1,2,3}
# s=s1.copy()
# print(s)

# -----List Comprehension------>

# l=['abc','efg','ijk']
# def reversed_ele(x):
#     empty_list=[i[::-1] for i in x ]
#     return empty_list
# print(reversed_ele(l))   

# def odd_even(x):
    
#     even_nums=[i for i in x if i%2==0]
#     odd_nums=[i for i in x if i%2!=0]
#     output=[even_nums,odd_nums]
#     return output
# number= list(range(1,11))
# print(odd_even(number))

# numbers=[1, 1.0, 3, True, False, [1,2,3]]
# empty_list=[]
# for i in numbers:
#     if type(i)==int or type(i)==float:
#         empty_list.append(str(i))
# print(empty_list)

# def new_func(x):
#     return [str(i) for i in x if type(i)==int or type(i)==float]
# numbers=[1, 1.0, 3, True, False, [1,2,3]]
# print(new_func(numbers))

# def odd_even(x):
#     return [-i if(i%2==0) else i*2 for i in nums]
# nums=[1, 2, 3, 5, 6, 7, 8, 9, 10]
# print(odd_even(nums))

# nested_comp=[[1,2,3],[1,2,3],[1,2,3]]

# example_comp=[[i for i in range(1,4)] for j in range(4)]
# print(example_comp)

# odd_even={i:('even' if i%2==0 else 'odd')for i in range(1,11)}
# print(odd_even)

# s={i*2 for i in range(1,11)}
# print(s)

# names=['Niladri','Akash','Rahul']
# s={i[0] for i in names}
# print(s)

# def all_total(*args):
#     return args
# print(all_total(3,4,5,6,78))

# add= lambda y,z : y+z
# print(add(2,3))

# even1= lambda a : a%2==0
# print(even1(5))

# last_char= lambda a : a[-1]
# print(last_char('niladri'))

# def all_total(*args):
#     total=0
#     for i in args:
#         total+=i
#     return total
# print(all_total(1,2,3,4,5))

# def multiply_nums(num, *args):
#     multiply=1
#     for i in args:
#         multiply*=i
#     return multiply
# print(multiply_nums(2,1,3,4,5))

# def multiply_list(*args):
#     multiply=1
#     for i in args:
#         multiply*=i
#     return multiply
# nums=[1,2,3,4,5]
# print(multiply_list(*nums))

# def list_multiple(nums, *args):
#     if args:
#         return [i**nums for i in args]
#     else:
#         return "You dont pass any args"
# print(list_multiple(3, *[2,4,6,8,10] ))

# def func(x, **kwargs):
#     if kwargs.get('kwargs_elements')==True:
#         return [i[::-1].title() for i in x]
#     else:
#         return [i.title() for i in x]
# names=['niladri','akash']
# print(func(names, kwargs_elements=True))





     
 





