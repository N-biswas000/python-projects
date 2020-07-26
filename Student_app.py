import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
import mysql.connector

win = tk.Tk()
win.title("Student Database")


# Labels---->

label_frame= ttk.LabelFrame(win, text="Enter Students Details")
label_frame.grid(row=0, column=5, padx=40, pady=2)

label_frame2= ttk.LabelFrame(win, text="Show Students Database")
label_frame2.grid(row=0, column=6, padx=20, pady=2)

r_num=ttk.Label(label_frame, text="Enter Roll No", font=('Helvetica', 10, 'bold'))
r_num.grid(row=0, column=0, sticky=tk.W, padx=10, pady=2)

f_name=ttk.Label(label_frame, text="Enter First Name", font=('Helvetica', 10, 'bold'))
f_name.grid(row=1, column=0, sticky=tk.W, padx=10, pady=2)

l_name=ttk.Label(label_frame, text="Enter Last Name", font=('Helvetica', 10, 'bold'))
l_name.grid(row=2, column=0, sticky=tk.W, padx=10, pady=2)

age=ttk.Label(label_frame, text="Enter Age", font=('Helvetica', 10, 'bold'))
age.grid(row=3, column=0, sticky=tk.W, padx=10, pady=2)

marks=ttk.Label(label_frame, text="Enter Students CGPA", font=('Helvetica', 10, 'bold'))
marks.grid(row=4, column=0, sticky=tk.W, padx=10, pady=2)

# EntryBoxs---->
rollnum_var=tk.StringVar()
rollnum_entrybox= ttk.Entry(label_frame, textvariable=rollnum_var)
rollnum_entrybox.grid(row=0, column=2, padx=10, pady=2)


fname_var=tk.StringVar()
fname_entrybox= ttk.Entry(label_frame, textvariable=fname_var)
fname_entrybox.grid(row=1, column=2, padx=10, pady=2)

lname_var=tk.StringVar()
lname_entrybox= ttk.Entry(label_frame, textvariable=lname_var)
lname_entrybox.grid(row=2, column=2, padx=10, pady=2)

age_var=tk.StringVar()
age_entrybox= ttk.Entry(label_frame, textvariable=age_var)
age_entrybox.grid(row=3, column=2, padx=10, pady=2)

mark_var=tk.StringVar()
mark_entrybox= ttk.Entry(label_frame, textvariable=mark_var)
mark_entrybox.grid(row=4, column=2, padx=10, pady=2)





# Functions----->

#Function For Submit Data
def submit_data():
    rollnumber=rollnum_var.get()
    first_name= fname_var.get()
    last_name= lname_var.get()
    age_s= age_var.get()
    marks_cgpa= mark_var.get()

    if (rollnumber=="" or first_name=="" or last_name=="" or age_s=="" or marks_cgpa==""):
        m_box.showerror("Error", 'All Fields Are Required !')
    else:
        try:
            age_s=int(age_s) 
            rollnumber=int(rollnumber)
            marks_cgpa= float(marks_cgpa)
        except ValueError:
            m_box.showerror("Error","The Value You Enter is Invalid!")
        else:
            con = mysql.connector.connect(host='localhost', username='root', password='8145977541',database='student')
            my_cursor = con.cursor()
            query="INSERT INTO student1 VALUES(%s,'%s','%s',%s,%s)"%(rollnumber,first_name,last_name,age_s,marks_cgpa)
            my_cursor.execute(query)
            con.commit()
            con.close()

            #effect After submit----->
            rollnum_entrybox.delete(0, tk.END)
            fname_entrybox.delete(0, tk.END)
            lname_entrybox.delete(0, tk.END)
            age_entrybox.delete(0, tk.END)
            mark_entrybox.delete(0, tk.END)

            m_box.showinfo("Success","Succesfully Submited!")
            rollnum_entrybox.focus()

#Function For delete data          
def delete_data():
    rollnumber=rollnum_var.get()
    if (rollnumber ==""):
        m_box.showerror("Error","No data found to delete!")
    else:
        try:
            rollnumber=int(rollnumber)
        except ValueError:
            m_box.showerror("Error","The Value You Enter is Invalid!")
        else:
            con = mysql.connector.connect(host='localhost', username='root', password='8145977541',database='student')
            my_cursor = con.cursor()
            query="DELETE FROM student1 WHERE roll='"+ str(rollnumber) +"'"
            my_cursor.execute(query)
            con.commit()
            con.close()
            m_box.showinfo("Delete","Delete Succesfully!")

            # effect after delete
            rollnum_entrybox.delete(0, tk.END)
            rollnum_entrybox.focus()

# Function For Update data
def update_data():
    rollnumber=rollnum_var.get()
    first_name= fname_var.get()
    last_name= lname_var.get()
    age_s= age_var.get()
    marks_cgpa= mark_var.get()

    if (rollnumber=="" or first_name=="" or last_name=="" or age_s=="" or marks_cgpa==""):
        m_box.showerror("Error","All Fields Are Required!")
    else:
        try:
            age_s=int(age_s) 
            rollnumber=int(rollnumber)
            marks_cgpa= float(marks_cgpa)
        except ValueError:
            m_box.showerror("Error","The Value You Enter is Invalid!")
        
        else:
            con = mysql.connector.connect(host='localhost', username='root', password='8145977541',database='student')
            my_cursor = con.cursor()
            query="UPDATE student1 SET fname='"+ first_name +"',lname='"+ last_name +"',age='"+ str(age_s) +"',cgpa='"+ str(marks_cgpa) +"' WHERE roll='"+ str(rollnumber) +"' "
            my_cursor.execute(query)
            con.commit()
            con.close()

            # Effect after update
            rollnum_entrybox.delete(0, tk.END)
            fname_entrybox.delete(0, tk.END)
            lname_entrybox.delete(0, tk.END)
            age_entrybox.delete(0, tk.END)
            mark_entrybox.delete(0, tk.END)
            m_box.showinfo("Updated","Updated Data!")
            rollnum_entrybox.focus()
  
# def get_data():
#     rollnumber=rollnum_var.get()
#     first_name= fname_var.get()
#     last_name= lname_var.get()
#     age_s= age_var.get()
#     marks_cgpa= mark_var.get()
#     if (rollnumber==""):
#         m_box("Error","Please Enter Roll No")
#     else:
#         try:
#             rollnumber=int(rollnumber)
#         except ValueError:
#             m_box.showerror("Error","The Value You Enter is Invalid!")
#         else:
#             con = mysql.connector.connect(host='localhost', username='root', password='8145977541',database='student')
#             my_cursor = con.cursor()
#             query="SELECT * FROM student1 WHERE roll='"+ str(rollnumber) +"'"
#             my_cursor.execute(query)
#             rows=my_cursor.fetchall()
            
#             for row in rows:
#                 first_name.insert(0, rows[1])
#                 last_name.insert(0, rows[2])
#                 age_s.insert(0, rows[3])
#                 marks_cgpa.insert(0, rows[4])
            
#             con.close()

def show():
        con = mysql.connector.connect(host='localhost', username='root', password='8145977541',database='student')
        my_cursor = con.cursor()
        query="SELECT * FROM student1"
        my_cursor.execute(query)
        rows=my_cursor.fetchall()
        for row in rows:
            insert_data=str(row[0])+'  '+str(row[1])+'  '+str(row[2])+'  '+str(row[3])+' '+str(row[4])
            list_box.insert(list_box.size(),insert_data)
        con.close()
    

                

# Buttons

submit_button=tk.Button(label_frame, text='SUBMIT', command=submit_data)
submit_button.grid(row=5, column=0)

delete_button=tk.Button(label_frame, text='DELETE', command=delete_data)
delete_button.grid(row=5, column=1)

update_button=tk.Button(label_frame, text='UPDATE', command=update_data)
update_button.grid(row=5, column=2)

# get_button=tk.Button(label_frame, text='GET', command=get_data)
# get_button.grid(row=5, column=3)

list_box=tk.Listbox(label_frame2, width=30, height=10)
list_box.grid(row=0, column=0)
show()

win.mainloop()
