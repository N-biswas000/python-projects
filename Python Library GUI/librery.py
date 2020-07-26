import tkinter as tk
from tkinter import *
from tkinter import messagebox as m_box
from tkinter import ttk
import mysql.connector



#startup---->

win=tk.Tk()
win.title('Student Librery')
win.geometry("900x300")

# Label Frames---->
label_frm=ttk.Labelframe(win, text='Enter Details')
label_frm.grid(row=0, column=5, padx=40, pady=2)

label_frm2=ttk.LabelFrame(win, text="Show Details")
label_frm2.grid(row=0, column=6, padx=40, pady=2 )

# Labels---->
name_lebel=ttk.Label(label_frm, text='Enter Student Name :',font=('Helvetica', 10, 'bold'))
name_lebel.grid(row=0, column=0, sticky=tk.W, padx=2, pady=5)

id_lebel=ttk.Label(label_frm, text='Enter Book Id Number :',font=('Helvetica', 10, 'bold'))
id_lebel.grid(row=1, column=0, sticky=tk.W, padx=2, pady=5)

rollno_lebel=ttk.Label(label_frm, text='Enter Roll Number :',font=('Helvetica', 10, 'bold'))
rollno_lebel.grid(row=2, column=0, sticky=tk.W, padx=2, pady=5)

date_lebel=ttk.Label(label_frm, text='Enter Date :',font=('Helvetica', 10, 'bold'))
date_lebel.grid(row=3, column=0, sticky=tk.W, padx=2, pady=5)

contact_lebel=ttk.Label(label_frm, text='Enter student Contact Number :',font=('Helvetica', 10, 'bold'))
contact_lebel.grid(row=4, column=0, sticky=tk.W, padx=2, pady=5)

dep_lebel=ttk.Label(label_frm, text='Enter Department :',font=('Helvetica', 10, 'bold'))
dep_lebel.grid(row=5, column=0, sticky=tk.W, padx=2, pady=5)

class_lebel=ttk.Label(label_frm, text="Enter Student's Class :",font=('Helvetica', 10, 'bold'))
class_lebel.grid(row=6, column=0, sticky=tk.W, padx=2, pady=5)

# EntryBox---->
name_var=StringVar()
name_entrybox=ttk.Entry(label_frm, textvariable=name_var)
name_entrybox.grid(row=0, column=1, padx=2, pady=5)

id_var=StringVar()
id_entrybox=ttk.Entry(label_frm, textvariable=id_var)
id_entrybox.grid(row=1, column=1, padx=2, pady=5)

roll_var=StringVar()
roll_entrybox=ttk.Entry(label_frm, textvariable=roll_var)
roll_entrybox.grid(row=2, column=1, padx=2, pady=5)

date_var=StringVar()
date_entrybox=ttk.Entry(label_frm, textvariable=date_var)
date_entrybox.grid(row=3, column=1, padx=2, pady=5)

contact_var=StringVar()
contact_entrybox=ttk.Entry(label_frm, textvariable=contact_var)
contact_entrybox.grid(row=4, column=1, padx=2, pady=5)

dep_var=StringVar()
dep_entrybox=ttk.Entry(label_frm, textvariable=dep_var)
dep_entrybox.grid(row=5, column=1, padx=2, pady=5)

class_var=StringVar()
class_entrybox=ttk.Entry(label_frm, textvariable=class_var)
class_entrybox.grid(row=6, column=1, padx=2, pady=5)

# Functions---->

def submit_data():
    name=name_var.get()
    book_id=id_var.get()
    roll_num=roll_var.get()
    d_t=date_var.get()
    contact=contact_var.get()
    de_part=dep_var.get()
    stu_class=class_var.get()

    if (name=="" or book_id=="" or roll_num=="" or d_t=="" or contact=="" or de_part=="" or stu_class==""):
        m_box.showerror("Error","All Are Fields Require !")
    else:
        try:
            roll_num=int(roll_num)
            contact=int(contact)
        except:
            m_box.showerror("Error","Invalid Values !")
        else:
            con=mysql.connector.connect(host="localhost",username="root",password="8145977541",database="lirery")
            my_cursor=con.cursor()
            query="INSERT INTO student_librery VALUES('%s','%s',%s,'%s',%s,'%s','%s')"%(name,book_id,roll_num,d_t,contact,de_part,stu_class)
            my_cursor.execute(query)
            con.commit()
            con.close()

            m_box.showinfo("Success","Data Submited !")

            name_entrybox.delete(0, tk.END)
            id_entrybox.delete(0, tk.END) 
            roll_entrybox.delete(0, tk.END) 
            date_entrybox.delete(0, tk.END) 
            contact_entrybox.delete(0, tk.END)
            dep_entrybox.delete(0, tk.END)
            class_entrybox.delete(0, tk.END)
                         

def delete_data():
    book_id=id_var.get()
    if (book_id==""):
        m_box.showerror("Error","Input Book Id")

    else:
        con=mysql.connector.connect(host="localhost",username="root",password="8145977541",database="lirery")
        my_cursor=con.cursor()
        query="DELETE FROM student_librery WHERE book_id='"+ book_id +"'"
        my_cursor.execute(query)
        con.commit()
        con.close()

        m_box.showinfo("Success","Data Delete!")

        id_entrybox.delete(0, tk.END) 


def update_data():
    name=name_var.get()
    book_id=id_var.get()
    roll_num=roll_var.get()
    d_t=date_var.get()
    contact=contact_var.get()
    de_part=dep_var.get()
    stu_class=class_var.get()
    if (name=="" or book_id=="" or roll_num=="" or d_t=="" or contact=="" or de_part=="" or stu_class==""):
        m_box.showerror("Error","All Are Fields Require !")
    else:
        try:
            roll_num=int(roll_num)
            contact=int(contact)
        except:
            m_box.showerror("Error","Invalid Values !")
        else:
            con=mysql.connector.connect(host="localhost",username="root",password="8145977541",database="lirery")
            my_cursor=con.cursor()
            query="UPDATE student_librery SET name='"+ name +"',roll_no='"+ str(roll_num) +"',book_taken='"+ d_t +"',contact_no='"+ str(contact) +"',stu_dep='"+ de_part +"',stu_class='"+ stu_class +"' WHERE book_id='"+ book_id +"' "
            my_cursor.execute(query)
            con.commit()
            con.close()

            m_box.showinfo("Update","Update ok!")

            name_entrybox.delete(0, tk.END)
            id_entrybox.delete(0, tk.END) 
            roll_entrybox.delete(0, tk.END) 
            date_entrybox.delete(0, tk.END) 
            contact_entrybox.delete(0, tk.END)
            dep_entrybox.delete(0, tk.END)
            class_entrybox.delete(0, tk.END)

def show():
        con = mysql.connector.connect(host='localhost', username='root', password='8145977541',database='lirery')
        my_cursor = con.cursor()
        query="SELECT * FROM student_librery"
        my_cursor.execute(query)
        rows=my_cursor.fetchall()
        
        for i in rows:
            insert_data=str(i[0])+'  '+str(i[1])+'  '+str(i[2])+'  '+str(i[3])+' '+str(i[4])+' '+str(i[5])+' '+str(i[6])
            list_box.insert(list_box.size(),insert_data)
        con.close()

# Listbox--->

list_box=tk.Listbox(label_frm2, width=40, height=15)
list_box.grid(row=0, column=0)
show()

# Buttons---->

submit_btn=ttk.Button(label_frm,text="SUBMIT",command=submit_data)
submit_btn.grid(row=7, column=0)

delete_btn=ttk.Button(label_frm,text="DELETE",command=delete_data)
delete_btn.grid(row=7, column=1)

update_btn=ttk.Button(label_frm,text="UPDATE",command=update_data)
update_btn.grid(row=7, column=2)



win.mainloop()