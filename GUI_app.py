# starter code
import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os

win = tk.Tk()
win.title("GuiApp")

# create labels
name_label=ttk.Label(win, text="Enter Your name : ")
name_label.grid(row=0, column=0, sticky=tk.W)

age_label=ttk.Label(win, text="Enter Your Age :")
age_label.grid(row=1, column=0, sticky=tk.W) 

gender_label=ttk.Label(win, text="Select Gender :")
gender_label.grid(row=3, column=0, sticky=tk.W) 

email_label=ttk.Label(win, text="Enter Your Email :")
email_label.grid(row=2, column=0, sticky=tk.W) 

# create entry Box
name_var = tk.StringVar()
name_entrybox = ttk.Entry(win, width=16, textvariable = name_var)
name_entrybox.grid(row= 0, column=1)
name_entrybox.focus()

age_var = tk.StringVar()
age_entrybox = ttk.Entry(win, width=16, textvariable = age_var)
age_entrybox.grid(row= 1, column=1)

email_var = tk.StringVar()
email_entrybox = ttk.Entry(win, width=16, textvariable = email_var)
email_entrybox.grid(row= 2, column=1)

# Submit botton create with function
# def action():
#     username= name_var.get()
#     age=age_var.get()
#     email=email_var.get()
#     print(f"{username} is {age} years old and email is {email}")
#     gender=gender_var.get()
#     user_type=usertype.get()
#     if check_var.get() == 0:
#         agree = 'NO'
#     else:
#         agree = 'YES'
#     print(gender, user_type, agree)

#     with open('fileGUI.txt', 'a') as f:
#         f.write(f'{username},{age},{email},{gender},{user_type},{agree}\n')

#     # effect after submit 
#     name_entrybox.delete(0, tk.END)
#     age_entrybox.delete(0, tk.END)
#     email_entrybox.delete(0, tk.END)
    
#     # Coloring 
#     name_label.configure(foreground='blue')
#     submit_button.configure(foreground='#F81111')
    

# Write to CSV File
def action():
    username= name_var.get()
    age=age_var.get()
    email=email_var.get()
    print(f"{username} is {age} years old and email is {email}")
    gender=gender_var.get()
    user_type=usertype.get()
    if check_var.get() == 0:
        agree = 'NO'
    else:
        agree = 'YES'

    with open('fileGUI.csv', 'a' , newline='') as f:
        Dict_Writer = DictWriter(f, fieldnames=['UserName','Age','Email_id','User_gender','User_type','Agreed'])

        if os.stat('fileGUI.csv').st_size==0:
            Dict_Writer.writeheader()
        else:
            Dict_Writer.writerow ({
                    'UserName': username,
                    'Age'     : age,
                    'Email_id': email,
                    'User_gender': gender,
                    'User_type' : user_type,
                    'Agreed' : agree                    
                }) 
                

    # effect after submit 
    name_entrybox.delete(0, tk.END)
    age_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)


submit_button=tk.Button(win, text='Submit', command=action)
submit_button.grid(row=6, column=0)

# creat Combo box

gender_var=tk.StringVar()
combo_box=ttk.Combobox(win, width=10, textvariable = gender_var, state='readonly')
combo_box['values'] = ('Male', 'Female','Other')
combo_box.current(0)
combo_box.grid(row=3, column=1)

#  create Radio button

usertype=tk.StringVar()
radio_btn1=ttk.Radiobutton(win, text='Student', value='Student', variable=usertype)
radio_btn1.grid(row=4, column=0)

radio_btn2=ttk.Radiobutton(win, text='Professional', value='Professional', variable=usertype)
radio_btn2.grid(row=4, column=1)


# check Button
check_var= tk.IntVar()
check_btn=ttk.Checkbutton(win, text="I Read All T&C", variable=check_var)
check_btn.grid(row=5, columnspan=5)

win.mainloop()
