import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box

win= tk.Tk()
win.title("Student")

label_frame = ttk.LabelFrame(win, text='Enter Your Details Below')
label_frame.grid(row=0, column=0, padx=40, pady=10)

labels=['What is Your name :', 'What is Your Age :','What is Your Email Id :','State :','City :']

#labels Using Loops

for i in range(len(labels)):
    cur_lebel = 'label' + str(i)
    cur_lebel = ttk.Label(label_frame, text=labels[i], font=('Helvetica', 12))
    cur_lebel.grid(row=i, column=0, sticky=tk.W, padx=5, pady=2)


#entryBox Using Loop

name_var= tk.StringVar()
user_info = {
    'name' : tk.StringVar(),
    'age' : tk.StringVar(),
    'Email' : tk.StringVar(),
    'State' : tk.StringVar(),
    'City' : tk.StringVar()
}
counter=0
for i in user_info:
    cur_entrybox= 'entry' + i
    cur_entrybox= ttk.Entry(label_frame, width=16, textvariable=user_info[i])
    cur_entrybox.grid(row=counter, column=1, padx=5, pady=2)
    counter+=1

def submit():
    print(user_info['name'].get())
    print(user_info.get('age').get())
    print(user_info.get('Email').get())
    print(user_info.get('State').get())
    print(user_info.get('City').get())

submit_btn= ttk.Button(label_frame, text='Submit', command=submit)
submit_btn.grid(row=6, columnspan=2)

win.mainloop()