"""
A program that records data entered manually by technicians on the production line regarding breakdowns
or any other interruptions.

This form stores:

date of breakdown,
machineID/ name,
tech lead working on affected machine,
machine downtime,
tech downtime,
job status,
description of fault,
repair comments,
job type,
job category
and verification steps taken for its release

Users can:
View all records,
Search for an entry,
Update existing entry,
Delete entries,
Export entries to excel

 """

from back import Database
from tkinter import *
from tkinter import ttk

database = Database('test.db')

machine_list = ['Machine#1', 'Machine#2']
tech_list = ['Tech#1', 'Tech#2']
status_list = ['Status#1', 'Status#2']
job_type_list = ['jt#1', 'jt#2', 'jt#3']
job_cat_list = ['jc#1', 'jc#2', 'jc#3']
ver_list = ['v#1', 'v#2']


class Window(object):
    def __init__(self, window):
        self.window = window
        self.window.wm_title("Machine Fault Log")

        l1 = Label(window, text="Date")
        l1.grid(row=0, column=0)
        self.date_text = StringVar()
        self.e1 = Entry(window, textvariable=self.date_text, width=10)
        self.e1.grid(row=0, column=1)

        l2 = Label(window, text="Machine ID", width=10)
        l2.grid(row=1, column=0)

        self.machine_id_text = StringVar()
        self.e2 = ttk.Combobox(window, textvariable=self.machine_id_text, values=machine_list, width=10)
        self.e2.grid(row=1, column=1)

        l3 = Label(window, text="Tech Lead", width=10)
        l3.grid(row=2, column=0)

        self.tech_text = StringVar()
        self.e3 = ttk.Combobox(window, textvariable=self.tech_text, values=tech_list, width=10)
        self.e3.grid(row=2, column=1)

        l4 = Label(window, text="Machine Downtime")
        l4.grid(row=3, column=0)

        self.machine_down_text = StringVar()
        self.e4 = Entry(window, textvariable=self.machine_down_text, width=5)
        self.e4.grid(row=3, column=1)

        l5 = Label(window, text="Tech Downtime")
        l5.grid(row=4, column=0)

        self.tech_down_text = StringVar()
        self.e5 = Entry(window, textvariable=self.tech_down_text, width=5)
        self.e5.grid(row=4, column=1)

        l6 = Label(window, text="Status")
        l6.grid(row=5, column=0)

        self.status_text = StringVar()
        self.e6 = ttk.Combobox(window, textvariable=self.status_text, values=status_list, width=10)
        self.e6.grid(row=5, column=1)

        l7 = Label(window, text="Fault Description/Comments")
        l7.grid(row=6, column=0)
        self.t1 = Text(window, height=8, width=40)
        self.t1.grid(row=7, column=0, columnspan=2)

        l8 = Label(window, text="Repair/Resolution Details")
        l8.grid(row=8, column=0)
        self.t2 = Text(window, height=10, width=40)
        self.t2.grid(row=9, column=0, columnspan=2)

        l9 = Label(window, text="Job Type", width=10)
        l9.grid(row=10, column=0)

        self.job_type_text = StringVar()
        self.e7 = ttk.Combobox(window, textvariable=self.job_type_text, values=job_type_list, width=10)
        self.e7.grid(row=10, column=1)

        l10 = Label(window, text="Job Category", width=10)
        l10.grid(row=11, column=0)

        self.job_cat_text = StringVar()
        self.e8 = ttk.Combobox(window, textvariable=self.job_cat_text, values=job_cat_list, width=10)
        self.e8.grid(row=11, column=1)

        l11 = Label(window, text="Verification", width=10)
        l11.grid(row=12, column=0)

        self.ver_text = StringVar()
        self.e9 = ttk.Combobox(window, textvariable=self.ver_text, values=ver_list, width=10)
        self.e9.grid(row=12, column=1)

        b1 = Button(window, text="Submit Entry", command=self.add_command)
        b1.grid(row=13, column=0)

        b2 = Button(window, text="Clear Fields", command=self.clear_entries)
        b2.grid(row=13, column=1)

        b3 = Button(window, text="View all", command=self.view_command)
        b3.grid(row=0, column=2)

        b4 = Button(window, text="Search Entry", command=self.search_command)
        b4.grid(row=0, column=3)

        b5 = Button(window, text="Update Selected", command=self.update_command)
        b5.grid(row=0, column=4)

        b6 = Button(window, text="Delete Selected", command=self.delete_command)
        b6.grid(row=0, column=5)

        b7 = Button(window, text="Export Entries")
        b7.grid(row=0, column=6)

        self.list1 = Listbox(window, height=40, width=65)
        self.list1.grid(row=1, column=2, rowspan=12, columnspan=6)

        sb1 = Scrollbar(window)
        sb1.grid(row=1, column=8, rowspan=12)

        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

    def get_selected_row(self, event):
        index = self.list1.curselection()[0]
        self.selected_tuple = self.list1.get(index)
        self.e1.delete(0, END)
        self.e1.insert(END, self.selected_tuple[1])
        self.e2.delete(0, END)
        self.e2.insert(END, self.selected_tuple[2])
        self.e3.delete(0, END)
        self.e3.insert(END, self.selected_tuple[3])
        self.e4.delete(0, END)
        self.e4.insert(END, self.selected_tuple[4])
        self.e5.delete(0, END)
        self.e5.insert(END, self.selected_tuple[5])
        self.e6.delete(0, END)
        self.e6.insert(END, self.selected_tuple[6])
        self.t1.delete('1.0', END)
        self.t1.insert(END, self.selected_tuple[7])
        self.t2.delete('1.0', END)
        self.t2.insert(END, self.selected_tuple[8])
        self.e7.delete(0, END)
        self.e7.insert(END, self.selected_tuple[9])
        self.e8.delete(0, END)
        self.e8.insert(END, self.selected_tuple[10])
        self.e9.delete(0, END)
        self.e9.insert(END, self.selected_tuple[11])

    def view_command(self):
        self.list1.delete(0, END)
        for row in database.view_all():
            self.list1.insert(END, row)

    def clear_entries(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)
        self.e5.delete(0, END)
        self.e6.delete(0, END)
        self.t1.delete('1.0', END)
        self.t2.delete('1.0', END)
        self.e7.delete(0, END)
        self.e8.delete(0, END)
        self.e9.delete(0, END)

    def search_command(self):
        self.list1.delete(0, END)
        for row in database.search_entry(self.date_text.get(), self.machine_id_text.get(),
                                self.tech_text.get(), self.machine_down_text.get(), self.tech_down_text.get(),
                                self.status_text.get(), self.t1.get('1.0', END), self.t2.get('1.0', END),
                                self.job_type_text.get(),
                                self.job_cat_text.get(), self.ver_text.get()):
            self.list1.insert(END, row)

    def add_command(self):
        database.insert_entry(self.date_text.get(), self.machine_id_text.get(),
                              self.tech_text.get(), self.machine_down_text.get(), self.tech_down_text.get(),
                              self.status_text.get(), self.t1.get('1.0', END), self.t2.get('1.0', END),
                              self.job_type_text.get(),
                              self.job_cat_text.get(), self.ver_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.date_text.get(), self.machine_id_text.get(),
                                self.tech_text.get(), self.machine_down_text.get(), self.tech_down_text.get(),
                                self.status_text.get(), self.t1.get('1.0', END), self.t2.get('1.0', END),
                                self.job_type_text.get(),
                                self.job_cat_text.get(), self.ver_text.get()))

    def delete_command(self):
        database.delete_entry(self.selected_tuple[0])

    def update_command(self):
        database.update_entry(self.date_text.get(), self.machine_id_text.get(),
                                self.tech_text.get(), self.machine_down_text.get(), self.tech_down_text.get(),
                                self.status_text.get(), self.t1.get('1.0', END), self.t2.get('1.0', END),
                                self.job_type_text.get(),
                                self.job_cat_text.get(), self.ver_text.get())


window = Tk()
Window(window)
window.mainloop()
