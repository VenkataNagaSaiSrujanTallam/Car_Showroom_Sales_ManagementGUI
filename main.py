import mysql.connector as con
from tkinter import *
from tkinter import ttk
from tabulate import tabulate
import matplotlib.pyplot as plt
from collections import OrderedDict

c = 0

window = Tk()

notebook = ttk.Notebook(window)

display_data = Frame(notebook, width=window.winfo_screenwidth()//2+250, height=window.winfo_screenheight()//2+250)
manage_data = Frame(notebook, width=window.winfo_screenwidth()//2+250, height=window.winfo_screenheight()//2+250)
report = Frame(notebook, width=window.winfo_screenwidth()//2+249, height=window.winfo_screenheight()//2+250)
notebook.pack()

notebook.add(display_data, text="Display data")
notebook.add(manage_data, text="Manage Data")
notebook.add(report, text="Generate Report")

option_see = [
    "Whole data",
    "Particular data"
]

option_table = [
    "Sales",
    "Cust",
    "Product"
]

manage_table = [
    "Add Data",
    "Delete Data",
    "Update Data"
]


columns = [["S.no", "Cust ID", "Product name", "Product ID", "Sale Price", "Date of sale"],
           ["Cust ID", "Customer Name", "Phone", "Address", "Aadhaar number"],
           ["Product ID", "Product Name", "Price"]]

tables = StringVar()
tables.set("Sales")

tables2 = StringVar()
tables2.set("Sales")

select = StringVar()
select.set("Whole data")

manage = StringVar()
manage.set("Add data")


def report_maker():
    cursor.execute("SELECT SUM(sale_price), MONTHNAME(date_sales) FROM Sales GROUP BY MONTHNAME(date_sales);")
    plot_data = cursor.fetchall()
    print(plot_data)
    plotter = {}
    for i in plot_data:
        plotter[i[1]] = i[0]
    print(plotter)
    month_names = list(plotter.keys())
    values = list(plotter.values())
    plt.bar(range(len(plotter)), values, tick_label=month_names)
    plt.show()


def particular(e):
    if select.get() == "Particular data":
        enter.config(state=NORMAL)
        name = tables.get()
        if name == "Sales":
            l1.config(text="Enter the s.no")
        if name == "Cust":
            l1.config(text="Enter the cust_id")
        if name == "Product":
            l1.config(text="Enter the product id")

    if select.get() == "Whole data":
        enter.config(state=DISABLED)
        l1.config(text="")


def creater():
    global c
    table_name = tables.get()
    if select.get() == "Whole data":
        if table_name == "Sales":
            cursor.execute("SELECT * FROM Sales;")
            c = 0
        if table_name == "Cust":
            cursor.execute("SELECT * FROM Cust;")
            c = 1
        if table_name == "Product":
            cursor.execute("SELECT * FROM Product;")
            c = 2

    if select.get() == "Particular data":
        id = enter.get()
        print(id)
        if id != "":
            if table_name == "Sales":
                cursor.execute("SELECT * FROM Sales where s_no = "+id+";")
                c = 0
            if table_name == "Cust":
                cursor.execute("SELECT * FROM Cust where cust_id = "+id+";")
                c = 1
            if table_name == "Product":
                cursor.execute("SELECT * FROM Product where product_id = "+id+";")
                c = 2

    data = cursor.fetchall()

    if data == []:
        l = []
        for r in range(0, len(columns[c])):
            r = "None"
            l.append(r)
        data = [l]

    print(data)
    j = []
    for i in data:
        i = list(i)
        j.append(i)
    print(j)
    tab = tabulate(j, headers=columns[c], tablefmt="grid", numalign="left", stralign="left")
    print(tab)
    data_label.config(text=tab)


def manager(e):
    if manage.get() == "Update Data":
        name = tables2.get()
        if name == "Sales":
            label1.config(text="Enter the s.no of data to change")
            enter1.config(state=NORMAL)
            label2.config(text="Enter the new sale price")
            enter2.config(state=NORMAL)
            enter3.config(state=DISABLED)
            enter4.config(state=DISABLED)
            enter5.config(state=DISABLED)
            enter6.config(state=DISABLED)
            label3.config(text="")
            label4.config(text="")
            label5.config(text="")
            label6.config(text="")

        if name == "Cust":
            label1.config(text="Enter the cust id of data to change")
            enter1.config(state=NORMAL)
            label2.config(text="Enter the new customer name")
            enter2.config(state=NORMAL)
            enter3.config(state=DISABLED)
            enter4.config(state=DISABLED)
            enter5.config(state=DISABLED)
            enter6.config(state=DISABLED)
            label3.config(text="")
            label4.config(text="")
            label5.config(text="")
            label6.config(text="")

        if name == "Product":
            label1.config(text="Enter the Product id of data to change")
            enter1.config(state=NORMAL)
            label2.config(text="Enter the new product price")
            enter2.config(state=NORMAL)
            enter3.config(state=DISABLED)
            enter4.config(state=DISABLED)
            enter5.config(state=DISABLED)
            enter6.config(state=DISABLED)
            label3.config(text="")
            label4.config(text="")
            label5.config(text="")
            label6.config(text="")

    if manage.get() == "Delete Data":
        name = tables2.get()
        if name == "Sales":
            label1.config(text="Enter the s.no of data to delete")
            enter1.config(state=NORMAL)
            enter2.config(state=DISABLED)
            enter3.config(state=DISABLED)
            enter4.config(state=DISABLED)
            enter5.config(state=DISABLED)
            enter6.config(state=DISABLED)
            label2.config(text="")
            label3.config(text="")
            label4.config(text="")
            label5.config(text="")
            label6.config(text="")

        if name == "Cust":
            label1.config(text="Enter the cust id of data to delete")
            enter1.config(state=NORMAL)
            enter2.config(state=DISABLED)
            enter3.config(state=DISABLED)
            enter4.config(state=DISABLED)
            enter5.config(state=DISABLED)
            enter6.config(state=DISABLED)
            label2.config(text="")
            label3.config(text="")
            label4.config(text="")
            label5.config(text="")
            label6.config(text="")

        if name == "Product":
            label1.config(text="Enter the product id of data to delete")
            enter1.config(state=NORMAL)
            enter2.config(state=DISABLED)
            enter3.config(state=DISABLED)
            enter4.config(state=DISABLED)
            enter5.config(state=DISABLED)
            enter6.config(state=DISABLED)
            label2.config(text="")
            label3.config(text="")
            label4.config(text="")
            label5.config(text="")
            label6.config(text="")

    if manage.get() == "Add Data":
        name = tables2.get()
        if name == "Sales":
            label1.config(text="Enter the s.no")
            enter1.config(state=NORMAL)
            label2.config(text="Enter the cust_id")
            enter2.config(state=NORMAL)
            enter3.config(state=NORMAL)
            enter4.config(state=NORMAL)
            enter5.config(state=NORMAL)
            enter6.config(state=NORMAL)
            label3.config(text="Enter Product name")
            label4.config(text="Enter Product id")
            label5.config(text="Enter Sales Price")
            label6.config(text="Enter date of sales(yyyy/mm/dd)")

        if name == "Cust":
            label1.config(text="Enter the cust id")
            enter1.config(state=NORMAL)
            label2.config(text="Enter the customer name")
            enter2.config(state=NORMAL)
            enter3.config(state=NORMAL)
            enter4.config(state=NORMAL)
            enter5.config(state=NORMAL)
            enter6.config(state=DISABLED)
            label3.config(text="Enter the custome phone no.")
            label4.config(text="Enter the cust_add")
            label5.config(text="Enter the customer aadhaar no.")
            label6.config(text="")

        if name == "Product":
            label1.config(text="Enter the Product ")
            enter1.config(state=NORMAL)
            label2.config(text="Enter the Product Name")
            enter2.config(state=NORMAL)
            enter3.config(state=NORMAL)
            enter4.config(state=DISABLED)
            enter5.config(state=DISABLED)
            enter6.config(state=DISABLED)
            label3.config(text="Enter the Product Price")
            label4.config(text="")
            label5.config(text="")
            label6.config(text="")


def action():
    if manage.get() == "Update Data":
        name = tables2.get()
        if name == "Sales":
            r = enter1.get()
            e = enter2.get()
            cursor.execute("UPDATE Sales SET sale_price = %s where s_no = %s;" % (e, r))

        if name == "Cust":
            r = enter1.get()
            e = enter2.get()
            cursor.execute("UPDATE Cust SET cust_name = %s where cust_id = %s;" % (e, r))

        if name == "Product":
            r = enter1.get()
            e = enter2.get()
            cursor.execute("UPDATE Product SET price = %s where product_id = %s;" % (e, r))

    if manage.get() == "Delete Data":
        name = tables2.get()
        if name == "Sales":
            r = enter1.get()
            cursor.execute("Delete FROM Sales where s_no = %s;" % r)

        if name == "Cust":
            r = enter1.get()
            cursor.execute("DELETE FROM Cust where cust_id = %s;" % r)

        if name == "Product":
            r = enter1.get()
            cursor.execute("DELETE FROM Product where product_id = %s;" % r)

    if manage.get() == "Add Data":
        name = tables2.get()
        if name == "Sales":
            r = enter1.get()
            e = enter2.get()
            f = enter3.get()
            g = enter4.get()
            h = enter5.get()
            j = enter6.get()
            cursor.execute("INSERT INTO SALES VALUES(%s, %s, %s , %s, %s, %s);" % (r, e, f, g, h, j))

        if name == "Cust":
            r = enter1.get()
            e = enter2.get()
            f = enter3.get()
            g = enter4.get()
            h = enter5.get()
            cursor.execute("INSERT INTO Cust VALUES(%s, %s, %s , %s, %s);" % (r, e, f, g, h))

        if name == "Product":
            r = enter1.get()
            e = enter2.get()
            f = enter3.get()
            cursor.execute("INSERT INTO Product VALUES(%s, %s, %s);" % (r, e, f))


connected = con.connect(user="root", password="SRU#JAN9b", host="localhost", autocommit=True)
cursor = connected.cursor()
cursor.execute("SHOW Databases")
list_databases = cursor.fetchall()

for i in list_databases:
    if i == ("project", ):
        cursor.execute("USE project")
        cursor.execute("SHOW Tables")
        list_tables = cursor.fetchall()
        print(list_tables)
        if list_tables.count(('sales',)) == 0:
            cursor.execute("CREATE TABLE Sales(s_no char(5) PRIMARY KEY, cust_id char(5) NOT NULL, Product_name varchar(100), Product_id char(20) NOT NULL, sale_price int NOT NULL, date_sales varchar(50));")
        if list_tables.count(("cust",)) == 0:
            cursor.execute("CREATE TABLE Cust(cust_id char(5) PRIMARY KEY, cust_name varchar(50), cust_ph varchar(10), cust_add varchar(250), cust_aadhaar_no varchar(15));")
        if list_tables.count(("product",)) == 0:
            cursor.execute("CREATE TABLE Product(Product_id char(20) PRIMARY KEY, Product_name varchar(100), price int);")
        else:
            pass


window.title("Lykos Cars- Management system")
window.geometry(str(window.winfo_screenwidth()//2+250)+"x"+str(window.winfo_screenheight()//2+250))
window.resizable(False, False)
icon = PhotoImage(file="logopng.png")
window.iconphoto(True, icon)
# --------------------------------------------------------Display Data ------------------------------------------------
menu = OptionMenu(display_data, tables, *option_table)
menu.pack(anchor=W)

Label(display_data, text="", pady=15).pack()

menu2 = OptionMenu(display_data, select, *option_see, command=particular)
menu2.pack(anchor=W)

Label(display_data, text="", pady=15).pack()

l1 = Label(display_data, text="")
l1.pack(anchor=W)

enter = Entry(display_data, state=DISABLED)
enter.pack(anchor=W)

Button(display_data, text="show data", command=creater).pack()

data_label = Label(display_data, text="", justify=LEFT, font=("Cascadia Mono", 10))
data_label.pack()

Label(display_data, text="", pady=15).pack()

# ----------------------------------------------------Manage Data-------------------------------------------------------
menu3 = OptionMenu(manage_data, tables2, *option_table)
menu3.pack(anchor=W)

Label(manage_data, text="", pady=15).pack()

menu4 = OptionMenu(manage_data, manage, *manage_table, command=manager)
menu4.pack(anchor=W)

Label(manage_data, text="", pady=15).pack()

label1 = Label(manage_data, text="")
label1.pack(anchor=W)

enter1 = Entry(manage_data, state=DISABLED)
enter1.pack(anchor=W)

label2 = Label(manage_data, text="")
label2.pack(anchor=W)

enter2 = Entry(manage_data, state=DISABLED)
enter2.pack(anchor=W)

label3 = Label(manage_data, text="")
label3.pack(anchor=W)

enter3 = Entry(manage_data, state=DISABLED)
enter3.pack(anchor=W)

label4 = Label(manage_data, text="")
label4.pack(anchor=W)

enter4 = Entry(manage_data, state=DISABLED)
enter4.pack(anchor=W)

label5 = Label(manage_data, text="")
label5.pack(anchor=W)

enter5 = Entry(manage_data, state=DISABLED)
enter5.pack(anchor=W)

label6 = Label(manage_data, text="")
label6.pack(anchor=W)

enter6 = Entry(manage_data, state=DISABLED)
enter6.pack(anchor=W)

take_button = Button(manage_data, text="make changes", command=action)
take_button.pack(anchor=N)
# --------------------------------------------------Generate Report ----------------------------------------------------
Label(report, text="", pady=100, padx=500).pack()

button2 = Button(report, text="Generate Sales Report Month Wise", command=report_maker,
                 font=("Comics San", 40))
button2.pack(anchor=N)

Label(report, text="", pady=250, padx=500).pack()

window.mainloop()
connected.close()
