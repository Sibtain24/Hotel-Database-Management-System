from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector


def mainwindow():

    root = Tk()
    root.geometry("1050x750")
    root.title("Hotel Management System")
    root.wm_iconbitmap("Icon.ico")

    # Assigning variables to get user input:

    g_no = StringVar()
    name = StringVar()
    age = StringVar()
    gender = StringVar()
    address = StringVar()
    contact = StringVar()
    room = StringVar()
    checkindate = StringVar()
    checkoutdate = StringVar()

    # Function to fetch the data from mySQL:

    def fetch():
        mydatabase = mysql.connector.connect(host="localhost", user="root", passwd='sufi')
        mycursor = mydatabase.cursor()
        mycursor.execute("use hotel_dbms")
        mycursor.execute("select * from info")
        query = mycursor.fetchall()
        if len(query) != 0:
            info_table.delete(*info_table.get_children())
            i = 0
            for row in query:
                info_table.insert('', i, text="",
                                  values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
                i = i + 1
        mydatabase.commit()
        mydatabase.close()

    # Function to take input from user and insert it into mySQL database:

    def add():
        mydatabase = mysql.connector.connect(host="localhost", user="root", passwd='sufi')
        mycursor = mydatabase.cursor()
        mycursor.execute("use hotel_dbms")
        enter = "Insert into info values({},'{}',{},'{}','{}',{},{},'{}','{}')".format(g_no.get(), name.get(),
                                                                                       age.get(), gender.get(),
                                                                                       address.get(), contact.get(),
                                                                                       room.get(), checkindate.get(),
                                                                                       checkoutdate.get())
        if g_no.get() == "" or name.get() == "" or age.get() == "" or gender.get() == "" or address.get() == "" or contact.get() == "" or room.get() == "" or checkindate.get() == "" or checkoutdate.get() == "":
            messagebox.showerror("Error", "All Fields are Required")
        else:
            mycursor.execute(enter)
            mydatabase.commit()
            messagebox.showinfo("Details Entered", "Record added successfully")
            fetch()
            clear()
        mydatabase.close()

    # Function to get the values from database into the entry widget:

    def getvals(event):
        get = info_table.focus()
        contents = info_table.item(get)
        row = contents['values']
        g_no.set(row[0])
        name.set(row[1])
        age.set(row[2])
        gender.set(row[3])
        address.set(row[4])
        contact.set(row[5])
        room.set(row[6])
        checkindate.set(row[7])
        checkoutdate.set(row[8])

    # Function to update the data:

    def update():
        mydatabase = mysql.connector.connect(host="localhost", user="root", passwd='sufi')
        mycursor = mydatabase.cursor()
        mycursor.execute("use hotel_dbms")
        updt = "update info set GuestName='{}', Age={}, Gender='{}', Address='{}', ContactNo={}, RoomNo={},CheckinDate='{}', CheckoutDate='{}' where GuestNo={}".format(
            name.get(), age.get(), gender.get(), address.get(), contact.get(), room.get(), checkindate.get(),
            checkoutdate.get(), g_no.get())
        if g_no.get() == "" or name.get() == "" or age.get() == "" or gender.get() == "" or address.get() == "" or contact.get() == "" or room.get() == "" or checkindate.get() == "" or checkoutdate.get() == "":
            messagebox.showerror("Error", "Select a data to update")
        else:
            mycursor.execute(updt)
            mydatabase.commit()
            messagebox.showinfo("Details Updated", "Details updated successfully")
            fetch()
            clear()
        mydatabase.close()

    # Function to delete a data:

    def delete():
        mydatabase = mysql.connector.connect(host="localhost", user="root", passwd='sufi')
        mycursor = mydatabase.cursor()
        mycursor.execute("use hotel_dbms")
        dlt = "delete from info where GuestNo={}".format(g_no.get())
        if g_no.get() == "" or name.get() == "" or age.get() == "" or gender.get() == "" or address.get() == "" or contact.get() == "" or room.get() == "" or checkindate.get() == "" or checkoutdate.get() == "":
            messagebox.showerror("Error", "Select a data to delete")
        else:
            mycursor.execute(dlt)
            mydatabase.commit()
            messagebox.showinfo("Data Deleted", "Details deleted successfully")
            fetch()
            clear()
        mydatabase.close()

    # Function to clear the inputs in entry widget.

    def clear():
        g_no.set("")
        name.set("")
        age.set("")
        gender.set("")
        address.set("")
        contact.set("")
        room.set("")
        checkindate.set("")
        checkoutdate.set("")

    # Function to search data:

    def search():
        mydatabase = mysql.connector.connect(host="localhost", user="root", passwd='sufi')
        mycursor = mydatabase.cursor()
        if combo_var.get() == "" or entry_var.get() == "":
            messagebox.showerror("Error", "Please enter a data to search")
        elif combo_var.get() == "" and entry_var.get() == "":
            messagebox.showerror("Error", "Please enter a data to search")
        else:
            mycursor.execute("use hotel_dbms")
            mycursor.execute(
                "select * from info where " + str(combo_var.get()) + " like '%" + str(entry_var.get()) + "%'")
            query = mycursor.fetchall()
            if len(query) != 0:
                info_table.delete(*info_table.get_children())
                i = 0
                for row in query:
                    info_table.insert('', i, text="",
                                      values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
                    i = i + 1
                mydatabase.commit()
                clear_search()
        mydatabase.close()

    # Setting Background Image:

    photo = PhotoImage(file="HotelInterior.png")
    img = Label(root, image=photo)
    img.pack()

    # Frame 1 - For making entry fields:

    frame1 = Frame(root, bg="peach puff", borderwidth=6, relief=RIDGE)
    frame1.place(x=20, y=100, width=450, height=620)

    l_title = Label(frame1, text=" Manage Details ", font=("Cambria", 30, "bold"), bg="peach puff", fg="black")
    l_title.grid(row=0, columnspan=2, pady=15)

    l_gno = Label(frame1, text="Guest No.", font=("lato", 13, "bold"), bg="peach puff", fg="black")
    l_gno.grid(row=1, column=0, pady=10, padx=30, sticky="w")
    ent_gno = Entry(frame1, font=("lato", 13, "bold"), textvariable=g_no, borderwidth=4, relief=GROOVE)
    ent_gno.grid(row=1, column=1, pady=10, padx=30, sticky="w")

    l_name = Label(frame1, text="Guest's Name", font=("lato", 13, "bold"), bg="peach puff", fg="black")
    l_name.grid(row=2, column=0, pady=10, padx=30, sticky="w")
    ent_name = Entry(frame1, font=("lato", 13, "bold"), textvariable=name, borderwidth=4, relief=GROOVE)
    ent_name.grid(row=2, column=1, pady=10, padx=30, sticky="w")

    l_age = Label(frame1, text="Age", font=("lato", 13, "bold"), bg="peach puff", fg="black")
    l_age.grid(row=3, column=0, pady=10, padx=30, sticky="w")
    ent_age = Entry(frame1, font=("lato", 13, "bold"), textvariable=age, borderwidth=4, relief=GROOVE)
    ent_age.grid(row=3, column=1, pady=10, padx=30, sticky="w")

    l_gender = Label(frame1, text="Gender", font=("lato", 13, "bold"), bg="peach puff", fg="black")
    l_gender.grid(row=4, column=0, pady=10, padx=30, sticky="w")
    ent_gender = Entry(frame1, font=("lato", 13, "bold"), textvariable=gender, borderwidth=4, relief=GROOVE)
    ent_gender.grid(row=4, column=1, pady=10, padx=30, sticky="w")

    l_address = Label(frame1, text="Address", font=("lato", 13, "bold"), bg="peach puff", fg="black")
    l_address.grid(row=5, column=0, pady=10, padx=30, sticky="w")
    ent_address = Entry(frame1, font=("lato", 13, "bold"), textvariable=address, borderwidth=4, relief=GROOVE)
    ent_address.grid(row=5, column=1, pady=10, padx=30, sticky="w")

    l_contact = Label(frame1, text="Contact No.", font=("lato", 13, "bold"), bg="peach puff", fg="black")
    l_contact.grid(row=6, column=0, pady=10, padx=30, sticky="w")
    ent_contact = Entry(frame1, font=("lato", 13, "bold"), textvariable=contact, borderwidth=4, relief=GROOVE)
    ent_contact.grid(row=6, column=1, pady=10, padx=30, sticky="w")

    l_room = Label(frame1, text="Room No.", font=("lato", 13, "bold"), bg="peach puff", fg="black")
    l_room.grid(row=7, column=0, pady=10, padx=30, sticky="w")
    ent_room = Entry(frame1, font=("lato", 13, "bold"), textvariable=room, borderwidth=4, relief=GROOVE)
    ent_room.grid(row=7, column=1, pady=10, padx=30, sticky="w")

    l_checkindate = Label(frame1, text="Check-in Date", font=("lato", 13, "bold"), bg="peach puff", fg="black")
    l_checkindate.grid(row=8, column=0, pady=10, padx=30, sticky="w")
    ent_checkindate = Entry(frame1, font=("lato", 13, "bold"), textvariable=checkindate, borderwidth=4, relief=GROOVE)
    ent_checkindate.grid(row=8, column=1, pady=10, padx=30, sticky="w")

    l_checkoutdate = Label(frame1, text="Check-out Date", font=("lato", 13, "bold"), bg="peach puff", fg="black")
    l_checkoutdate.grid(row=9, column=0, pady=10, padx=30, sticky="w")
    ent_checkoutdate = Entry(frame1, font=("lato", 13, "bold"), textvariable=checkoutdate, borderwidth=4, relief=GROOVE)
    ent_checkoutdate.grid(row=9, column=1, pady=10, padx=30, sticky="w")

    # Frame for Buttons:

    frame_btn = Frame(frame1, borderwidth=3, relief=RIDGE, bg="black")
    frame_btn.place(x=10, y=550, width=420)

    # Buttons:

    b1 = Button(frame_btn, text="Add", font=("cambria", 10, "bold"), width=9, command=add)
    b1.grid(row=0, column=0, padx=10, pady=10)

    b2 = Button(frame_btn, text="Update", font=("cambria", 10, "bold"), width=9, command=update)
    b2.grid(row=0, column=1, padx=10, pady=10)

    b3 = Button(frame_btn, text="Delete", font=("cambria", 10, "bold"), width=9, command=delete)
    b3.grid(row=0, column=2, padx=10, pady=10)

    b4 = Button(frame_btn, text="Clear", font=("cambria", 10, "bold"), width=9, command=clear)
    b4.grid(row=0, column=3, padx=10, pady=10)

    # Frame 2:

    frame2 = Frame(root, bg="peach puff", borderwidth=6, relief=RIDGE)
    frame2.place(x=500, y=100, width=1000, height=620)

    # Creating Search Box to search a particular data:

    d_search = Label(frame2, text="Search By:", font="Cambria 16 bold", bg="peach puff", fg="black", borderwidth=4)
    d_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

    # Search Combobox

    combo_var = StringVar()
    combo_search = ttk.Combobox(frame2, font="Cambria 16 bold", state='readonly', textvariable=combo_var)
    combo_search['values'] = ("GuestNo", "GuestName", "Age", "Address", "RoomNo", "CheckinDate", "CheckoutDate")
    combo_search.grid(row=0, column=1, padx=20, pady=10)

    # Search Box:

    entry_var = StringVar()
    entry_search = Entry(frame2, font="Cambria 16 bold", width=20, borderwidth=3, relief=GROOVE, textvariable=entry_var)
    entry_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

    # Search Button and Show table/data Button:

    search_btn = Button(frame2, text="Search", command=search, font=("cambria", 11, "bold"), width=10, pady=5)
    search_btn.grid(row=0, column=3, padx=10, pady=10)

    show_btn = Button(frame2, text="Show All", command=fetch, font=("cambria", 11, "bold"), width=10, pady=5)
    show_btn.grid(row=0, column=4, padx=10, pady=10)

    # Function for clearing entries:

    def clear_search():
        combo_var.set("")
        entry_var.set("")

    # Frame for Table:

    frame_table = Frame(frame2, relief=SUNKEN)
    frame_table.place(x=10, y=70, width=970, height=530)

    # Displaying the Table with treeview:

    info_table = ttk.Treeview(frame_table)
    info_table['show'] = 'headings'

    style = ttk.Style(frame_table)
    style.theme_use()

    style.configure(".", font=("arial", 10), background="peach puff")
    style.configure("Treeview.Heading", font=("arial", 10, "bold"), foreground="PeachPuff4")

    info_table["columns"] = ("GuestNo", "GuestName", "Age", "Gender", "Address", "ContactNo", "RoomNo", "Checkindate", "Checkoutdate")

    info_table.column("GuestNo", width=80, minwidth=80, anchor=CENTER)
    info_table.column("GuestName", width=200, minwidth=200, anchor=CENTER)
    info_table.column("Age", width=70, minwidth=70, anchor=CENTER)
    info_table.column("Gender", width=80, minwidth=80, anchor=CENTER)
    info_table.column("Address", width=250, minwidth=250, anchor=CENTER)
    info_table.column("ContactNo", width=110, minwidth=110, anchor=CENTER)
    info_table.column("RoomNo", width=80, minwidth=80, anchor=CENTER)
    info_table.column("Checkindate", width=120, minwidth=120, anchor=CENTER)
    info_table.column("Checkoutdate", width=120, minwidth=120, anchor=CENTER)

    info_table.heading("GuestNo", text="Guest No.", anchor=CENTER)
    info_table.heading("GuestName", text="Guest's Name", anchor=CENTER)
    info_table.heading("Age", text="Age", anchor=CENTER)
    info_table.heading("Gender", text="Gender", anchor=CENTER)
    info_table.heading("Address", text="Address", anchor=CENTER)
    info_table.heading("ContactNo", text="Contact No.", anchor=CENTER)
    info_table.heading("RoomNo", text="Room No.", anchor=CENTER)
    info_table.heading("Checkindate", text="Check-in Date", anchor=CENTER)
    info_table.heading("Checkoutdate", text="Check-out Date", anchor=CENTER)
    info_table.bind('<ButtonRelease-1>', getvals)
    fetch()

    horizontal_scr = ttk.Scrollbar(frame_table, orient=HORIZONTAL)
    vertical_scr = ttk.Scrollbar(frame_table, orient=VERTICAL)

    horizontal_scr.configure(command=info_table.xview)
    vertical_scr.configure(command=info_table.yview)
    info_table.configure(xscrollcommand=horizontal_scr.set, yscrollcommand=vertical_scr.set)
    horizontal_scr.pack(fill=X, side=BOTTOM)
    vertical_scr.pack(fill=Y, side=RIGHT)

    info_table.pack(fill=BOTH, expand=1)

    root.mainloop()


# Creating Password for Program:

def passw():
    if password.get() == "admin@123":  # You can change the password
        messagebox.showinfo("Verified", "Verification Successful!")
        verification.destroy()
        mainwindow()
    elif password.get() == "":
        messagebox.showerror("Error", "Password Required")
    else:
        messagebox.showerror("Error", "Wrong Password, Try again")


# Creating Welcome Screen

verification = Tk()
verification.geometry("1280x720")
verification.title("Verify")
verification.resizable("False", "False")
verification.wm_iconbitmap("Icon.ico")

back = PhotoImage(file="Hotel_DBMS.png")
lab = Label(verification, image=back)
lab.pack()

password = StringVar()
frame = Frame(verification, bg="gray27", borderwidth=4)
frame.place(x=310, y=250, width=700, height=300)

title_label1 = Label(frame, text="Welcome", font=("Cambria", 42, "bold"), bg="gray27", fg="white", padx=215, pady=20)
title_label1 .grid(row=0, column=0)

title_label2 = Label(frame, text="Enter Password to Verify your Identity", font=("lato", 20, "bold"), bg="gray27", fg="white")
title_label2.grid(row=1, column=0, padx=15, pady=5)
title_entry = Entry(frame, font=("lato", 16, "bold"), textvariable=password, bd=4, relief=GROOVE)
title_entry.grid(row=2, column=0, pady=10)

btn = Button(frame, text="Verify", font="Cambria 13 bold", width=10, command=passw, bg="white", fg="black")
btn.grid(row=3, columnspan=2, padx=15, pady=10)


verification.mainloop()
