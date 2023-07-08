from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from data_base import Database

data_base = Database("Employee.db")
root = Tk()
root.title("Employee Management Software                                                                                                                                                                                                                                     ")
root.geometry("1920x1080+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")

EId= SringVar()
name = StringVar()
contact = StringVar()
email = StringVar()
doj = StringVar()

entries_frame = Frame(root, bg="#535c68")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Employee Management System", font=("Times New Roman", 18, "bold"), bg="#535c68", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")


lblEId = Label(entries_frame, text="Age", font=("Times New Roman", 16), bg="#535c68", fg="white")
lblEId.grid(row=1, column=2, padx=10, pady=10, sticky="w")
txtEId = Entry(entries_frame, textvariable=age, font=("Times New Roman", 16), width=30)
txtEId.grid(row=1, column=3, padx=10, pady=10, sticky="w")

lblName = Label(entries_frame, text="Name", font=("Times New Roman", 16), bg="#535c68", fg="white")
lblName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txtName = Entry(entries_frame, textvariable=name, font=("Times New Roman", 16), width=30)
txtName.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lblContact = Label(entries_frame, text="Contact No", font=("Times New Roman", 16), bg="#535c68", fg="white")
lblContact.grid(row=3, column=2, padx=10, pady=10, sticky="w")
txtContact = Entry(entries_frame, textvariable=contact, font=("Times New Roman", 16), width=30)
txtContact.grid(row=3, column=3, padx=10, sticky="w")

lblEmail = Label(entries_frame, text="Email", font=("Times New Roman", 16), bg="#535c68", fg="white")
lblEmail.grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtEmail = Entry(entries_frame, textvariable=email, font=("Times New Roman", 16), width=30)
txtEmail.grid(row=2, column=3, padx=10, pady=10, sticky="w")

lbldoj = Label(entries_frame, text="D.O.J", font=("Times New Roman", 16), bg="#535c68", fg="white")
lbldoj.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtDoj = Entry(entries_frame, textvariable=doj, font=("Times New Roman", 16), width=30)
txtDoj.grid(row=2, column=1, padx=10, pady=10, sticky="w")


def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    eid.set(row[1])
    name.set(row[2])
    contact.set(row[3])
    email.set(row[4])
    doj.delete(1.0, END)
    dojinsert(END, row[4])

def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)


def add_detail():
    if txtEId.get() == "" or txtName.get() == "" or txtContact.get() == "" or txtEmail.get() == "" or txtDoj.get( 1.0, END) == "":
        messagebox.showerror("Error: Please fill all the information")
        return
    db.insert(txtEId.get(),txtName.get(), txtContact.get() ,txtDoj.get(1.0, END))
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    displayAll()



def update_detail():
    if txtEId.get() == "" or txtName.get() == "" or txtContact.get() == "" or txtEmail.get() == "" or  txtDoj.get(1.0, END) == "":
        messagebox.showerror("Error: Please fill all the information")
        return
    db.update(row[0],txtEId.get(), txtName.get(), txtContact.get(), txtEmail.get(),txtDoj.get(1.0, END))
    messagebox.showinfo("Success", "Record Updated")
    clearAll()
    displayAll()


def delete_detail():
    db.remove(row[0])
    clearAll()
    displayAll()




btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnAdd = Button(btn_frame, command=add_employee, text="Add Details", width=15, font=("Times New Roman", 16, "bold"), fg="white",
                bg="#16a085", bd=0).grid(row=0, column=0)
btnEdit = Button(btn_frame, command=update_employee, text="Update Details", width=15, font=("Times New Roman", 16, "bold"),
                 fg="white", bg="#2980b9",
                 bd=0).grid(row=0, column=1, padx=10)
btnDelete = Button(btn_frame, command=delete_employee, text="Delete Details", width=15, font=("Times New Roman", 16, "bold"),
                   fg="white", bg="#c0392b",
                   bd=0).grid(row=0, column=2, padx=10)



tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=0, y=480, width=1980, height=520)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Times New Roman', 18),
                rowheight=50)  
style.configure("mystyle.Treeview.Heading", font=('Times New Roman', 18))  
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5), style="mystyle.Treeview")
tv.heading("1", text="EId")
tv.column("1", width=5)
tv.heading("2", text="Name")
tv.heading("3", text="contact")
tv.heading("4", text="Email")
tv.heading("5", text="DOJ")
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

dispalyAll()
root.mainloop()
