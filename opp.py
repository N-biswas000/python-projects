# ------class Demo--------
class Person:    #define the class
    def __init__(self, first_name, last_name, age):  #<--------define constructor/ INIT Method
        self.first_name=first_name  #<-----------define Attributes/ Instance Variables
        self.last_name=last_name
        self.age=age

# ------Create Object-----

p1=Person('Niladri', 'Biswas', 22)
p2=Person('Akash','Biswas', 21)

