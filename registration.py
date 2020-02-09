from tkinter import *
from tkinter import ttk



# methods
def clicked():
    if len(fname_entry.get()) == 0:
        fname_error = "Please enter your first name "
        fname_warning.configure(text=fname_error)
        fname_entry.focus()
    else:
        fname_warning.configure(text="")

    if len(lname_entry.get()) == 0:
        lname_error = "Please enter your last name "
        lname_warning.configure(text=lname_error)
        lname_entry.focus()
    else:
        lname_warning.configure(text="") 
        
    if len(email_entry.get()) == 0:
        email_error = "Please enter your email address "
        email_warning.configure(text=email_error)
        email_entry.focus()
    else:
        email_warning.configure(text="")
        
    if len(contact_entry.get()) == 0:
        contact_error = "Please enter your contact details"
        contact_warning.configure(text=contact_error)
        contact_entry.focus()
    else:
        contact_warning.configure(text="")
        
    if len(lname_entry.get()) > 0:
        res = "Welcome " + lname_entry.get()
        lbl.configure(text=res)
    if len(fname_entry.get()) > 0 and len(lname_entry.get()) > 0 and len(email_entry.get()) > 0 and len(contact_entry.get()) > 0:
        header = "Submitted Details"
        submitted_details_header.configure(text=header)
        fname = fname_entry.get()
        submitted_fname.configure(text=fname)
        lname = lname_entry.get()
        submitted_lname.configure(text=lname)
        email = email_entry.get()
        submitted_email.configure(text=email)
        contact = contact_entry.get()
        submitted_contact.configure(text=contact)
        
        
        

    else:
        submitted_fname.configure(text="")
        submitted_lname.configure(text="")
        submitted_email.configure(text="")
        submitted_contact.configure(text="")
        submitted_gender.configure(text="")



    
root = Tk()

root.title("User Registration")
root.geometry("400x450")
#root.configure(background="grey")

fname = Label(root, text="First Name")
fname.grid(row=1, column=0)
lname = Label(root, text="Last Name")
lname.grid(row=2, column=0)
email = Label(root, text="Email Address")
email.grid(row=3, column=0)
contact = Label(root, text="Contact Number")
contact.grid(row=4, column=0)

fname_entry = Entry(root)
fname_entry.grid(row=1, column=1)
lname_entry = Entry(root)
lname_entry.grid(row=2, column=1)
email_entry = Entry(root)
email_entry.grid(row=3, column=1)
contact_entry = Entry(root)
contact_entry.grid(row=4, column=1)


ttk.Button(root, text="Submit", command=clicked).grid(row=8, column=0)

lbl = Label(root)
lbl.grid(row=9, column=0, columnspan=6)

fname_warning = Label(root)
fname_warning.grid(row=10, column=0, columnspan=6)
lname_warning = Label(root)
lname_warning.grid(row=11, column=0, columnspan=6)
email_warning = Label(root)
email_warning.grid(row=12, column=0, columnspan=6)
contact_warning = Label(root)
contact_warning.grid(row=13, column=0, columnspan=6)



submitted_details_header = Label(root, font=("Arial Bold", 12))
submitted_details_header.grid(row=14, column=0, columnspan=6)
submitted_fname = Label(root)
submitted_fname.grid(row=15, column=0, columnspan=6)
submitted_lname = Label(root)
submitted_lname.grid(row=16, column=0, columnspan=6)
submitted_email = Label(root)
submitted_email.grid(row=17, column=0, columnspan=6)
submitted_contact = Label(root)
submitted_contact.grid(row=18, column=0, columnspan=6)
submitted_gender = Label(root)
submitted_gender.grid(row=19, column=0, columnspan=6)


root.mainloop()




# end of methods


