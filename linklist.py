# Link List View, Delete, insert, search----->

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linklist:
    def __init__(self):
        self.start=None

    def view_List(self):
        if self.start==None:
            print("List is empty")
        else:
            temp=self.start
            while temp!=None:
                print(temp.data)
                temp=temp.next 
    def delete_first(self):
        if self.start==None:
            print("List is Empty")
        else:
            self.start=self.start.next
            
    def delete_last(self):
        if self.start==None:
            print("No data found")
        else:
            temp=self.start
            while temp.next!=None:
                temp1=temp
                temp=temp.next
            temp1.next=None

    def delete_data_with_position(self, pos):
        temp=self.start
        if pos==0:
            self.start=temp.next
        else:
            try:
                count=0
                while temp and count!=pos:
                    temp1=temp
                    temp=temp.next
                    count += 1
                temp1.next=temp.next
            except:
                print("no data")
    
    def delete_data_with_key(self, key):
        temp=self.start
        if temp and temp.data==key:
            self.start=temp.next
        else:
            try:
                while temp and temp.data!=key:
                    temp1=temp
                    temp=temp.next
                temp1.next=temp.next
            except:
                print("No data")

    def Insert_last(self,value):
        new_Node=Node(value)
        if self.start==None:
            self.start=new_Node
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=new_Node
    
    def Insert_first(self, value):
        new_Node=Node(value)
        new_Node.next=self.start
        self.start=new_Node

    def Insert_Middle(self,midvalue,value):
        if midvalue==None:
            print("no previous value")
        else:
            new_Node=Node(value)
            new_Node.next=midvalue.next
            midvalue.next=new_Node

    def reverse_iterative(self):
        prev=None
        temp=self.start
        while temp!=None:
            tempnxt=temp.next
            temp.next=prev
            prev=temp
            temp=tempnxt
        self.start=prev


    def search_data(self, value):
        temp=self.start
        while temp.next!=None:
            if temp.data==value:
                return True
            temp=temp.next
        return False


mylist=Linklist()
mylist.Insert_last("A")
mylist.Insert_last("B")
mylist.Insert_last("c")
mylist.Insert_last("d")
mylist.Insert_last("e")
mylist.Insert_last("f")
mylist.Insert_first("g")
mylist.Insert_first("h")
# mylist.delete_data_with_key("e")
# mylist.Insert_Middle(mylist.start.next,"f")
# mylist.delete_last()
mylist.view_List()
# if mylist.search_data("f"):
#     print("yes")
# else:
#     print("No")
# print()
# mylist.delete_data_with_position(3)
# mylist.view_List()
print()
mylist.reverse_iterative()
mylist.view_List()